import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import SessionNotCreatedException
from selenium.common.exceptions import WebDriverException, InvalidSessionIdException, NoSuchWindowException


class WebDriverManager:
    def __init__(self, driver_setting: json, driver_path: str = ""):
        self.driver_path = driver_path
        self.init_driver(driver_setting)

    def add_driver_setting_arguments(self, config: json):
        if "prefs" in config:
            print(f"add {config['prefs']}")
            self.browser_options.add_experimental_option(
                "prefs", config["prefs"])

        if "arguments" in config:
            for arg in config["arguments"]:
                print(f"add {arg}")
                self.browser_options.add_argument(arg)

        if "experimental_option" in config:
            for key, value in config["experimental_option"].items():
                print(f"add experimental_option : {key}, {value} ")
                self.browser_options.add_experimental_option(key, value)

    def init_driver(self, config: json):
        if not self.is_driver_alive():
            self.close_driver()
        if config["browser"] == "chrome":
            self.browser_options = ChromeOptions()
            self.add_driver_setting_arguments(config)
            try:
                service = ChromeService(ChromeDriverManager().install())
                print("Try to launch driver by ChromeService")
                self.driver = webdriver.Chrome(
                    service=service, options=self.browser_options)
            except SessionNotCreatedException as e:
                print(e)
                print(f"Due to ChromeDriverManager install driver fail, using\
                      config driver path:{self.driver_path}")
                service = ChromeService(self.driver_path)
                self.driver = webdriver.Chrome(
                    service=service, options=self.browser_options)
            except Exception as e:
                raise e

        else:
            raise ValueError(f"Browser {config['browser']} doesn't exist !")

    def is_driver_alive(driver: webdriver) -> bool:
        if driver is not None:
            try:
                return driver.session_id and driver.window_handles
            except Exception as e:
                print(e)
        return False

    def close_driver(self):
        n = 0
        while self.is_driver_alive():
            if n > 5:
                raise Exception("Driver can't be closed")
            n += 1
            try:
                if self.driver.session_id and self.driver.window_handles:
                    self.driver.quit()
            except (WebDriverException, InvalidSessionIdException, NoSuchWindowException) as e:
                print(f"Unable to quit WebDriver - {e}")
