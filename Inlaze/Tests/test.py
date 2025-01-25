import pytest
from Pages.homepage import HomePages
from Pages.signinpages import SignInPages
from Pages.signuppages import SignUpPages

from Interactions.interaction import InteractionElement
from Questions.questionElement import QuestionElement as qe
from Questions.questionData import QuestionData as qd

"""Clase para ejecutar las pruebas"""
class TestInlaze():
    
    def __init__(self,driver):
        self.driver=driver
       # yield driver
        
    
    def testLogin(self,email,password):
        #Prueba de login con usuario y contraseña correctos
        signin = SignInPages(self.driver)
        iElement = InteractionElement(self.driver)

        iElement.sendText(signin.elements("txtUserEmail"),email)
        iElement.sendText(signin.elements("txtUserPassword"),password)
        iElement.clickElement(signin.elements("btnSignIn"))
        self.validateLoginOk()
        

    def testRegistro(self, name, email, password):
        #Prueba de registro con datos correctos
        signup = SignUpPages(self.driver)
        signin = SignInPages(self.driver)
        iElement = InteractionElement(self.driver)
        qElement = qe(self.driver)
        
        iElement.clickElement(signin.elements("lnkSignUp"))
        iElement.sendText(signup.elements("txtFullName"), name)
        iElement.sendText(signup.elements("txtEmail"), email)
        #iElement.clickElement(signup.elements("txtPasswords"))
        iElement.sendText(signup.elements("txtPasswords"), password)
        iElement.sendText(signup.elements("txtConfirPasswords"), password)
        #Verificacion del boton este activo
        if qElement.isClickable(signup.elements("btnSignUp")):
            iElement.clickElement(signup.elements("btnSignUp"))
            
        
    def testResgistroPasswordIncorrecto(self, name, email, password):
        #Prueba de registro con datos correctos
        qData=qd(email,password,name)
        signup = SignUpPages(self.driver)
        iElement = InteractionElement(self.driver)
        qElement = qe(self.driver)

        #validacion de datos segun los requerimientos
        if qData.validateName & qData.validateEmail & qData.validatePassword:
            iElement.clickElement(signin. lnkSignUp)
            iElement.sendText(signup.elements("txtFullName"), name)
            iElement.sendText(signup.elements("txtEmail"), email)
            #iElement.clickElement(signup.elements("txtPasswords"))
            iElement.sendText(signup.elements("txtPasswords"), password)
            iElement.sendPassFaild(signup.elements("txtConfirPasswords"), password)
        #Verificacion del boton este activo
        if qElement.isPresentElement(signup.lblPassword):
            assert "Passwords do not match" in signup.lblPassword

    def validateLoginOk(self):
        home = HomePages(self.driver)
        assert "WELCOME" in home.elements("lblWelcome")

    def validateData(self, name,email,password):
        qData=qd(email,password,name)
        #validacion de datos segun los requerimientos
        if qData.validateName & qData.validateEmail & qData.validatePassword:
            return True
        else:
            return False


    def logut(self):
        #verificacion de logut 
        signin = SignInPages(self.driver)
        home = HomePages(self.driver)
        iElement = InteractionElement(self.driver)
        qElement = qe(self.driver)

        iElement.clickElement(home.elements("lblAvatar"))
        iElement.clickElement(home.elements("btnLogOut"))
        
        if qElement.isPresentElement(signin.elements("title")):
            assert "Logut correcto" 

