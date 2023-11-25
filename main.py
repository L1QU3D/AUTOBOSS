import getpass
import os
import time

# import selenium

from selenium import webdriver

#  launch Logo.py and it has the display the welcome message
os.system("python3 Logo.py")

# Define your starting text and content
starting_text = "Enter the URL of the website to be automated: "
content = "http://github.com:"

# Use the print function to print the combined text and content



# ask the user to enter the URL of the website to be automated
url = input((starting_text + content).format(url=""))

# get the username and password from the user
username = input("Enter username: ")
password = input("Enter password: ")


def main():
    # open Chrome browser and launch
    driver = webdriver.Chrome()
    driver.get(url)
    os.system("python3 Element.py")

    # wait for 10 seconds and close the browser
    time.sleep(10)
    driver.close()


if __name__ == "__main__":
    main()
