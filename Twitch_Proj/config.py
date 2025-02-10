import os
import datetime
now = datetime.datetime.now()
formatted_now = now.strftime("%Y-%m-%d_%H%M_%S")

# Path
file_path = os.path.abspath(__file__)
current_folder_path = os.path.dirname(file_path)
current_folder_name = os.path.basename(current_folder_path)

# url
twitch_url = "https://m.twitch.tv"


# Browser Driver
# [Backup] when webdriver-manager couldn't install the latest chromedriver
chrome_driver_path = r"c:/Users/paul/Desktop/openent/WAPTEST/Twitch_Proj/chromedriver.exe"

driver_setting = {
    "url": "",
    "browser": "chrome",
    "prefs": {
        "intl.accept_languages": "en-US"  # zh-TW,zh-HK,zh-CN,ja,en-US,ko
    },
    "experimental_option": {
        "mobileEmulation": {"deviceName": "iPhone 12 Pro"}
    },
    "arguments": [
        "--ignore-certificate-errors",
        "--disable-gpu",
        "--incognito"
        # "--headless"
    ]
}


# Log

log_config = {
    'version': 1,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'level': 'DEBUG'
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': f'{current_folder_name}/{formatted_now}_twitch.log',
            'formatter': 'standard',
            'level': 'DEBUG'
        }
    },
    'loggers': {
        '': {  # '' means root logger
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': False
        }
    }
}
