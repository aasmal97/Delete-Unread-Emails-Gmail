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
#to use this, add a cred.py file to project directorywith variable password 
from cred import password
def signIn():
    #user is given 40 sec to manually type in username and click next
    time.sleep(40)
    # to use this script for organization emails (i.e cornell.edu, job.com, etc)
    # comment the bottom 4 lines out and manually input both username and password
    # passWordBox = driver.find_element_by_xpath(
    #     '//*[@id ="password"]/div[1]/div / div[1]/input')
    # passWordBox.send_keys(password)
    # nextBtn =  driver.find_element_by_xpath('//*[@id ="passwordNext"]')
    # nextBtn.click()

def emailPageActions():
        #click on check box
        try :
            #depending on computer/internet speed, increase or decrease 
            # this time variableto avoid errors
            time.sleep(6)
            dropdownbtn = driver.find_element_by_xpath("//*[@aria-label='Select']/div/div[@aria-hidden='true']")
            dropdownbtn.click()
        except ElementNotSelectableException: 
            dropdownbtn = driver.find_elements_by_xpath("//*[@aria-label='Select']/div/div[@aria-hidden='true']")[1]
            dropdownbtn.click()
        except ElementNotInteractableException:
            dropdownbtn = driver.find_elements_by_xpath("//*[@aria-label='Select']/div/div[@aria-hidden='true']")[1]
            dropdownbtn.click()

        #choose unread option
        try: 
            unreadOption = driver.find_element_by_xpath("//*[@selector='unread']")
            unreadOption.click()
        except ElementNotSelectableException: 
            unreadOption = driver.find_elements_by_xpath("//*[@selector='unread']")[1]
            unreadOption.click()
        except ElementNotInteractableException:
            unreadOption = driver.find_elements_by_xpath("//*[@selector='unread']")[1]
            unreadOption.click()
        #choose trash can to remove all unread emails
        try:
            trashBtn = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.XPATH, "//*[@aria-label='Delete']"))
            )
            try:
                trashBtn.click()
            except StaleElementReferenceException:
                trashBtn = WebDriverWait(driver, 2).until(
                     EC.presence_of_element_located((By.XPATH, "//*[@aria-label='Delete']"))
                )
                trashBtn.click()
            except ElementNotSelectableException:
                trashBtn = driver.find_elements_by_xpath("//*[@aria-label='Delete']")[1]
                trashBtn.click()
            except ElementNotInteractableException:
                trashBtn = driver.find_elements_by_xpath("//*[@aria-label='Delete']")[1]
                trashBtn.click()
        except:
            print("no items to delete here")

#move on to next page in inbox
#declaring this earlier causes stale and interactivable elements to occur
def nextPage(buttonType, btnPath):
    try:
        buttonType = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, btnPath))
        )
        buttonType.click()
    except StaleElementReferenceException:
        try: 
            buttonType = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.XPATH, btnPath))
                )
            buttonType.click()
        except ElementNotInteractableException:
            buttonType = driver.find_elements_by_xpath(btnPath)[1]
            buttonType.click()
    except ElementNotSelectableException:
        buttonType = driver.find_elements_by_xpath(btnPath)[1]
        buttonType.click()
    except ElementNotInteractableException:
        buttonType = driver.find_elements_by_xpath(btnPath)[1]
        buttonType.click()

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

#this allows us to naviagte from google to gmail login/or gmail inbox
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
while not seeOlderMess.get_attribute("aria-disabled"):
    emailPageActions()
    #avoid stale element error (meaning element position has changed since last assigned)
    seeOlderMess = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH, "//*[@aria-label='Older']"))
    )
    nextPage(seeOlderMess,"//*[@aria-label='Older']")
    #avoid stale element error (meaning element position has changed since last assigned)
    try:
        seeOlderMess = driver.find_elements_by_xpath("//*[@aria-label='Older']")[1]
    except IndexError:
        seeOlderMess = driver.find_element_by_xpath("//*[@aria-label='Older']")

time.sleep(1)
#loop back to start
try:
    seeRecentMess = driver.find_elements_by_xpath("//*[@aria-label='Newer']")[1]
except IndexError: 
    seeRecentMess = driver.find_element_by_xpath("//*[@aria-label='Newer']")
while not seeRecentMess.get_attribute("aria-disabled"):
    emailPageActions()
    #avoid stale element error (meaning element position has changed since last assigned)
    seeRecentMess = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH, "//*[@aria-label='Newer']"))
    )
    nextPage(seeRecentMess, "//*[@aria-label='Newer']")
    #avoid stale element error (meaning element position has changed since last assigned)
    try:
        seeRecentMess = driver.find_elements_by_xpath("//*[@aria-label='Newer']")[1]
    except IndexError: 
        seeRecentMess = driver.find_element_by_xpath("//*[@aria-label='Newer']")
