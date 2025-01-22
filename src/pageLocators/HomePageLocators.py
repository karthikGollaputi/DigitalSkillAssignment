from selenium.webdriver.common.by import By


class HomePageLocators:
    VR_NO_INPUT = (By.ID, "vrm-input")
    VALUE_BUTTON = (By.CSS_SELECTOR, "button[data-cy='valueButton']")
    ERROR_MESSAGE = (By.XPATH,"//div[@id='app']//li/div/div/div[3]/div")
    ERROR_MESSAGE_TEXT = "We couldn’t find a vehicle with that registration. Enter a valid UK reg. Recent registrations take a few days to appear on our system."