from time import *

def validador(self,usuario,edad):
    self.usuario = str(usuario)
    self.edad = edad 
    
    #mayor_longitud_usuarioa = usuario > 12 < 5 mejor con len()
    #mayor_lon_edad = edad >=18 < 99
    if not (5 <= len(usuario) <= 12):
        return "Usuarios de 5 - 12 caracteres solamente"
    
    try:     
        edad = int(edad)
        if not (18 <= edad <= 99):
            return f"edad fuera del rango {edad}"
        
        #if usuario  == mayor_longitud_usuarioa :
            #return ("Usuario de 5 - 12 caracteres solamente")
            # Solo try para la el rango de la edad y q sea solo de valorint
        
    except ValueError:
        return "Error: la edad deber ser un numero"
    
    time(2)
    return "Registro exitoso"
    
    
          
    
    
    
    
