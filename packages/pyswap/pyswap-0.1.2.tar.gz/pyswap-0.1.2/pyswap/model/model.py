"""The main model class.

Classes:
    Model: Main class that runs the SWAP model.
"""

from ..core import PySWAPBaseModel
from ..core import open_file
from typing import Optional, Any
from pathlib import Path
import shutil
import tempfile
import subprocess
import os
from importlib import resources
from pandas import read_csv, to_datetime
from numpy import nan
from ..soilwater import SnowAndFrost
from ..simsettings import RichardsSettings
from ..extras import HeatFlow, SoluteTransport
from .result import Result
import warnings
import platform

IS_WINDOWS = platform.system() == 'Windows'


class Model(PySWAPBaseModel):
    """Main class that runs the SWAP model.

    The attributes must be valid pySWAP classes. For avoiding validation errors,
    for now the attributes are defined as Any.

    Attributes:
        metadata (Any): Metadata of the model.
        general_settings (Any): Simulation settings.
        meteorology (Any): Meteorological data.
        crop (Any): Crop data.
        fixedirrigation (Any): Fixed irrigation settings.
        soilmoisture (Any): Soil moisture data.
        surfaceflow (Any): Surface flow data.
        evaporation (Any): Evaporation data.
        soilprofile (Any): Soil profile data.
        snowandfrost (Optional[Any]): Snow and frost data.
        richards (Optional[Any]): Richards data.
        lateraldrainage (Any): Lateral drainage data.
        bottomboundary (Any): Bottom boundary data.
        heatflow (Optional[Any]): Heat flow data.
        solutetransport (Optional[Any]): Solute transport data.

    Methods:
        write_swp: Write the .swp input file.
        _copy_executable: Copy the appropriate SWAP executable to the temporary directory.
        _run_swap: Run the SWAP executable.
        _read_output: Read the output file.
        _read_output_tz: Read the output file with time zone.
        _read_vap: Read the .vap output file.
        _write_inputs: Write the input files.
        _identify_warnings: Identify warnings in the log file.
        _raise_swap_warning: Raise a warning.
        _save_old_output: Save the old output files.
        run: Run the model.
    """

    metadata: Any
    general_settings: Any
    meteorology: Any
    crop: Any
    fixedirrigation: Any
    soilmoisture: Any
    surfaceflow: Any
    evaporation: Any
    soilprofile: Any
    snowandfrost: Optional[Any] = SnowAndFrost(swsnow=0, swfrost=0)
    richards: Optional[Any] = RichardsSettings(swkmean=1, swkimpl=0)
    lateraldrainage: Any
    bottomboundary: Any
    heatflow: Optional[Any] = HeatFlow(swhea=0)
    solutetransport: Optional[Any] = SoluteTransport(swsolu=0)

    def write_swp(self, path: str) -> None:
        """Write the .swp input file."""

        string = self._concat_sections()
        self.save_element(string=string, path=path,
                          filename='swap', extension='swp')
        print('swap.swp saved.')

    @staticmethod
    def _copy_executable(tempdir: Path):
        """Copy the appropriate SWAP executable to the temporary directory."""
        if IS_WINDOWS:
            exec_path = resources.files(
                "pyswap.libs.swap420-exe").joinpath("swap.exe")
            shutil.copy(str(exec_path), str(tempdir))
            print('Copying the windows version of SWAP into temporary directory...')
        else:
            exec_path = resources.files(
                "pyswap.libs.swap420-linux").joinpath("swap420")
            shutil.copy(str(exec_path), str(tempdir))
            print('Copying linux executable into temporary directory...')

    @staticmethod
    def _run_swap(tempdir: Path) -> str:
        """Run the SWAP executable."""
        swap_path = Path(tempdir, 'swap.exe') if IS_WINDOWS else './swap420'

        p = subprocess.Popen(swap_path,
                             stdout=subprocess.PIPE,
                             stdin=subprocess.PIPE,
                             stderr=subprocess.STDOUT,
                             cwd=tempdir)

        return p.communicate(input=b'\n')[0].decode()

    @staticmethod
    def _read_output(path: Path):
        df = read_csv(path, comment='*', index_col='DATETIME')
        df.index = to_datetime(df.index)

        return df

    @staticmethod
    def _read_output_tz(path: Path):
        df = read_csv(path, comment='*', index_col='DATE')
        df.index = to_datetime(df.index)

        return df

    @staticmethod
    def _read_vap(path: Path):
        df = read_csv(path, skiprows=11, encoding_errors='replace')
        df.columns = df.columns.str.strip()
        df.replace(r'^\s*$', nan, regex=True, inplace=True)
        return df

    def _write_inputs(self, path: str) -> None:
        print('Preparing files...')
        self.write_swp(path)
        if self.lateraldrainage.drafile:
            self.lateraldrainage.write_dra(path)
        if self.crop.cropfiles:
            self.crop.write_crop(path)
        if self.meteorology.metfile:
            self.meteorology.write_met(path)
        if self.fixedirrigation.irgfile:
            self.irrigation.fixedirrig.write_irg(path)

    @staticmethod
    def _identify_warnings(log: str) -> list[Warning]:
        lines = log.split('\n')
        warnings = [line for line in lines
                    if line.strip().lower().startswith('warning')]

        return warnings

    def _raise_swap_warning(self, message):
        warnings.warn(message, Warning, stacklevel=3)

    def _save_old_output(self, tempdir: Path):
        list_dir = os.listdir(tempdir)
        list_dir = [f for f in list_dir if not f.find(
            'result') and not f.endswith('.csv')]

        if list_dir:
            dict_files = {f.split('.')[1]: open_file(Path(tempdir, f))
                          for f in list_dir}

        return dict_files

    def run(self, path: str | Path, silence_warnings: bool = False, old_output: bool = False):
        """Main function that runs the model.
        """
        with tempfile.TemporaryDirectory(dir=path) as tempdir:

            self._copy_executable(tempdir)
            self._write_inputs(tempdir)

            result = self._run_swap(tempdir)

            if 'normal completion' not in result:
                raise Exception(
                    f'Model run failed. \n {result}')

            print(result)

            log = open_file(Path(tempdir, 'swap_swap.log'))
            warnings = self._identify_warnings(log)

            if warnings and not silence_warnings:
                print('Warnings:')
                for warning in warnings:
                    self._raise_swap_warning(message=warning)

            if old_output:
                dict_files = self._save_old_output(tempdir)

            result = Result(
                output=self._read_output(
                    Path(tempdir, 'result_output.csv')),
                output_tz=self._read_output_tz(
                    Path(tempdir, 'result_output_tz.csv')) if self.general_settings.inlist_csv_tz else None,
                log=log,
                output_old=dict_files if old_output else None,
                warning=warnings
            )

            return result
