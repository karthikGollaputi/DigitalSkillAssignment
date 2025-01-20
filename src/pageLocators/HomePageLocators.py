from selenium.webdriver.common.by import By


class HomePageLocators:
    VR_NO_INPUT = (By.ID, "vrm-input")
    VALUE_BUTTON = (By.CSS_SELECTOR, "button[data-cy='valueButton']")
    ERROR_MESSAGE = (By.XPATH,"//li[@data-thc-toast-id='thc-toast-1']/div/div/div[3]/div")