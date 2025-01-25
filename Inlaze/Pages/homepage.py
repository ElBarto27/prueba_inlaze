from selenium.webdriver.common.by import By
import time
class HomePages:

    def __init__(self, driver):
        self.driver = driver

    def elements(self, name):
        time.sleep(3)
        """Elementos de la pagina principal"""
        self.element={
            "lblWelcome": self.driver.find_element(
                By.XPATH,"//*[contains(text(),' Welcome to Lorem ')]"),
            "lblAvatar" : self.driver.find_element(
                By.XPATH,"//*[contains(@class,'avatar')]"),
            "lnkLogout" : self.driver.find_element(
                By.XPATH,"//a[contains(text(),' Logout')]")
        }
        if name not in self.element:
            raise ValueError(f"Elemento {name} no se encuentra definido.")

        return self.element[name]
    