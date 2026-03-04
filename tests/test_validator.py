from pytest import *
from src.validator import validador

# Caso de prueba 1 rgistro Exitoso (Camino Feliz)
def test_registro_exitoso():
    resultado = validador("Gabriel123", 25)
    assert resultado == "Registro exitoso"

# Caso de prueba 2 Edad fuera de rango (Valor Limite)
def test_edad_menor_minimo():
    resultado = validador("Gabriel123", 17)
    assert "edad fuera del rango" in resultado

# Caso de prueba 3 usuario muy corto (Valor Limite)
def test_usuario_corto():
    resultado = validador("Gabo", 20)
    assert resultado == "Usuarios de 5 - 12 caracteres solamente"
    
# caso de prueba edad incorrecta (No numerica)

def test_edad_no_numerica():
    resultado = validador("Juanpis",'')
    assert resultado == "Error: la edad deber ser un numero"