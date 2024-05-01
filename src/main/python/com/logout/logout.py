from selenium.webdriver.common.by import By

# from com.utilities.credentials import username, password
# from src.main.python.com.utilities.initializebrowser import Initiate_FireFox
# from com.login.login import jbhifi_signin

# browser = Initiate_FireFox.get_instance().driver
# browser = None

def jbhifi_signout(browser):
    print(" Inside jbhifi_signout ")
    print(id(browser))
    print(type(browser))
    flex_container = browser.find_element(By.CSS_SELECTOR, "._1iscg2f0")
    flex_container.click()
    logout_ribbon_button = browser.find_element(By.XPATH,
                                                "/html/body/div[5]/div[1]/div[1]/header/div[1]/div/div/div/div[4]/div[3]/button/svg")
    logout_ribbon_button.click()
    logout_button = browser.find_element(By.XPATH,
                                         "/html/body/div[5]/div[1]/div[1]/header/div[1]/div/div/div/div[4]/div[3]/div/div/button[5]")
    logout_button.click()


if __name__ == '__main__':
    print("Inside Logout main method ")
    jbhifi_signout(None)

#LEG-B : L : Local # E-Enclosed # G Global, B-Builtin