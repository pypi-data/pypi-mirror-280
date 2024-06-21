import os.path
import shutil
from subprocess import Popen, PIPE
from time import sleep, time

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By

from .service import Service
from .options import Options


class Element(WebElement):
    def __init__(self, parent, _id):
        super().__init__(parent, _id)

    def find_element(self, by=By.ID, value=None):
        elem = super().find_element(by, value)
        return Element(elem.parent, elem.id)

    def find_elements(self, by=By.ID, value=None):
        elems = super().find_elements(by, value)
        return [Element(elem.parent, elem.id) for elem in elems]

    def click(self, timeout=0.0, ignore_errors=False):
        start = time()
        current_exception = WebDriverException
        while time() - start <= timeout:
            try:
                super().click()
                return True
            except WebDriverException as exception:
                current_exception = exception
                sleep(0.1)
        if ignore_errors:
            return False
        raise current_exception

    def check_element(self, by=By.ID, value=None, timeout=0.0):
        start = time()
        while time() - start <= timeout:
            try:
                return self.find_element(by, value)
            except WebDriverException:
                sleep(0.1)
        return None

    def check_elements(self, by=By.ID, value=None, timeout=0.0):
        start_time = time()
        elems = self.find_elements(by, value)

        while not elems and time() - start_time <= timeout:
            elems = self.find_elements(by, value)
            sleep(0.1)
        return elems

    def send_keys(self, values, delay=0.25):
        timeout = delay // len(values)
        for value in values:
            super().send_keys(value)
            sleep(timeout)

    def is_exists(self):
        try:
            return self.is_displayed()
        except WebDriverException:
            return False


class Chrome(webdriver.Chrome):
    def __init__(self, options: Options = None, service: Service = None):
        super().__init__(options=options, service=service)

    def _wrap_value(self, value):
        if isinstance(value, Element):
            return {"element-6066-11e4-a52e-4f735466cecf": value.id}
        return super()._wrap_value(value)

    def _unwrap_value(self, value):
        if isinstance(value, dict) and "element-6066-11e4-a52e-4f735466cecf" in value:
            return Element(self, (value["element-6066-11e4-a52e-4f735466cecf"]))
        return super()._unwrap_value(value)

    def find_element(self, by=By.ID, value=None):
        elem = super().find_element(by, value)
        return Element(elem.parent, elem.id)

    def find_elements(self, by=By.ID, value=None):
        elems = super().find_elements(by, value)
        return [Element(elem.parent, elem.id) for elem in elems]

    def check_element(self, by=By.ID, value=None, timeout=0.0):
        start = time()
        while time() - start <= timeout:
            try:
                return self.find_element(by, value)
            except WebDriverException:
                sleep(0.1)
        return None

    def check_elements(self, by=By.ID, value=None, timeout=0.0):
        start_time = time()
        elems = self.find_elements(by, value)

        while not elems and time() - start_time <= timeout:
            elems = self.find_elements(by, value)
            sleep(0.1)
        return elems


class Shellium:
    def __init__(self, chromedriver_location=None,
                 binary_location=None, user_data_dir=None):
        # Setup options and service
        self._driver: Chrome | None = None
        self._options = Options()
        self._service = Service()

        # Setup paths
        if chromedriver_location:
            self.chromedriver_location = chromedriver_location
        if binary_location:
            self.binary_location = binary_location
        if user_data_dir:
            self.user_data_dir = user_data_dir

    # Setup methods
    @property
    def driver(self):
        return self._driver

    @property
    def options(self):
        return self._options

    @property
    def service(self):
        return self._service

    def launch(self):
        if self.driver:
            return None
        self._driver = Chrome(self.options, self.service)
        cmd = "Page.addScriptToEvaluateOnNewDocument"
        args = {'source': "delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;"
                          "delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;"
                          "delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;"
                          "const newProto = navigator.__proto__;"
                          "delete newProto.webdriver;"
                          "navigator.__proto__ = newProto;"}
        self.driver.execute_cdp_cmd(cmd, args)

    def terminate(self):
        if not self.driver:
            return
        self.driver.quit()
        self._driver = None

    def close(self):
        return self.driver.close()

    def make(self):
        if os.path.exists(self.user_data_dir):
            raise IsADirectoryError(f'{self.user_data_dir} already exists.')

        process = Popen([self.binary_location, '--no-startup-window',
                         f'--user-data-dir={self.user_data_dir}'], stdout=PIPE)
        _, error = process.communicate()
        if process.returncode != 0:
            raise RuntimeError(error)

    def unmake(self):
        self.terminate()
        shutil.rmtree(self.user_data_dir, ignore_errors=True)

    # Options methods
    @property
    def user_data_dir(self):
        return self.options.user_data_dir

    @user_data_dir.setter
    def user_data_dir(self, value):
        self.options.user_data_dir = value

    @property
    def binary_location(self):
        return self.options.binary_location

    @binary_location.setter
    def binary_location(self, value):
        self.options.binary_location = value

    # Service methods
    @property
    def chromedriver_location(self):
        return self.service.path

    @chromedriver_location.setter
    def chromedriver_location(self, value):
        self.service.path = value

    # URL methods
    def get(self, url):
        return self.driver.get(url)

    def refresh(self):
        return self.driver.refresh()

    def get_window_size(self):
        return self.driver.get_window_size()

    @property
    def current_url(self):
        return self.driver.current_url

    @property
    def title(self):
        return self.driver.title

    # Window methods
    @property
    def current_window_handle(self):
        return self.driver.current_window_handle

    @property
    def window_handles(self):
        return self.driver.window_handles

    @property
    def switch_to(self):
        return self.driver.switch_to

    # Execute methods
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    # Find&Check methods
    def find_element(self, by=By.ID, value=None):
        return self.driver.find_element(by, value)

    def find_elements(self, by=By.ID, value=None):
        return self.driver.find_elements(by, value)

    def check_element(self, by=By.ID, value=None, timeout=0.0):
        return self.driver.check_element(by, value, timeout)

    def check_elements(self, by=By.ID, value=None, timeout=0.0):
        return self.driver.check_elements(by, value, timeout)
