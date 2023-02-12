from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#args is a list of chrome options
driver_instance = None
def get_global_driver(start_url, args=None):
    global driver_instance
    if not driver_instance:
        driver_instance = GlobalDriver(start_url=start_url,  arguments=args)
    return driver_instance

class GlobalDriver:
    chrome_options = Options()
    def __init__(self, start_url, arguments=None):
        if arguments:
            for arg in arguments:
                self.chrome_options.add_argument(arg)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(start_url)