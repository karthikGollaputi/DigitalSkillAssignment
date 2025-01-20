from src.pageLocators.HomePageLocators import HomePageLocators
from src.pageObjects.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_vat_reg_no(self, reg_no):
        super().type_input(HomePageLocators.VR_NO_INPUT, reg_no)

    def click_value_button(self):
        super().click_element(HomePageLocators.VALUE_BUTTON)

    def validcar_errormessage(self):
        return super().is_element_present(HomePageLocators.ERROR_MESSAGE)

