from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by_element):
        return self.driver.find_element(by_element)

    def click_element(self, webelement):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(webelement)).click()

    def type_input(self, web_element, text):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(web_element)).send_keys(text)

    def get_element_text(self, web_element):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(web_element))
        return element.text

    def is_element_present(self, web_element):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(web_element)).is_displayed()
