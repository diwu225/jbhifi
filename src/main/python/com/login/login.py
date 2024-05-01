from com.logout.logout import jbhifi_signout


def jbhifi_signin(login_id, login_secret, browser=None):
    print("calling jbhifi.. login method ...")
    import time
    from selenium.webdriver.common.by import By
    browser.get("https://www.jbhifi.com.au/")  # calling jbhifi url
    login_icon = browser.find_element(By.XPATH,
                                        "/html/body/div[5]/div[1]/div[1]/header/div[1]/div/div/div/div[4]/div["
                                        "3]/button")
    login_icon.click()  # click on login button
    time.sleep(10)
    #browser.implicitly_wait(60)
    email_add = browser.find_element(By.ID, 'email')
    email_add.click()
    email_add.send_keys(login_id)
    pwd = browser.find_element(By.ID, "password")
    pwd.click()
    pwd.send_keys(login_secret)
    confirm_button = browser.find_element(By.XPATH, '//*[@id="continueProxy"]')
    confirm_button.click()
    browser.implicitly_wait(10)

    print(id(browser))
    print(type(browser))
    # logout
    jbhifi_signout(browser)



if __name__ == '__main__':
    from com.utilities.credentials import username, password
    from com.utilities.initializebrowser import Initiate_FireFox
    browser = Initiate_FireFox.get_instance().driver

    # jbhifi_signin(login_id=username, login_secret=password, browser=browser)
    jbhifi_signin(login_id=username, login_secret=password)
