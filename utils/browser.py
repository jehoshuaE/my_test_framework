from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def get_driver():
    try:
        service=Service(r'C:\webdriver\chromedriver.exe')
        driver = webdriver.Chrome(service=service)
        print("WebDriver initialized successfully.")
        return driver
    except Exception as e:
        print(f"Error initializing WebDriver: {e}")
        return None