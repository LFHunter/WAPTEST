import datetime
now = datetime.datetime.now()
formatted_now = now.strftime("%Y-%m-%d_%H%M_%S")


driver_setting = {
    "url" : "",
    "browser": "chrome",
    "driver_path": "",
    "prefs": {
        "intl.accept_languages": "en-US"  #zh-TW,zh-HK,zh-CN,ja,en-US,ko
    },
    "experimental_option":{
        "mobileEmulation":{ "deviceName": "iPhone 12 Pro" }
    },
    "arguments": [
        "--disable-gpu"
        #"--headless"
    ]
}

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
            'filename': f'{formatted_now}_twitch.log',
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
