<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

# **Ejercicios propuestos**

El presente conjunto de ejercicios pretender servir para asentar los conocimientos explicados en la teoría y a través de los ejericios resueltos. Estos ejercicios están basados en componentes reales, los cuales se indican en los diferentes enunciados. Se incluyen los enlaces donde se pueden descargar las hojas de características de los mismo.

La verificación del resultado se puede realizar utilizando el software Calculador de Disipadores (CdD) [AñadirEnlace].

## **Ejercicio 1**
___
**Un IGBT modelo IGP40N65F5 de [Infineon](https://www.infineon.com/) con un encapsulado PG-TO220-3 se encuentra trabajando entre sus estados extremos (corte y conducción) en el circuito equivalente de la Figura 1.** 

<p align="center">
  <img src="../../assets/img/ejerciciosPropuestos/Ej Fig1.png">
</p>
<p align = "center">Figura 1. – Circuito electrónico con interruptor trabajando en modo on-off pulsante.</p> 

**La temperatura máxima de trabajo que suporta el semiconductor, $(T_J)_{MAX}$ es de $175^{\circ}\text{C}$, su constante de tiempo unión-capsula,$\tau$, es igual a $200\;\text{ms}$**


**En su modo normal de funcionamiento se encontrará sometido a unas condiciones de tensión y corriente como las especificadas en la Figura 2. En esta Figura 2, cuando el interruptor se encuentra cerrado soporta una tensión, $V_{ON}$, y una corriente, $I_{ON}$, iguales a $1,8\;V$ y $40\;A$ respectivamente. Sin embargo, cuando el interruptor se encuentra abierto suporta una tensión, $V_{OFF}$ y una corriente, $I_{OFF}$, con valores de $400\;V$ y $0\;A$. Los tiempos de conmutación del dispositivo $t_1$ y $t_2$ son iguales a $15\;ns$. Su frecuencia de operación es de $50\;kHz$ y el ciclo de trabajo, $D$ de $0,5$.**

<p align="center">
  <img src="../../assets/img/ejerciciosPropuestos/Ej Fig2.png">
</p>
<p align = "center">Figura 2. – Forma de onda de la señal de conmutación. Nota: En esta figura la tensión y la corriente conmutan a la vez, lo cual indica que la carga que ve el dispositivo es resistiva. </p>


**Las características térmicas del dispositivo se recogen en la Figura 3. Mientras que la Figura 4 muestra las gráficas de la resistencia térmica transitoria del IGBT**

<p align="center">
  <img src="../../assets/img/ejerciciosPropuestos/Ej Fig3.png">
</p>
<p align = "center">Figura 3. – Tabla de resistencias del dispositivo.</p>

<p align="center">
  <img src="../../assets/img/ejerciciosPropuestos/Ej Fig4.png">
</p>
<p align = "center">Figura 4. – Resistencia térmica transitoria.</p>

**Estos datos y Figuras han sido extraídos directamente de las [hojas de características del componente IGP40N65F5](https://www.infineon.com/cms/en/product/power/igbt/igbt-discretes/igp40n65f5/#!documents).**

**En las condiciones de operación indicadas se pide determinar:**
1. **Potencia media total en el interruptor.**
2. **Potencia instantánea en conducción, suponiendo una conmutación ideal.**
3. **Temperatura de la cápsula y disipador requerido para una correcta operación del dispositivo, suponiendo una temperatura ambiente de $30^{\circ}\text{C}$.**
4. **Determinar el disipador requerido para que dicho componente semiconductor pueda soportar un pulso de sobrecorriente de $60\;\text{A}$ como el representado en la Figura 5.**
<p align="center">
  <img src="../../assets/img/ejerciciosPropuestos/Ej Fig5.png">
</p>
<p align = "center">Figura 5. – Forma de onda de la señal de conmutación para una sobrecorriente de 60 A.</p>

5. **Repetir los apartados 1, 2 y 3 para una frecuencia de operación de $50\;\text{Hz}$.**


## **Ejercicio 2**
___
**Un IGBT modelo IRFB7730PbF de [Infineon](https://www.infineon.com/) con un encapsulado PG-TO220-3 se encuentra trabajando entre sus estados extremos (corte y conducción) en el circuito equivalente de la Figura 6.** 

<p align="center">
  <img src="../../assets/img/ejerciciosPropuestos/Ej Fig6.png">
</p>
<p align = "center">Figura 6. – Circuito electrónico con interruptor trabajando en modo on-off pulsante.</p> 

**La temperatura máxima de trabajo que suporta el semiconductor, $(T_J)_{MAX}$ es de $175^{\circ}\text{C}$, su constante de tiempo unión-capsula, $\tau$, es igual a $200\;\text{ms}$**


**En su modo normal de funcionamiento se encontrará sometido a unas condiciones de tensión y corriente como las especificadas en la Figura 7. En esta Figura 7, cuando el interruptor se encuentra cerrado soporta una tensión, $V_{ON}$, y una corriente, $I_{ON}$$, iguales a $0,26\;V$ y $100\;A$ respectivamente. Sin embargo, cuando el interruptor se encuentra abierto suporta una tensión, $V_{OFF}$ y una corriente, $I_{OFF}$, con valores de $75\;V$ y $0\;A$$. Los tiempos de conmutación del dispositivo $t_1$ y $t_2$ son iguales a $120\;ns$. Su frecuencia de operación es de $30\;kHz$ y el ciclo de trabajo, $D$ de $0,5$.**

<p align="center">
  <img src="../../assets/img/ejerciciosPropuestos/Ej Fig7.png">
</p>
<p align = "center">Figura 7. – Forma de onda de la señal de conmutación.</p>


**Las características térmicas del dispositivo se recogen en la Figura 8. Mientras que la Figura 9 muestra las gráficas de la resistencia térmica transitoria del MOSFET CANAL N**

<p align="center">
  <img src="../../assets/img/ejerciciosPropuestos/Ej Fig8.png">
</p>
<p align = "center">Figura 8. – Tabla de resistencias del dispositivo.</p>

<p align="center">
  <img src="../../assets/img/ejerciciosPropuestos/Ej Fig9.png">
</p>
<p align = "center">Figura 9. – Resistencia térmica transitoria.</p>

**Estos datos y Figuras han sido extraídos directamente de las [hojas de características del componente IRFB7730PbF](https://www.infineon.com/cms/en/product/power/mosfet/n-channel/irfs7730/#!documents).**

**En las condiciones de operación indicadas se pide determinar:**
1. **Potencia media total en el interruptor.**
2. **Potencia instantánea en conducción, suponiendo una conmutación ideal.**
3. **Temperatura de la cápsula y disipador requerido para una correcta operación del dispositivo, suponiendo una temperatura ambiente de $30^{\circ}\text{C}$.**
4. **Determinar el disipador requerido para que dicho componente semiconductor pueda soportar un pulso de sobrecorriente de $150\;\text{A}$ como el representado en la Figura 10.**
<p align="center">
  <img src="../../assets/img/ejerciciosPropuestos/Ej Fig10.png">
</p>
<p align = "center">Figura 10. – Forma de onda de la señal de conmutación para una sobrecorriente de 150 A.</p>

5. **Repetir los apartados 1, 2 y 3 para una frecuencia de operación de $50\;\text{Hz}$.**