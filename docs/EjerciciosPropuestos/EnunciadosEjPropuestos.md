# **Ejericios propuestos**

El presente conjutno de ejercicios pretender servir para asentar los conocimientos presentados en la teoría y a través de los ejericios resueltos. Estos ejercicios están basados en componentes reales, los cuales se indican en los diferentes enunciados. Se incluyen los enlaces donde se pueden descargar las hojas de características de los mismo.

La verificación del resultado se puede realizar utilizando el software Calculador de Disipadores (CdD) [AñadirEnlace].

## **Ejercicio 1**
___
**Un IGBT modelo IGP40N65F5 de [Infineon](https://www.infineon.com/) con un encapsulado PG-TO247-3 se encuentra trabajando entre sus estados extremos (corte y conducción) en el circuito equivalente de la Figura 1.** 

<p align="center">
  <img src="../../assets/img/ejerciciosPropuestos/Ej Fig1.png">
</p>
<p align = "center">Figura 1. – Circuito electrónico con interruptor trabajando en modo on-off pulsante.</p> 

**La temperatura máxima de trabajo que suporta el semiconductor, $$(T_J)_{MAX}$$ es de $$175^{\circ}\text{C}$$, su constante de tiempo unión-capsula, $$\tau$$, es igual a $$2\;\text{ms}$$**


**En su modo normal de funcionamiento se encontrará sometido a unas condiciones de tensión y corriente como las especificadas en la Figura 2. En esta Figura 2, cuando el interruptor se encuentra cerrado soporta una tensión, $$V_{ON}$$, y una corriente, $$I_{ON}$$, iguales a $$1,8\;V$$ y $$40\;A$$ respectivamente. Sin embargo, cuando el interruptor se encuentra abierto suporta una tensión, $$V_{OFF}$$ y una corriente, $$I_{OFF}$$, con valores de $$400\;V$$ y $$0\;A$$. Los tiempos de conmutación del disposítivo $$t_1$$ y $$t_2$$ son iguales a $$250\;ns$$. Su frecuencia de operacion es de $$50\;kHz$$ y el ciclo de trabajo, $$D$$ de $$0,5$$. L**

<p align="center">
  <img src="../../assets/img/ejerciciosPropuestos/Ej Fig2.png">
</p>
<p align = "center">Figura 2. – Forma de onda de la señal de conmutación.</p>


**Las caractarísticas térmicas del dispositivo se recogen en la Figura 3. Mientras que la Figura 4 muestra las gráficas de la resistencia térmica transitoria del IGBT**

<p align="center">
  <img src="../../assets/img/ejerciciosPropuestos/Ej Fig3.png">
</p>
<p align = "center">Figura 3. – Tabla de resistencias del dispositivo.</p>

<p align="center">
  <img src="../../assets/img/ejerciciosPropuestos/Ej Fig4.png">
</p>
<p align = "center">Figura 4. – Resistencia térmica transistoria.</p>

**Estos datos y Figuras han sido extraidos directamente de las [hojas de características del componente IGP40N65F5](https://www.infineon.com/cms/en/product/power/igbt/igbt-discretes/igp40n65f5/#!documents).**

**En las condiciones de operación indicadas se pide determinar:**
1. **Potencia media total en el interruptor.**
2. **Potencia instantánea en conducción, suponiendo una conmutación ideal.**
3. **Temperatura de la cápsula y disipador requerido para una correcta operación del dispositivo, suponiendo una temperatura ambiente de $$30^{\circ}\text{C}$$.**
4. **Determinar el disipador requerido para que dicho componente semiconductor pueda soportar un pulso de sobrecorriente de $$200\;\text{A}$$ como el representado en la Figura 5.**
<p align="center">
  <img src="../../assets/img/ejerciciosPropuestos/Ej Fig5.png">
</p>
<p align = "center">Figura 5. – Forma de onda de la señal de conmutación para una sobrecorriente de 60 A.</p>

5. **Repetir los apartados 1, 2 y 3 para una frecuencia de operación de $$50\;\text{Hz}$$.**