from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://werent.me/"
        self.xpaht_button_demo_acc = "//div[contains(@class, 'button-2')]"

    def open_web(self):
        self.driver.get(self.base_url)
        return self

    def click_demo_acc_button(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(('xpath', self.xpaht_button_demo_acc))
        )
        button.click()
        from pages.demo_acc_page import DemoAccPage
        return DemoAccPage(self.driver)