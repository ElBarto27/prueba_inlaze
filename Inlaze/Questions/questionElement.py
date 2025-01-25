from selenium.webdriver.support import expected_conditions as ex
from selenium.webdriver.support.ui import WebDriverWait

class QuestionElement:
    def __init__(self, driver):
        self.driver = driver
    
    def isPresentElement(self,element):
        isPresent= WebDriverWait(self.driver,10).until(
            ex.presence_of_element_located(element)
        )
        return isPresent

    def isClickable(self,element):
        isclick = element.is_enabled()
        return isclick
