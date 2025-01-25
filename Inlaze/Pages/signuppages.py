import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

"""Clase para definir los elementos web de la vista Sign Up y su localizador"""
class SignUpPages:
    
    """Constructor de la clase"""
    def __init__(self, dr):
        self.driver = dr
        
    def elements(self,name):
        time.sleep(3)
        self.element = {
            "txtFullName": self.driver.find_element(By.ID, "full-name"),
            "txtEmail": self.driver.find_element(By.ID, "email"),
            "txtPasswords":self.driver.find_element(
                By.XPATH, "//input[@id='password']"),
            "txtConfirPasswords":self.driver.find_element(
                By.XPATH, "//input[@id='confirm-password']"),
            "btnViewPasswords": self.driver.find_element(
                By.XPATH, "//i[contains(@class,'fa-eye')]"),
            "btnSignUp": self.driver.find_element(
                By.XPATH, "//button[contains(text(),'Sign up')]"),
            #"lblPassword": WebDriverWait(self.driver, 10).until(
             #   self.driver.find_element(By.XPATH, "//*[contains(text(),'Passwords do not match')]")),
            "lnkSignIn": self.driver.find_element(
                By.XPATH, "//a[contains(text(),'Sign in')]")
        }
        if name not in self.element:
            raise ValueError(f"Elemento '{name}' no se encuentra definido.")

        return self.element[name]
    