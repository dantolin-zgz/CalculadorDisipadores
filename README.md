[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

# Interfaz calculadora de disipadores

El presente repositorio contiene el software y documentación necesaria para el uso de la **aplicación Calculo de Disipadores (CdD)**, que sirve para calcular disipadores térmicos y para averiguar la sobrepotencia máxima que soportará un circuito integrado. Este cálculo se encuentra fuertemente ligado a la Electrónica de Potencia.

Contiene el código fuente del calculador ([`calc.py`](calc.py)), el de la interfaz gráfica ([`gui.py`](gui.py)), la [documentación](docs/instrucciones.md) y la teoría del cálculo en los tres regímenes de trabajo considerados: [régimen de excitación continua](docs/teoriaRegimenPermanente.md), [tren de pulsos](docs/teoriaTrenPulsos.md) y [de pulso único](docs/teoriaPulsoUnico.md). Además se ha generado un ejecutable de Windows, [gui.exe](gui.exe).

Junto con la teoría asociada se incluyen una serie de ejercicios resueltos y explicados que permiten conocer el procedimiento de cálculo del disipador necesario para un dispositivo semiconductor de electrónica de potencia en sus diferentes modos de funcionamiento: Ejercicio resuelto para un semiconductor en [régimen de excitación continua](docs/EjerciciosResueltos/regimenPermanente.md), Ejercicio resuelto con un [tren de pulsos](docs/EjerciciosResueltos/trenPulsos.md) y de [pulso único](docs/EjerciciosResueltos/pulsoUnico.md) como regímenes de funcionamiento.

Por otro lado, hay unos [ejercicios prorpuestos](docs/EjerciciosPropuestos/EnunciadosEjPropuestos.md) para que ayuden a afianzar los conceptos de la teoría y de los ejercicios de ejemplo.

 El código de la aplicación está desarrollado en Python para que la aplicación sea multiplataforma y pueda ser utilizada tanto en sistemas operativos Windows, Linux o MacOS, usando los recursos que ofrece el paquete [PySimpleGUI](https://github.com/PySimpleGUI/PySimpleGUI). Para el uso del software puede ser necesaria la [descarga de Python](https://www.python.org/downloads/).

El conjunto de lo anteriormente comentado convierte a la aplicación en un Recurso Educativo en Abierto (REA), *Open Educative Resource* (OER), en inglés. Esto está alineado con los siguientes [Objetivos de Desarrollo Sostenible (ODS) de la Agenda 2030 de Naciones Unidas](https://www.un.org/sustainabledevelopment/es/), contribuyendo en cierta medida a su logro número 4: **Educación de calidad**. Concretamente en los siguientes puntos:
- **4.3 Asegurar el acceso igualitario a la formación superior:** De aquí a 2030, asegurar el acceso igualitario de todos los hombres y las mujeres a una formación técnica, profesional y superior de calidad, incluida la enseñanza universitaria.
- **4.4 Aumento de las competencias para acceder al empleo:** De aquí a 2030, aumentar considerablemente el número de jóvenes y adultos que tienen las competencias necesarias, en particular técnicas y profesionales, para acceder al empleo, el trabajo decente y el emprendimiento.


## Autores
Los autores del proyecto son Diego Antolín Cañada y Daniel Enériz Orta.
