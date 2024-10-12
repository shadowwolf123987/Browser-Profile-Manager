#Imports
import os
import shutil
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chromeMainPath = r"C:\\Users\\User\\source\\repos\\Profile Downloader\\Profiles\\Chrome\\main"
chromeTempPath = r"C:\\Users\\User\\source\\repos\\Profile Downloader\\Profiles\\Chrome\\template"
chromeSavedPath = r"C:\\Users\\User\\source\\repos\\Profile Downloader\\Profiles\\Chrome\\saved\\"

def browserSelect():
    browser = input("\nChoose from our current available browsers: Google Chrome\n\n")
    browser = browser.lower()
    
    if "google" in browser or "chrome" in browser:
        launch("google")
        
def launch(browser):
    if browser == "google":
        options = Options()
        options.add_argument(f"--user-data-dir={chromeMainPath}")
        options.add_argument("--start-maximized")
        options.headless = False
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        driver = webdriver.Chrome(options=options)
        
        googleActions(driver)
    
def googleActions(driver):
    time.sleep(1)
    print("\033[H\033[J", end="")
    action = input("Enter an action: save, load, delete, clear, list, exit\n\n")
    print("\n")
    
    param = action.split(" ",1)
        
    if len(param) > 1:
        action = param[0]
        param = str(param[1])
    
    if action == "save":
        save("google", driver, param)
    elif action == "load":
        load("google", driver, param)
    elif action == "delete":
        delete("google", driver, param)
    elif action == "list":
        listSaved("google", driver)
    elif action == "clear":
        clear("google", driver)
    elif action == "exit":
        driver.quit()
        return
    
    else:
        print("ERROR: Invalid Command Entered")
    
    googleActions(driver)
    
def save(browser, driver, fileName=""):
    if browser == "google":
        driver.quit()
        
        if fileName == "":
            fileName = input("Enter the file name to save the profile as here\n\n")
        
        try:
            shutil.copytree(chromeMainPath,chromeSavedPath+fileName)
        except FileExistsError:
            print(f"ERROR: {fileName} Already Exists")
            launch("google")
        else:
            print(fileName + " Profile Saved")
            launch("google")
        
def load(browser, driver, fileName=""):
    if browser == "google":
        
        if fileName == "":
            fileName = input("Enter the saved profile name to load\n\n")
        
        if os.path.isdir(chromeSavedPath+fileName):
            driver.quit()
            
            shutil.rmtree(chromeMainPath)
                
            shutil.copytree(chromeSavedPath+fileName,chromeMainPath)
            print(fileName + " Profile Loaded")
            launch("google")
            
        else:
            print(f"ERROR: Profile {fileName} Doesn't Exist")
            googleActions(driver)

def delete(browser, driver, fileName=""):
    if browser == "google":
        
        if fileName == "":
            fileName = input("Enter the saved profile name to load\n\n")
        
        if os.path.isdir(chromeSavedPath+fileName):
            shutil.rmtree(chromeSavedPath+fileName)
            
            print(fileName + " Profile Deleted")
            
        else:
            print(f"ERROR: Profile {fileName} Doesn't Exist")
        
        googleActions(driver)

def listSaved(browser, driver):
    if browser == "google":
        print(os.listdir(chromeSavedPath))

def clear(browser, driver):
    if browser == "google":
        driver.quit()
        shutil.rmtree(chromeMainPath)
        
        shutil.copytree(chromeTempPath,chromeMainPath)
        
        print("Main Profile Cleared")
        launch("google")

browserSelect()