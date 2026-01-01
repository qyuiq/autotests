from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DemoAccPage:
    def __init__(self, driver):
        self.driver = driver
        self.xpaht_button_settings = "//a[contains(@href, 'settings') and contains(text(), 'Настройки')]"

    def click_demo_settings(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(('xpath', self.xpaht_button_settings))
        )
        button.click()
        from pages.settings_page import SettingsPage
        return SettingsPage(self.driver)