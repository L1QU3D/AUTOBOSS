from lib2to3.pgen2 import driver

from main import username, password

# find the username and password fields and enter the values
username_field = driver.find_element_by_id("AuthModel_Username")
if username_field is not None:
    # Interact with the element
    username_field.send_keys(username)
password_field = driver.find_element_by_id("AuthModel_Password")
if password_field is None:
    password_field.send_keys(password)

# find the login button and click it
login_button = driver.find_element_by_id("login")
if login_button is not None:
    login_button.click()
