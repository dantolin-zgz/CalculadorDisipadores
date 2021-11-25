<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

# Manual de Usuario del Programa Calculador de Disipadores (CdD)

- [Menú Principal](#menú-principal)
- [Menús modo de operación](#menús-modo-de-operación)
    - [Régimen de excitación continua](#régimen-de-excitación-continua)
    - [Púlso único](#pulso-único)
    - [Tren de pulsos](#tren-de-pulsos)
- [Tratamiento de errores](#tratamiento-de-errores)

El presente documento contiene las instrucciones necesarias para el uso de la **aplicación Calculo de Disipadores (CdD)**, que sirve para calcular disipadores térmicos y para averiguar la sobrepotencia máxima que soportará un circuito integrado. Este cálculo se encuentra fuertemente ligado a la Electrónica de Potencia.

El código del software, así como todos los documentos asociados se encuentran en [este repositorio de Github](https://github.com/dantolin-zgz/CalculadorDisipadores/). Todo el conjunto se encuentra bajo una licencia [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). El código de la aplicación se está desarrollado en Python para que la aplicación sea multiplataforma y pueda ser utilizada tanto en sistemas operativos Windows, Linux o MAC.

El conjunto de lo anteriormente comentado convierte a la aplicación en un Recurso Educativo en Abierto (REA), Open Educative Resource (OER), en inglés. Esto está alineado con los siguientes [Objetivos de Desarrollo Sostenible (ODS) de la Agenda 2030 de Naciones Unidas](https://www.un.org/sustainabledevelopment/es/), contribuyendo en cierta medida a su logro número 4: **Educación de calidad.** Concretamente en los siguientes puntos:
* **4.3 Asegurar el acceso igualitario a la formación superior:** De aquí a 2030, asegurar el acceso igualitario de todos los hombres y las mujeres a una formación técnica, profesional y superior de calidad, incluida la enseñanza universitaria.
* **4.4 Aumento de las competencias para acceder al empleo:** De aquí a 2030, aumentar considerablemente el número de jóvenes y adultos que tienen las competencias necesarias, en particular técnicas y profesionales, para acceder al empleo, el trabajo decente y el emprendimiento.

A continuación, se van a presentar y explicar el uso de los diferentes menús, comenzando por el menú principal.

## Menú principal
La Figura 1 muestra el menú principal. Desde el menú se puede acceder directamente a este mismo documento pulsando el botón **Instrucciones del programa**.

![Menu Principal](/assets/img/Fig1.png)
<p align = "center">Figura 1. – Menú Principal</p>

Desde este menú se puede acceder a las diferentes funcionalidades de la aplicación. Comenzaremos explicando para que sirven los diferentes menús disponibles en el menú. 

En primer lugar, el botón **Salir** cierra la aplicación.

Además de los botones **Instrucciones del programa** y **Salir** existen otros 6 botones. Cada  pareja de ellos (**Teoría-Calculador**) se encuentra etiquetada con un texto que hace referencia a los diferentes modos de operación (régimen de excitación continua, pulso único y tren de pulsos) en los que se puede encontrar un dispositivo electrónico (circuito integrado) para el que queremos calcular cuál es la resistencia térmica disipador-ambiente –resistencia térmica del disipador– necesaria para que éste opere dentro de sus límites térmicos.

Cada uno de los botones **Teoría** permiten acceder al documento que contiene la teoría asociada al modo de operación referenciado por la etiqueta. El documento se lanza sobre la aplicación para la lectura de documentos pdf que el usuario tenga instalada en su ordenador. Cada documento contiene la teoría/información necesaria para comprender los conceptos relacionados con el cálculo de disipadores y en los diferentes regímenes de funcionamiento.

Al lanzarse el documento frente al programa instalado por el usuario, la aplicación CdD queda en un segundo plano, de manera que el usuario pueda consultar la documentación necesaria y continuar utilizando CdD al mismo tiempo.

Los documentos de teoría tienen el siguiente aspecto:

![Documentacion PDF](/assets/img/Fig2.png)
<p align="center">Figura 2. – Ejemplo de documento pdf con contenido teórico.</p>

Por último, cada uno de los botones **Calculador** lanzan una nueva ventana asociada a cada uno de los modos de operación donde se recogerán los datos necesarios para la realización del calculo que permite obtener el valor de la resistencia térmica del disipador necesaria para un dispositivo, así como la sobrepotencia máxima que puede soportar un circuito integrado dependiendo de su régimen de funcionamiento.

A continuación, se explican detalladamente los menús que aparecen para el cálculo en los diferentes modos de operación.

## Menús modo de operación

### Régimen de excitación continua
El menú que aparece para la realización del cálculo de la resistencia térmica necesaria por un componente que se encuentra trabajando en un **Régimen de excitación continua**, es el que se muestra en la Figura 3:

![Menu Regimen de excitacion continua](/assets/img/Fig3.png)
<p align = "center">Figura 3. – Menú para el cálculo de disipadores en dispositivos trabajando en régimen de excitación continua.</p>

Para realizar el cálculo, basta con introducir los parámetros requeridos y presionar el botón **Calcular**, entonces el resultado aparece en la parte inferior de la ventana, indicado por la etiqueta que se muestra en negrita.

Los parámetros a introducir en este menú son los siguientes:
* $T_j$: Temperatura máxima de la unión.
* $T_a$: Temperatura ambiente.
* $P$: Potencia que disipa el componente en régimen permanente de excitación continua.
* $R_{jc}$: Resistencia térmica equivalente unión-cápsula.
* $R_{cs}$: Resistencia térmica equivalente cápsula-disipador.

El resultado se muestra en la negrita junto con la etiqueta **Resistencia térmica disipador ambiente ($R_{sa}$)**.

El botón **Inicio** devuelve el programa al Menú principal (menú anterior) y el botón **Salir** cierra el programa. Estos dos botones funcionan del mismo modo en todos los menús.

### Pulso único
El menú mostrado por la aplicación para el cálculo de la resistencia térmica necesaria por un componente para una situación de **Pulso único**, es el que se muestra en la Figura 4:

![Menu Regimen de excitacion continua](/assets/img/Fig4.png)
<p align = "center">Figura 4. – Menú para el cálculo de disipadores en dispositivos sometido a un pulso único de potencia.</p>

Para realizar el cálculo de la sobrepotencia máxima, basta con introducir los parámetros requeridos y presionar el botón **Calcular**, entonces el resultado aparece en la parte inferior de la ventana, indicado por la etiqueta que se muestra en negrita.

Los parámetros a introducir en este menú son:
* $(T_j)_{\max}$: Temperatura máxima de la unión.
* $T_a$: Temperatura ambiente.
* $V_{off}$: Tensión del componente cuando no está conduciendo.
* $I_{on}'$: Corriente en el instante de la sobrepotencia.
* $t_{on}'$: Tiempo que dura la situación de sobrepotencia.
* $t_1'$: Tiempo de conmutación off - on de la sobrepotenica.
* $t_2'$: Tiempo de conmutación on - off de la sobrepotenica.
* $D$: Ciclo de trabajo del dispositivo.
* $V_{on}$: Tensión del componente cuando está conduciendo y operando en condiciones normales.
* $I_{on}$: Corriente por el dispositivo cuando conduce en condiciones normales de trabajo.
* $f$: Frecuencia de trabajo del dispositivo.
* $t_1$: Tiempo de conmutación off – on en condiciones normales de trabajo.
* $t_2$: Tiempo de conmutación on - off en condiciones normales de trabajo.
* $R_{jc}$ o $Z_{jc}(t_{on},D)$: Resistencia térmica equivalente unión-cápsula o impedancia térmica transitoria en régimen de trabajo de tren de pulsos. Dependiendo de las condiciones de trabajo a las que se encuentre sometido el dispositivo.
* $R_{cs}$: Resistencia térmica equivalente cápsula-disipador.
* $R_{sa}$: Resistencia térmica equivalente disipador-ambiente.
* $Z_{jc}(t_{on})$: Impedancia térmica transitoria de pulso único.

El resultado se muestra en la negrita junto con la etiqueta **Resistencia térmica disipador ambiente ($R_{sa}$)**, necesario para soportar la sobrepotencia correspondiente.

El botón **Inicio** devuelve el programa al Menú principal (menú anterior) y el botón **Salir** cierra el programa. Estos dos botones funcionan del mismo modo en todos los menús.

### Tren de pulsos
El menú mostrado por la aplicación para el cálculo de la resistencia térmica necesaria por un componente para una situación de **Tren de pulsos**, es el que se muestra en la Figura 5:

![Menu para calculo de Tren de pulsos](/assets/img/Fig5.png)
<p align = "center">Figura 5. – Menú para el cálculo de disipadores en dispositivos sometido a un tren de pulsos de potencia.</p>

Para realizar el cálculo, basta con introducir los parámetros requeridos y presionar el botón **Calcular**, entonces el resultado aparece en la casilla de abajo, correspondiente a la etiqueta que se muestra en negrita.

Los parámetros a introducir en este menú son:
* $T_j$: Temperatura máxima de la unión.
* $T_a$: Temperatura ambiente.
* $V_{off}$: Tensión del componente cuando no está conduciendo.
* $I_{on}$: Corriente por el dispositivo cuando conduce. 
* $D$: Ciclo de trabajo del dispositivo.
* $f$: Frecuencia de trabajo del dispositivo.
* $t_1$: Tiempo de conmutación off – on en condiciones normales de trabajo.
* $t_2$: Tiempo de conmutación on - off en condiciones normales de trabajo.
* D: Ciclo de trabajo.
* $Z_{jc}$ (ton,D): Impedancia térmica transitoria en régimen de trabajo de tren de pulsos.
* $R_{cs}$: Resistencia térmica equivalente cápsula-disipador.

El resultado se muestra en la negrita junto con la etiqueta **Resistencia térmica disipador ambiente ($R_{sa}$)**.

El botón **Inicio** devuelve el programa al Menú principal (menú anterior) y el botón **Salir** cierra el programa. Estos dos botones funcionan del mismo modo en todos los menús.

## Tratamiento de errores
Los errores que se pueden producir son los siguientes:
* Al menos uno de los cuadros en destinados a introducir los valores necesarios para el cálculo de la resistencia térmica del disipador se encuentre vacía. En este caso aparece el mensaje mostrado en la Figura 6 dentro de la propia ventana del CdD.

![Error por asuncia/falta de parametros de entrada](/assets/img/Fig6.png)
<p align = "center">Figura 6. – Mensaje de error en el proceso de cálculo por falta de al menos un valor en los cuadros de entrada de datos.</p>

* También puede ocurrir que el resultado obtenido sea un valor negativo. Por ello se indica la solución en ROJO, resaltando que existe un error. Esto se acompaña con el mensaje “*Hay un error en el cálculo, la Resistencia Térmica disipador-ambiente no puede tener un valor negativo*”. Este hecho se muestra en la Figura 7.

![Error por valor Rsa negativo](/assets/img/Fig7.png) 
<p align = "center">Figura 7. – Mensaje de error en el proceso de cálculo por resultado Rsa negativo.</p>

