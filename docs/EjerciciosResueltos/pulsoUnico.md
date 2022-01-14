<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

# **Ejercicio resuelto sobre el disipador necesario en un Semiconductor trabajando en régimen permanenete con un puslo único de sobrecorriente.**

**Un dispositivo de electrónica de potencia se puede representar de manera genérica como un interruptor, ya que estos dispositivos semiconductores trabajan generalmente entre sus estados estremos de corte y conducción. La Figura1 refleja de manera general el circuito equivalente de funcionamiento de uno de estos dispositivos.**

**En su modo normal de funcionamiento se encontrará sometido a unas condiciones de tensión y corriente como las especificadas en la Figura 2. En esta Figura 2, cuando el interruptor se encuentra cerrado soporta una tensión, $V_{ON}$, y una corriente, $I_{ON}$, iguales a $2\;V$ y $20\;A$ respectivamente. Sin embargo, cuando el interruptor se encuentra abierto suporta una tensión, $V_{OFF}$ y una corriente, $I_{OFF}$, con valores de $60\;V$ y $0\;A$. Los tiempos de conmutación del disposítivo $t_1$ y $t_2$ son iguales a $1\;\mu s$. Su frecuencia de operacion es de $50\;kHz$ y el ciclo de trabajo, $D$ de 0,5.**

<p align="center">
  <img src="../../assets/img/regPer/Ej Fig1.png">
</p>
<p align = "center">Figura 1. – Circuito electrónico con interruptor trabajando en modo on-off pulsante.</p> 


<p align="center">
  <img src="../../assets/img/regPer/Ej Fig2.png">
</p>
<p align = "center">Figura 2. – Formas de onda de la conmutación.</p>

**La temperatura máxima de trabajo que suporta el semiconductor, $(T_J)_{MAX}$ es de $150^{\circ}C$, su constante de tiempo unión-capsula, $\tau$, es igual a $2\;ms$ y las resistencias térmicas unión-cápsula, $R_{JC}$, y cápsula-disipador, $R_{CS}$, son $1^{\circ}C/W$ y $0,2^{\circ}C/W$, respectivamente**

**Se pide determinar el disipador requirido para que dicho componente semiconductor pueda soportar un pulso de sobrecorriente de $200\;A$ como el representado en la Figura 3.**

<p align="center">
  <img src="../../assets/img/regPer/Ej Fig2.png">
</p>
<p align = "center">Figura 3. – Formas de onda de la conmutación en situación de sobrecorriente.</p>

La teoría asociada a la solución de este problema está relacionada con la teoría mostradad en el documento que trata sobre la situación del pulso [Pulso único](docs/teoriaPulsoUnico.md).

La potencia media disipada por el componente esta formada por pontencia perdida durante la conducción y durante la conmutación. Expresiones que vienen explicadas en la resolución del [ejercicio del comportamiento de un semiconductor en régimen permanente](docs/EjerciciosResueltos/regimenPermanente.md).

La potencia media total disipada en régimen normal de operación viene determinado por la expresión: 
$$P=D \cdot I_{ON} \cdot V_{ON}+\frac 16 \cdot V_{OFF} \cdot f \cdot(t_1+t_2)\;\;\;(1)$$
Sustituyendo valores:
$$P=0.5 \cdot 20A \cdot 2V+\frac 16 \cdot 60V \cdot 50kHz \cdot(1\mu s+1\mu s)=20W+20W=40W\;\;\;(2)$$

Por otro lado, necesitamos calcular el calor de la potencia equivalente instantánea en conducciónpara el pulso único de sobrepotencia, $P'_{ON}$, el cual se obtiene de la expresión siguiente:

$$P'_{ON}=P_1+P_2+V_{ON}*I'_{ON}\;\;\;(3)$$

Donde $P_1$ y $P_2$ corresponden a las respectivas perdidas de conmutación en el instante en el que se produde la sobre potencia o sobrecorriente.

$$P'_{ON}=\frac {V_{OFF} \cdot I'_{ON}} {t_{ON}} \cdot \frac {t_1+t_2} {6} + V_{ON} \cdot I'_{ON}\;\;\;(4)$$

Sustituyendo los valores del enunciado del problema se obtiene:
$$P'_{ON}=\frac {60\;V \cdot 200\;A} {10\;\mu s} \cdot \frac {2\;\mu s} {6} + 2\;V \cdot 200\;A=800W\;\;\;(5)$$

Podemos concluir que debido a este pulso de sobrecorriente, de sobreconducción o de sobrepotencia, el semiconductor sufre un incremento de potencia calculado a continuación:

$$\Delta P = P'_{ON}-P = 800\;W-40\;W = 760\;W\;\;\;(6)$$


## Referencias
1.	V. Fernández, F.J. Pérez, C. Bernal, “Electrónica de Potencia: Teoría, Problemas y Prácticas”. Servicio de publicaciones Universidad de Zaragoza.
2.	A. Barrado, A. Lázaro, “Problemas de Electrónica de Potencia”. Pearson, 2007 