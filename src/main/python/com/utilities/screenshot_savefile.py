def screenshot_savefile():
    from com.utilities.initializebrowser import Initiate_FireFox
    browser = Initiate_FireFox.get_instance().driver
    file_format = ""
    screenshot_taken = browser.get_full_page_screenshot_as_png()
    if file_format == 'png':
        file_path = 'search_result.png'
        with open(file_path, 'wb') as file:
            file.write(screenshot_taken)
    else:
        browser.get_full_page_screenshot_as_file("search_result.pdf")
