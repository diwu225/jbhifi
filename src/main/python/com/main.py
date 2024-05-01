from com.login.login import jbhifi_signin
from com.logout.logout import jbhifi_signout
from com.utilities.credentials import username, password

def flow_control(browser):
    # Login to application
    print("Step 1 : Login ")
    jbhifi_signin(username, password, browser)
    # search for product
    print("Step 2 : Search Product  ")

    # Logout
    print("Step 3: Logout ")
    jbhifi_signout(browser)


if __name__ == '__main__':
    from com.utilities.initializebrowser import Initiate_FireFox
    browser = Initiate_FireFox.get_instance().driver

    flow_control(browser)