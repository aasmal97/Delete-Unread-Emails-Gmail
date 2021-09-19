import os
import time
from random import randrange
from random import seed
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException, ElementNotSelectableException, StaleElementReferenceException
#to use this, add a cred.py file to project directory with variable password 
from cred import password
def signIn():
    #user is given 40 sec to manually type in username and click next
    time.sleep(40)
    # to use this script for organization emails (i.e cornell.edu, job.com, etc)
    # comment the bottom 4 lines out and manually input both username and password
    passWordBox = driver.find_element_by_xpath(
        '//*[@id ="password"]/div[1]/div / div[1]/input')
    passWordBox.send_keys(password)
    nextBtn =  driver.find_element_by_xpath('//*[@id ="passwordNext"]')
    nextBtn.click()
#this function handles all common exceptions
def handle_exceptions(element, elementPath):
        try :
            element = driver.find_element_by_xpath(elementPath)
            element.click()
        except ElementNotSelectableException: 
            element = driver.find_elements_by_xpath(elementPath)[1]
            element.click()
        except ElementNotInteractableException:
            try:
                element = driver.find_elements_by_xpath(elementPath)[1]
                element.click()
            except IndexError:
                #means were inside a personal account, so if the first instance of trash can
                #is not interactable, there are no items to delete
                print("No items To Delete")
            except ElementNotInteractableException:
                #means were inside a org account, so if the second instance of trash can is
                #not interactable, there are no items to delete
                print("No items To Delete")
        except StaleElementReferenceException:
            try:
                element = WebDriverWait(driver, 2).until(
                    EC.presence_of_element_located((By.XPATH, elementPath))
                )
            except ElementNotInteractableException:
                element = driver.find_elements_by_xpath(elementPath)[1]
                element.click()

def emailPageActions():
        #depending on computer/internet speed, increase or decrease 
        # this time variable to avoid errors
        time.sleep(5)
        #click on check box
        dropdownBtn = True
        handle_exceptions(dropdownBtn, "//*[@aria-label='Select']/div/div[@aria-hidden='true']")

        #choose unread option
        unreadOption = True
        handle_exceptions(unreadOption, "//*[@selector='unread']")

        #choose trash can to remove all unread emails
        trashBtn = True
        time.sleep(1)
        handle_exceptions(trashBtn, "//*[@aria-label='Delete']")

#move on to next page in inbox
def nextPage(buttonType, btnPath):
    time.sleep(0.5)
    handle_exceptions(buttonType, btnPath)

def loop_direction(btn_Direction, btn_Path):
    while not btn_Direction.get_attribute("aria-disabled"):
        emailPageActions()
        nextPage(btn_Direction, btn_Path)
        #avoid stale element error (meaning element position has changed since last assigned)
        try:
            btn_Direction = driver.find_elements_by_xpath(btn_Path)[1]
        except IndexError: 
            btn_Direction = driver.find_element_by_xpath(btn_Path)

#setup to avoid bot detection and grab driver (the automated tool)
os.environ['PATH'] +=  os.pathsep + r"C:/chromeDriver"
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=options)
driver.maximize_window()
stealth(driver,
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True,
    )
#for randomizing numbers
seed(1)

#naviagte from google to gmail login/or gmail inbox
driver.get("https://www.google.com/")
gmailBtn = driver.find_element_by_link_text("Gmail")
gmailBtn.click()

#Click on Sign in if it exists
time.sleep(randrange(1,3))
signInBtn = driver.find_element_by_link_text("Sign in")

if(signInBtn):
    signInBtn.click()
    signIn()

#loop to the end of email inbox
time.sleep(2)
seeOlderMess = driver.find_element_by_xpath("//*[@aria-label='Older']")
loop_direction(seeOlderMess, "//*[@aria-label='Older']")
time.sleep(1)

#loop back to start
try:
    seeRecentMess = driver.find_elements_by_xpath("//*[@aria-label='Newer']")[1]
except IndexError: 
    seeRecentMess = driver.find_element_by_xpath("//*[@aria-label='Newer']")
loop_direction(seeRecentMess, "//*[@aria-label='Newer']")
