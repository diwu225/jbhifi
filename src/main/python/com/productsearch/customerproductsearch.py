def customer_product_search(fileformat):
    import time
    from selenium.webdriver import Keys
    from selenium.webdriver.common.by import By
    from com.utilities.screenshot_savefile import screenshot_savefile
    from src.main.python.com.utilities.initializebrowser import Initiate_FireFox

    browser = Initiate_FireFox.get_instance().driver
    browser.find_element(By.XPATH, "/html/body/div[5]/div[1]/div[1]/header/div[1]/div/div/div/div[2]/div/input").click()
    search_button = browser.find_element(By.XPATH, "/html/body/div[8]/div/div[1]/div/div/form/input")
    search_button.click()
    search_button.send_keys("TP Link Router")
    search_button.send_keys(Keys.RETURN)
    time.sleep(10)
    #browser.find_element(By.XPATH, "/html/body/div[7]/div/div[1]/div/div[1]/form/button[2]").click()
    screenshot_savefile()
    browser.get_full_page_screenshot_as_png()

    if fileformat == 'png':
        file_path = 'screenshot2.png'
        with open(file_path, 'wb') as file:
            file.write(browser.get_screenshot_as_png())
    else:
        browser.get_full_page_screenshot_as_file("search_result.pdf")

    browser.quit()

customer_product_search(fileformat="jpg")

