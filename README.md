# MiniMTP-Testing-Lab
#  Mini MTP - Sistema de Validación de Usuarios

Este proyecto contiene el **Mini Test Plan (MTP)** y la automatización mínima viable para un sistema de validación de registros, desarrollado como parte de la estrategia de aseguramiento de calidad.

##  Contexto y Alcance
El sistema bajo prueba es un módulo de validación en Python encargado de verificar los requisitos de negocio para el registro de nuevos usuarios:
- **In Scope:** Validación de longitud de nombre de usuario (5-12 caracteres) y rango de edad (18-99 años).
- **Out of Scope:** Persistencia en base de datos, recuperación de contraseñas y validación de identidad biométrica.

##  Stack Tecnológico
- **Lenguaje:** Python 3.14+
- **Testing Framework:** Pytest
- **CI/CD:** GitHub Actions
- **Control de Versiones:** Git & GitHub

##  Estrategia de Pruebas
Se aplicaron técnicas de **Caja Negra**:
1. **Partición de Equivalencia:** Probar datos válidos dentro de los rangos permitidos.
2. **Análisis de Valores Límite:** Verificación de los bordes críticos (17, 18, 99, 100 años).

### Evidencia de ejecución (CI/CD)
El proyecto cuenta con un workflow automatizado que ejecuta las pruebas en cada `push`. 
> **Estado actual:** ✅ 3 Passed (Ver pestaña [Actions]((https://github.com/GabrielBlanc0o/MiniMTP-Testing-Lab/actions/runs/22682178974/job/65755363341))


##  Gestión de Defectos
Siguiendo las directrices de Mozilla, se documentaron los hallazgos durante el ciclo:
- **BUG-01:** Error de comparación de tipos (String vs Int). *Estado: Cerrado.*
- **BUG-02:** Inconsistencia de mayúsculas en mensajes de error. *Estado: Corregido.*

## 📂 Estructura del Repositorio
- `src/`: Código fuente del validador.
- `tests/`: Scripts de prueba automatizados.
- `docs/`: Documentación formal (Anexo 1 - Mini MTP).
- `.github/workflows/`: Configuración del pipeline de CI.

---
**Entregable por:** Gabriel Tarazona Blanco
**Versión:** v1.0  
**Fecha:** Marzo 2026
