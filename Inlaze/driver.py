import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv


class Driver:
    
    load_dotenv()
    def __init__(self):
        pass
        
    def open(self):
        self.url=os.getenv("URL")
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        return self.driver
    
    def close(self):
        self.driver.quit()
    