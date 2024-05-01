from selenium import webdriver


class Initiate_FireFox:
    _instance = None  # it will be updated during first call

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            print(cls._instance)
            cls._instance = super(Initiate_FireFox, cls).__new__(cls, *args, **kwargs)
            print(cls._instance)
            # initiliase the web driver instance
            cls._instance.driver = webdriver.Firefox()
            # browser initialization:
            # cls._instance.driver

        return cls._instance

    @classmethod
    def get_instance(cls):
        return cls()

