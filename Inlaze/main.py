from driver import Driver
from Tests.test import TestInlaze
class runner:
    
    
    dr = Driver()
    driver = dr.open()
    driver.maximize_window()

    test=TestInlaze(driver)
    #Registro exitoso
    test.testRegistro(name="brandon gonzalez",email="test@test.com",password="Test123!")
    #Registro sin el formulario completo
    test.testRegistro(name="brandon gonzalez",email="test2@test.com",password="")
    test.testRegistro(name="brandon gonzalez",email=" ",password="Test123!")
    test.testRegistro(name="",email="test3@test.com",password="Test123!")
    test.testRegistro(name="Brandon",email="test4@test.com",password="Test123!")
    #Registro password no coinciden
    test.testResgistroPasswordIncorrecto(name="brandon gonzalez",email="test@test.com",password="Test123!")

    #login correcto
    test.testLogin(email="test@test.com",password="Test123!")
    #validacion de login
    test.validateLoginOk()
    #cierre de sesion
    test.logut()