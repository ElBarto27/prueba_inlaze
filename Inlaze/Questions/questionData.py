class QuestionData:
    def __init__(self,email, password, name=""):
        self.name = name
        self.email = email
        self.password = password

    def validateName(self):

        try:
            # Verifica si hay dos palabras
            if len(self.name.split())<2:
                raise ValueError("El nombre debe contener mínimo 2 palabras (primer nombre y apellido).")
            return True
        except ValueError as e:
            # Si nombre no contiene mínimo 2 palabras,se lanza una excepción.
            raise ValueError(e)
    
    def validateEmail(self):
        try:
            # Verifica si hay al menos un símbolo especial
            if not any(c in "@." for c in self.email):
                raise ValueError("El email debe cumplir con el estándar de una dirección de correo electrónico")
            
            return True
        except ValueError as e:
            # Si la contraseña no cumple con algún criterio, se lanza una excepción
            raise ValueError(e)
            
    def validatePassword(self):
        try:
            # Verifica la longitud de la contraseña
            if len(self.password) < 8:
                raise ValueError("La contraseña no cumple con los criterios establecidos: debe tener al menos 8 caracteres.")
            
            # Verifica si hay al menos una letra mayúscula
            if not any(c.isupper() for c in self.password):
                raise ValueError("La contraseña no cumple con los criterios establecidos: debe contener al menos una letra mayúscula.")
            
            # Verifica si hay al menos una letra minúscula
            if not any(c.islower() for c in self.password):
                raise ValueError("La contraseña no cumple con los criterios establecidos: debe contener al menos una letra minúscula.")
            
            # Verifica si hay al menos un número
            if not any(c.isdigit() for c in self.password):
                raise ValueError("La contraseña no cumple con los criterios establecidos: debe contener al menos un número.")
            
            # Verifica si hay al menos un símbolo especial
            if not any(c in "@#$%" for c in self.password):
                raise ValueError("La contraseña no cumple con los criterios establecidos: debe contener al menos un símbolo especial (@, #, $, %).")
            
            # Si pasa todas las verificaciones, la contraseña es segura
            return True
        except ValueError as e:
            # Si la contraseña no cumple con algún criterio, se lanza una excepción
            raise ValueError(e)