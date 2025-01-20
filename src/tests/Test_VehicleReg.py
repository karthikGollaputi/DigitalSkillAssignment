import pytest
from selenium.common import TimeoutException
from conftest import reg_vehicles, convert_inp_reg_to_output_reg
from src.pageObjects.DetailsPage import DetailsPage
from src.pageObjects.HomePage import HomePage
from src.tests.BaseTest import BaseTest


class Test_VehicleReg(BaseTest):
    @pytest.mark.parametrize("reg_no", reg_vehicles())
    def test_vehicles_make_model_year(self, setup_teardown, output_data, reg_no):
        homepage = HomePage(self.driver)
        detailspage = DetailsPage(self.driver)
        homepage.enter_vat_reg_no(reg_no)
        try:
            homepage.click_value_button()
        except TimeoutException:
            print("The Car is not Valid Car")
            assert homepage.validcar_errormessage() == True



        car_details = [data for data in output_data if data["VARIANT_REG"] == convert_inp_reg_to_output_reg(reg_no)]
        if (car_details is None):

            AssertionError("No Car Exists in the Market")
        else:
            assert detailspage.get_make_model_text() in car_details["MODEL"]
            assert detailspage.get_vehicle_year() == car_details["YEAR"]
            assert detailspage.get_vehicle_color() in car_details["MODEL"]
            assert detailspage.get_vehicle_engine() in car_details["MODEL"]
