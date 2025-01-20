import pytest
import re
import os.path
from src.utils.DriverManager import DriverManager
from src.utils.FileUtils import FileUtils


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome"
    )


@pytest.fixture()
def setup_teardown(request, browser_name):
    driver = DriverManager.get_driver(browser_name)
    driver.maximize_window()
    driver.get("http://motorway.com/")
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield driver
    driver.quit()


def input_file():
    return "C:\\Users\\karthik\\Downloads\\car_input V4.txt"


@pytest.fixture()
def output_file():
    return "C:\\Users\\karthik\\Downloads\\car_output V4.txt"


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
                {"VARIANT_REG": vehicle_detail[0], "MAKE": vehicle_detail[1], "MODEL": vehicle_detail[2],
                 "YEAR": vehicle_detail[3].split("\n")[0]});
        index = index + 1
    return vehicle_details


def convert_inp_reg_to_output_reg(regno):
    vr_no = None
    if " " in regno:
        vr_no = regno.replace(" ", "")

    return vr_no
