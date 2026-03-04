def validador(self,usuario,edad):
    self.usuario = str(usuario)
    self.edad = edad 
    
    mayor_longitud_usuarioa = usuario > 12 < 5
    
    edad = int(edad)
    mayor_lon_edad = edad >=18 < 99
    
    try:     
        if edad == mayor_lon_edad:
            return f"edad fuera del rango {mayor_lon_edad}"
        
        if usuario  == mayor_longitud_usuarioa :
            return ("Usuario de 5 - 12 caracteres solamente")
        
    except edad and usuario is True:
        return edad and usuario
    
          
    
    
    
    
