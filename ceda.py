from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains


options = Options()
options.binary_location = (
    "C:\\Users\\KARNAV\\AppData\\Local\\Firefox Developer Edition\\firefox.exe"
)

driver = webdriver.Firefox(options=options)
driver.implicitly_wait(0.5)
driver.maximize_window()


driver.get("https://dbie.rbi.org.in/DBIE/dbie.rbi?site=statistics")
print("Page title is: ")
print(driver.title)


driver.execute_script("document.getElementById('m1').style.visibility = 'visible';")
driver.implicitly_wait(0.5)
second_menu_button = driver.find_element(
    locate_with(By.LINK_TEXT, "Industrial Statistics")
)
second_menu_button.click()
driver.implicitly_wait(0.5)

driver.switch_to.frame("_ddajaxtabsiframe-petsdivcontainer")
test = driver.find_element(
    locate_with(By.LINK_TEXT, "Index Number of Industrial Production")
)
print(test)

driver.quit()
