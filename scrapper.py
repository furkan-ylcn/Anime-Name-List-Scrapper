from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = r'./ChromeDriver/chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

link = 'https://www.turkanime.co/'
driver.get(link)

driver.find_element_by_xpath("//a[@href='//www.turkanime.co/anime-izle']").click()

main_window = driver.current_window_handle
popup_window = None

for handle in driver.window_handles:
    if handle != main_window:
        popup_window = handle
        break

if popup_window:
    driver.switch_to.window(popup_window)
    driver.close()
    driver.switch_to.window(main_window)

time.sleep(3)

while True:
    try:
        driver.find_element_by_xpath("//button[@data-loading-text=\"Sonraki <i class='fa fa-spinner fa-spin fa-fw'></i>\"]").click()
        time.sleep(2)
        elements = driver.find_elements(By.CLASS_NAME, 'panel-ust-ic')
        for element in elements:
            print(element.text)
    except NoSuchElementException:
        break

driver.quit()
