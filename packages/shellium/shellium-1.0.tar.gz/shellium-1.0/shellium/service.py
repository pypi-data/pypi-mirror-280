import re
from subprocess import Popen, PIPE
from selenium.webdriver.chrome import service
from pathlib import Path


class Service(service.Service):
    def __init__(self, executable_path=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._path = str(Path.cwd() / 'chromedriver.exe')
        if executable_path:
            self.path = executable_path

        # Определение версии chromedriver
        process = Popen([self.path, '--version'], stdout=PIPE)
        output, error = process.communicate()
        numbers = re.findall(r'\d+', output.decode())
        if not numbers:
            raise RuntimeError('The chromedriver version could not be determined.')
        if int(numbers[0]) < 116:
            raise RuntimeError(f'Chromedriver version less than 116 is not supported. Current version: {numbers[0]}.')

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        if not any(isinstance(value, cls) for cls in [str, Path]):
            raise TypeError(f"Invalid path type '{type(value)}'")
        self._path = str(value)
