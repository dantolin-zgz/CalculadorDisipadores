<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

# Ejercicio ejemplo para el cálculo de disipadores para un dispositivo trabajando en régimen permanente.

**Suponiendo la conmutación del interruptor indicado en la Figura 2, calcular:**

**1. Potencia media disipada en el interruptor.**

**2. Potencia instantánea equivalente en conducción, suponiendo conmutación ideal.**

**3. Disipador requerido suponiendo temperatura ambiente de 30ºC.**

La Figura 1 muestra el esquema conceptual del circuito con los valores de funcionamiento del mismo, mientras que la Figura 2 presenta las señales de conmutación.
<p align="center">
  <img src="../assets/img/teoPulsoUnico/Fig1.png">
</p>
<p align = "center">Figura 1. – Circuito electrónico equivalente al comportamiento térmico.AUN SIN PONER IMAGEN</p> 


<p align="center">
  <img src="../assets/img/teoPulsoUnico/Fig1.png">
</p>
<p align = "center">Figura 2. – Circuito electrónico equivalente al comportamiento térmico.AUN SIN PONER IMAGEN</p>

Los parámetros de funcionamiento del circuito y de los componentes son los siguientes:
* Tensión de bloque (no conducción: $V_{OFF}=60 V$
* Tensión de conducción:            $V_{ON}=2 V$
* Frecuencia de operación: $f=50kHz$
* Ciclo de trabajo: $D=0.5$
* Resistencia Térmica Unión-Cápsula: $R_{jc}=1ºC/W$
* Resistencia Térmica Cápsula-Disipador: $R_{cs}=0.2ºC/W$

El objetivo final del problema es calcular el disipador necesario para el interruptor que opera en las condiciones citadas y que este pueda trabajar sin romperse por sobrepasar la temperatura máxima de la unión. Para ello es necesario seguir y calcular la información indicada en los puntos en los que se ha dividido el problema.

**1. Potencia media disipada en el interruptor.**
El primer paso es obtener la potencia media disipada por el componente.

La potencia media disipada por el componente esta formada por pontencia perdida durante la conducción y durante la conmutación.
$$P=P_{CONDUCCIÓN}+P_{CONMUTACIÓN}$$
Se procede a obtener el valor de ambas. Las perdidas en conducción vienen definidas por:
$$P_{CONDUCCIÓN}= \frac 1T \cdot \int_{0}^{t_{ON}} p(t) \cdot dt=\frac 1T \cdot \int_{0}^{t_{ON}} I_{ON} \cdot V_{ON} \cdot dt=I_{ON} \cdot V_{ON} \cdot \dfrac {t_{ON}} T=D \cdot I_{ON} \cdot V_{ON}$$

De forma similar las perdidas en comuntación vienen definidas por:
$$P_{CONDUCCIÓN}= \frac 16 \cdot V_{OFF} \cdot f \cdot(t_1+t_2)$$
Siendo $t_1$ el paso de conmutación de OFF a ON y $t_2$ el paso de ON a OFF.

Las perdidas totales son:
$$P=D \cdot I_{ON} \cdot V_{ON}+\frac 16 \cdot V_{OFF} \cdot f \cdot(t_1+t_2)$$
Sustituyendo valores:
$$P=0.5 \cdot 20A \cdot 2V+\frac 16 \cdot 60V \cdot 50kHz \cdot(1\mu s+1\mu s)=20W+20W=40W$$

\cdot  \quad