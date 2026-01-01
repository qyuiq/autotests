from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SettingsPage:
    def __init__(self, driver):
        self.driver = driver
        self.xpaht_button_delete = "//button[contains(@id, 'deleteAvatar')]"
        self.xpaht_sandbox_popup = "//div[contains(@class, 'sandbox__popup')]"
        self.xpaht_sandbox_popup_text = "//span[contains(@class, 'sandbox__popup-text')]"

    def click_delete_avatar_button(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(('xpath', self.xpaht_button_delete))
        )
        button.click()

    def wait_for_sandbox_popup(self, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(
            EC.visibility_of_element_located(("xpath", self.xpaht_sandbox_popup))
        )


    def text_in_sandbox_popup(self):
        message = self.driver.find_element("xpath", self.xpaht_sandbox_popup_text).text
        return message