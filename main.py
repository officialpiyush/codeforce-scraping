import json
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from sys import exit

def main():
    if os.path.exists("./config.json"):
        with open("./config.json") as f:
            jd = json.load(f)
        try:
            handle = jd["handle"]
            email = jd["email"]
            password = jd["password"]
        except KeyError:
            print("The config.json file has not been filled properly.")
            exit()

    driver = webdriver.Chrome()
    driver.get("https://codeforces.com/register")
    driver.find_element_by_name("handle").send_keys(handle)
    driver.find_element_by_name("email").send_keys(email)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("passwordConfirmation").send_keys(password)
    driver.find_element_by_name("passwordConfirmation").send_keys(Keys.RETURN)
    driver.save_screenshot("registration.png")
    driver.close()

if __name__ == '__main__':
    main()