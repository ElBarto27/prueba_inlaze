"""clase para interactuar con elementos web"""
class InteractionElement():
    def __init__(self, driver):
        self.driver = driver
    
    def sendText(self,elements, text):
        if not isinstance(elements, list):
            elements = [elements]  # Convertimos un solo elemento a una lista
            
        for element in elements:
            element.send_keys(text)

    def sendPassFaild(self,elements, text):
        if not isinstance(elements, list):
            elements = [elements]  # Convertimos un solo elemento a una lista

        for element in elements:
            text=text[::-1]
            element.send_keys(text)

    def clickElement(self,element):
        element.click()