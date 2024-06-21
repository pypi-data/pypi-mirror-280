from selenium.webdriver.chrome import options
from pathlib import Path


class Options(options.Options):
    def __init__(self, user_data_dir=None, binary_location=None):
        super().__init__()
        # Setup path to chrome.exe
        self._binary_location = Path('C:/Program Files/Google/Chrome/Application/chrome.exe')
        if binary_location:
            self.binary_location = binary_location

        # Setup path to User Data
        self._user_data_dir = Path.home() / 'AppData/Local/Google/Chrome/User Data'
        if user_data_dir:
            self.user_data_dir = user_data_dir
        arg = f"--user-data-dir={self.user_data_dir}"
        self.add_argument(arg)

        # Common options
        self.add_argument("--start-maximized")
        self.add_argument("–-disable-translate")
        self.add_argument("–disable-plugins")
        self.add_argument("--disable-extensions")

        # Setup undetected options
        self.add_argument("--disable-blink-features=AutomationControlled")
        self.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.add_experimental_option('useAutomationExtension', False)

    @property
    def binary_location(self):
        return str(self._binary_location)

    @binary_location.setter
    def binary_location(self, value):
        if not any(isinstance(value, cls) for cls in [str, Path]):
            raise TypeError(self.BINARY_LOCATION_ERROR)
        self._binary_location = Path(value).resolve()

    @property
    def user_data_dir(self) -> str:
        return str(self._user_data_dir)

    @user_data_dir.setter
    def user_data_dir(self, value):
        if not any(isinstance(value, cls) for cls in [str, Path]):
            raise TypeError(self.BINARY_LOCATION_ERROR)

        self._arguments = [argument for argument in self.arguments
                           if '--user-data-dir=' not in argument]
        self._user_data_dir = Path(value).absolute()
        self.add_argument(f"--user-data-dir={self.user_data_dir}")

    def __repr__(self):
        return f"<Options at 0x{id(self)}: {self._arguments}>"
