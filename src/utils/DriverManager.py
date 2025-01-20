from selenium import webdriver


class DriverManager:
    DRIVER = None

    @classmethod
    def get_driver(cls, browser):
        if browser == "chrome":
            cls.DRIVER = webdriver.Chrome()
        elif browser == "edge":
            cls.DRIVER = webdriver.Edge()
        elif browser == "firefox":
            cls.DRIVER = webdriver.Firefox()
        else:
            raise ValueError("The Entered browser is not supported by the program")
        return cls.DRIVER