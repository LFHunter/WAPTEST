import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import SessionNotCreatedException


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
                self.driver = webdriver.Chrome(
                    service=service, options=self.browser_options)
                print("erewrrwerwr")
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
        try:
            _ = driver.current_url
            return True
        except Exception:
            return False

    def close_driver(self):
        n = 0
        while self.is_driver_alive():
            n += 1
            self.driver.quit()
            if n > 5:
                print("Driver can't be closed")
                break
