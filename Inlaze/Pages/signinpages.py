from selenium.webdriver.common.by import By
import time
"""Clase para definir los elementos web de la vista login y su localizador"""
class SignInPages:
    
    """Constructor de la clase"""
    def __init__(self, driver):
        self.driver = driver
    
    def elements(self, name):
        time.sleep(3)
        """Elementos web de la vista de login"""
        self.element={
            "title":self.driver.find_element(By.XPATH,"//h1[contains(text(),'Sign in')]"),
            "txtUserEmail" : self.driver.find_element(By.ID,"email"),
            "txtUserPassword" : self.driver.find_element(By.ID,"password"),
            "btnViewPassword" : self.driver.find_element(By.XPATH,"//i[contains(@class,'fa-eye')]"),
            "btnSignIn" : self.driver.find_element(By.XPATH,"//button[contains(text(),'Sign in')]"),
            "lnkSignUp":self.driver.find_element(By.XPATH,"//a[contains(text(),'Sign up')]")
        }
        if name not in self.element:
            raise ValueError(f"Elemento '{name}' no se encuentra definido.")

        return self.element[name]