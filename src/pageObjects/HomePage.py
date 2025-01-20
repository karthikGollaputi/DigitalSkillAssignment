from selenium.common import TimeoutException

from src.pageLocators.HomePageLocators import HomePageLocators
from src.pageObjects.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_vat_reg_no(self, reg_no):
        super().type_input(HomePageLocators.VR_NO_INPUT, reg_no)

    def click_value_button(self):
        try:
         super().click_element(HomePageLocators.VALUE_BUTTON)
        except TimeoutException:
            print("Hey Outside Catched Exception")
            if(super().is_element_present(HomePageLocators.ERROR_MESSAGE)):
                print("Hey Catched Exception")
                assert super().get_element_text(HomePageLocators.ERROR_MESSAGE) == "We couldn’t find a vehicle with that registration. Enter a valid UK reg. Recent registrations take a few days to appear on our system."


