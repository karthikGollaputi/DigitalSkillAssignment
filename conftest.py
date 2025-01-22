import os
from pathlib import Path
import pytest
import re
from src.utils.DriverManager import DriverManager
from src.utils.FileUtils import FileUtils
from src.utils.TestData import TestData


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome"
    )


def get_project_path():
    current_file = Path(__file__).resolve()
    return str(current_file.parent)


def input_file():
    return get_project_path() + os.sep + "src" + os.sep + "resources" + os.sep + TestData.INPUT_FILE

@pytest.fixture()
def output_file():
    return get_project_path() + os.sep + "src" + os.sep + "resources" + os.sep + TestData.OUTPUT_FILE


def get_config_file():
    return get_project_path() + os.sep + TestData.CONFIG_FILE


@pytest.fixture()
def setup_teardown(request, browser_name):
    driver = DriverManager.get_driver(browser_name)
    driver.maximize_window()
    driver.get(TestData.BASE_URL)
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield driver
    driver.quit()


def reg_vehicles():
    reg_vehicles = []
    data = FileUtils.read_file(input_file(), "r")
    for lines in data:
        reg_veh = re.findall("[A-Z]{2}[0-9]{2}\s[A-Z]{3}", lines)
        reg_vehicles.extend(reg_veh)
    return reg_vehicles


@pytest.fixture()
def browser_name(request):
    return request.config.getoption('--browser')


@pytest.fixture()
def output_data(output_file):
    vehicle_details = []
    index = 1
    data = FileUtils.read_file(output_file, "r")
    for lines in data:
        if index == 1:
            index = index + 1
            continue
        else:
            vehicle_detail = lines.split(",")
            vehicle_details.append(
                {"VARIANT_REG": vehicle_detail[0],"MODEL": vehicle_detail[1],
                 "YEAR": vehicle_detail[2].split("\n")[0]})
        index = index + 1
    return vehicle_details


def convert_inp_reg_to_output_reg(reg_no):
    vr_no = None
    if " " in reg_no:
        vr_no = reg_no.replace(" ", "")

    return vr_no
