import time

import pytest
from selenium.common import TimeoutException
from conftest import reg_vehicles, convert_inp_reg_to_output_reg
from src.pageLocators.HomePageLocators import HomePageLocators
from src.pageObjects.DetailsPage import DetailsPage
from src.pageObjects.HomePage import HomePage
from src.tests.BaseTest import BaseTest


class Test_VehicleReg(BaseTest):
    @pytest.mark.parametrize("reg_no", reg_vehicles())
    def test_vehicles_make_model_year(self, setup_teardown, output_data, reg_no):
        homepage = HomePage(self.driver)
        detailspage = DetailsPage(self.driver)
        homepage.enter_vat_reg_no(reg_no)
        homepage.click_value_button()
        try:
            if homepage.is_error_message_present():
                assert homepage.validate_car_error_message_text() == HomePageLocators.ERROR_MESSAGE_TEXT
                raise ValueError("The Car is not Present in the UK and Details Not Found in Website")
        except TimeoutException as t:
            car_details = [data for data in output_data if data["VARIANT_REG"] == reg_no]
            if not car_details:
                raise ValueError("The car doesn't Exist in the OutPut File")
            else:
                assert detailspage.get_make_model_text() in car_details[0]["MODEL"]
                assert detailspage.get_vehicle_year() == car_details[0]["YEAR"]






