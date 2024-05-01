#def compare_products_and_store_result():
# getlogin()
    # iphone13,iphone14
    # iphone13, galaxy14
    #for line in lines:
        # product search()
        # store result
    # logout

compare_iphones = ["iphone13", "iphone14"]
compare_android = ["galaxy24", "galaxy23"]


def compare_products(product_list):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    import time
    from com.utilities.credentials import username, password
    from src.main.python.com.login.login import jbhifi_signin
    from src.main.python.com.utilities.initializebrowser import Initiate_FireFox

    # Initialize the WebDriver
    browser = Initiate_FireFox.get_instance().driver

    jbhifi_signin(username, password, browser)

    if not isinstance(product_list, list):
        raise TypeError("product list should be a list of product names")

    if len(product_list) != 2:
        raise ValueError("No of items are not correctly defined")

    else:
        # Find the search input box and enter the product name (e.g., "iPhone 13")
        browser.find_element(By.XPATH, "/html/body/div[5]/div[1]/div[1]/header/div[1]/div/div/div/div[2]/div/input").click()
        search_button = browser.find_element(By.XPATH, "/html/body/div[8]/div/div[1]/div/div/form/input")
        search_button.click()
        # search_button.send_keys("iphone13")
        search_button.send_keys(compare_iphones[0])
        search_button.send_keys(Keys.RETURN)

        # Wait for the search results to load
        time.sleep(5)

        #browser.execute_script("window.scrollBy(0, 1000);")

        # Click on the first search result to view the product details
        #product1_link = browser.find_element(By.XPATH, "/html/body/div[8]/div/div[1]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div/div/div/a/div/div[1]")
        #product1_link.click()

        # Click on the "Add to Compare" button for the first product
        label_element = browser.find_element(By.CLASS_NAME, "Checkbox_label__pomeu20")
        compare_button_1 = label_element.find_element(By.XPATH, '//*[@id="jbcheckbox-product-compare"]')
        if not compare_button_1.is_selected():
            compare_button_1.click()

        #search second product
        #browser.find_element(By.)
        browser.find_element(By.XPATH, "/html/body/div[5]/div[1]/div[1]/header/div[1]/div/div/div/div[2]/div/input").click()
        search_button = browser.find_element(By.XPATH, "/html/body/div[8]/div/div[1]/div/div/form/input")
        search_button.click()
        # search_button.send_keys("iphone14")
        search_button.send_keys(compare_iphones[1])
        search_button.send_keys(Keys.RETURN)

        # Wait for the search results to load
        time.sleep(3)

        # Click on the first search result to view the product details
        product2_link = browser.find_element(By.XPATH,
                                            "/html/body/div[8]/div/div[1]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div/div/div/a/div/div[1]")
        product2_link.click()

        # Wait for the product page to load
        time.sleep(3)

        browser.execute_script("window.scrollTo(0, 500);")

        # Click on the "Add to Compare" button for the first product
        compare_button_2 = browser.find_element(By.XPATH, "//button[@class='compare-button']")
        compare_button_2.click()

        # Click on the "Continue Shopping" button to go back to the search results
        compare_products = browser.find_element(By.XPATH, "//button[text()='Continue Shopping']")
        compare_products.click()

        # Close the browser
        browser.quit()


compare_products(compare_iphones)
