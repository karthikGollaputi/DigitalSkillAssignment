from selenium.webdriver.common.by import By


class DetailsPageLocators:
    VEHICLE_MODEL_MAKE_DESC = (By.CSS_SELECTOR, "h1[data-cy='vehicleMakeAndModel']")
    VEHICLE_REG_YEAR = (By.XPATH, "//ul[@data-cy='vehicleSpecifics']/li[1]")
    VEHICLE_COLOR = (By.XPATH, "//ul[@data-cy='vehicleSpecifics']/li[2]")
    VEHICLE_MODEL = (By.XPATH, "//ul[@data-cy='vehicleSpecifics']/li[3]")
    VEHICLE_ENGINE = (By.XPATH, "//ul[@data-cy='vehicleSpecifics']/li[4]")

