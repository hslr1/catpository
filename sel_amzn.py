import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
action = ActionChains(driver)

# code start

driver.get('https://amazon.com')
driver.maximize_window()


# menu = driver.find_element("id", "nav-hamburger-menu")
# hidden_submenu = driver.find_element_by_css_selector(".nav # submenu1")
  
# ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()

# for link in prime_video_links:
#     link.get_attribute("href")
#     print(link)

# prime_video_links[7].click()



search_input = driver.find_element("id", "twotabsearchtextbox")

search_input.click()

search_input.send_keys("iphone 14")
search_input.send_keys(Keys.ENTER)

first_found_element_on_amzn = driver.find_element("xpath", '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span')

first_found_element_on_amzn.click()

second_found_element_on_amzn = driver.find_element("xpath", '//*[@id="a-autoid-20-announce"]/div/div[1]/p')
second_found_element_on_amzn.click()

add_to_cart_btn = driver.find_element("id", "add-to-cart-button")
add_to_cart_btn.click()

# protection_question = driver.find_element("id", "attachSiNoCoverage-announce")
# protection_question.click()

cart_link = driver.find_element("id", "nav-cart-count-container")
cart_link.click()

time.sleep(3)

driver.back()

# HAM menu

ham_menu = driver.find_element("id", "nav-hamburger-menu")

ham_menu.click()

time.sleep(3)

what = driver.find_element("xpath", "//a[@data-menu-id='2']")



what.click()

time.sleep(3)

prime_video_link = driver.find_element("xpath", "/html/body/div[3]/div[2]/div/ul[2]/li[3]/a")

prime_video_link.click()


signin_link = driver.find_element("id", "nav-link-accountList")
signin_link.click()

create_acc_btn = driver.find_element("id", "createAccountSubmit")
create_acc_btn.click()

customer_name = driver.find_element("id", "ap_customer_name")
customer_name.send_keys("Tom Cruise") 

customer_phone_or_email = driver.find_element("id", "ap_email")
customer_phone_or_email.send_keys("hello@tomcruise.com")

customer_password = driver.find_element("id", "ap_password")
customer_password.send_keys("CUSTOMER_password_123!")

customer_password_check = driver.find_element("id", "ap_password_check")
customer_password_check.send_keys("CUSTOMER_password_123!")








