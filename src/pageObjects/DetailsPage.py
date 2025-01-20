from src.pageLocators.DetailsPageLocators import DetailsPageLocators
from src.pageObjects.BasePage import BasePage


class DetailsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_make_model_text(self):
        return super().get_element_text(DetailsPageLocators.VEHICLE_MODEL_MAKE_DESC)

    def get_vehicle_year(self):
        return super().get_element_text(DetailsPageLocators.VEHICLE_REG_YEAR)

    def get_vehicle_color(self):
        return super().get_element_text(DetailsPageLocators.VEHICLE_COLOR)

    def get_vehicle_model(self):
        return super().get_element_text(DetailsPageLocators.VEHICLE_MODEL)

    def get_vehicle_engine(self):
        return super().get_element_text(DetailsPageLocators.VEHICLE_ENGINE)

