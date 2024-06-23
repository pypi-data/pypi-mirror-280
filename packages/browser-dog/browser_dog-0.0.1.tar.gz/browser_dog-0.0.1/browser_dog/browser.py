import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import os
from colorama import Fore, Style

class BrowserDog:
    def __init__(self, cookies_json: str, base_url: str, headless=False):
        """
        Initializes the Chrome Driver.
        """
        try:
            print(Fore.BLACK + "=" * 30 + " Initializing Driver " + "=" * 30 + Style.RESET_ALL)
            # use local selenium driver
            self.options = Options()
            # headless mode
            if headless:
                self.options.add_argument("--headless")
            self.driver = webdriver.Chrome(options=self.options)

            # use docker selenium/standalone-chrome
            # selenium_grid_url = 'http://localhost:4444/wd/hub'
            # option = Options()
            # option.set_capability("browserName", "chrome")
            # option.set_capability("platformName", "Linux")
            # print('Initialize selenium')
            # self.driver = webdriver.Remote(command_executor=selenium_grid_url, options=option)

            self.driver.maximize_window()
            print(Fore.GREEN + "Opening URL Page: " + base_url + Style.RESET_ALL)
            self.driver.get(base_url)
            self.medium_wait()

            if not os.path.exists(cookies_json):
                print(Fore.RED + "No cookies file found, please login first, default: cookies.json " + Style.RESET_ALL)
            else:
                with open(cookies_json, 'r') as file:
                    cookies = json.loads(file.read())

                for cookie in cookies:
                    cookie['sameSite'] = "None"
                    self.driver.add_cookie(cookie)

                print(Fore.GREEN + "Refreshing the page to apply cookies" + Style.RESET_ALL)
                self.driver.refresh()
                self.medium_wait()
                print(Fore.GREEN + "Successfully login the website, please start browsering..." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f'Error: {e}' + Style.RESET_ALL)

    def get_driver(self):
        return self.driver

    def scroll_to_bottom(self):
        """
        Scrolls to the bottom of the page.
        """
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_top(self):
        """
        Scrolls to the top of the page.
        """
        self.driver.execute_script("window.scrollTo(0, 0);")

    def scroll_to_middle(self):
        """
        Scrolls to the middle of the page.
        """
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")

    def scroll_to_random(self):
        """
        Scrolls to a random position of the page.
        """
        self.driver.execute_script("window.scrollTo(0, Math.floor(Math.random() * document.body.scrollHeight));")

    def short_wait(self):
        """
        Sleeps for a random amount of time between 1 and 3 seconds.
        """
        time.sleep(random.randint(1, 3))

    def medium_wait(self):
        """
        Sleeps for a random amount of time between 3 and 5 seconds.
        """
        time.sleep(random.randint(3, 5))

    def long_wait(self):
        """
        Sleeps for a random amount of time between 5 and 10 seconds.
        """
        time.sleep(random.randint(5, 10))


