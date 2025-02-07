import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions


class WebDriverManager:
    def __init__(self ,driver_setting):
        self.init_driver(driver_setting)


    def add_driver_setting_arguments(self, config: json):
        if "prefs" in config:
            self.browser_options.add_experimental_option("prefs", config["prefs"])

        if "arguments" in config:
            for arg in config["arguments"]:
                self.browser_options.add_argument(arg)

        if "experimental_option" in config:
            for key,value in config["experimental_option"].items():
                print(f"add experimental_option : {key}, {value} ")
                self.browser_options.add_experimental_option(key,value)


    def init_driver(self, config: json):
        if not self.is_driver_alive():
            self.close_driver()
        if config["browser"] =="chrome":
            self.browser_options = ChromeOptions()
            self.add_driver_setting_arguments(config)
            service = ChromeService(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=self.browser_options)

        elif config["browser"] =="edge":
            self.browser_options = EdgeOptions()
            self.add_driver_setting_arguments(config)
            service = EdgeService(executable_path=config["driver_path"])
            self.driver = webdriver.Edge(service=service, options=self.browser_options)
        else:
            raise ValueError(f"Browser {config['browser']} doesn't exist !")


    def is_driver_alive(driver) -> bool:
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
            if n > 5 :
                print("Driver can't be closed")
                break

