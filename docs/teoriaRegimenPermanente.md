<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

## Limitación de potencia máxima capaz de disipar un dispositivo en régimen de excitación continua
El valor máximo de la temperatura de operación, también denominada **temperatura de la unión**, $$T_j$$, determina la potencia máxima que puede disipar el componente.
Cuando el componente conduce, se produce una absorción de potencia en las uniones que origina un calentamiento en su estructura interna, de modo que un flujo de calor sale hacia el exterior, su valor resulta proporcional a la diferencia de temperaturas entre el interior, $$T_j$$, y la cápsula externa, $$T_c$$. En régimen estacionario se establece un equilibrio térmico en el que el flujo hacia el exterior compensa exactamente el que se genera en el interior, siendo éste proporcional a la potencia $$P$$ disipada en las uniones:

$$
T_j-T_c=R_{jc} \cdot P
$$

Donde $$R_{jc}$$ (°C/W) representa la **resistencia térmica** unión-cápsula.

Para cada valor de $$T_c$$, existe un límite de potencia, $$P_\text{lim}$$, correspondiente a la **máxima temperatura de operación**, $$(T_j)_{\max}$$. Ese límite resulta tanto mayor cuanto menor es la temperatura de la cápsula externa, $$T_c$$, de modo que el valor mínimo de ésta, coincidente con la temperatura ambiente (típicamente 25°C), $$T_a$$, define el valor medio límite de **máxima potencia** que puede disipar el componente, $$P_{\max}$$:

$$
P_\text{lim}=\frac{(T_j)_{\max}-T_c}{R_{jc}}, \quad P_{\max}=\frac{(T_j)_{\max}-T_a}{R_{jc}}=\frac{(T_j)_{\max}-25°}{R_{jc}}
$$

La posibilidad de manejar potencias importantes está condicionada al mantenimiento del encapsulado a una temperatura lo más baja posible, es decir, próxima a la temperatura ambiente, $$T_a$$, lo que exige unas buenas condiciones de transferencia calorífica de la cápsula al exterior. Esta transferencia cápsula-ambiente puede caracterizarse por la expresión:

$$
T_c-T_a=R_{ca} \cdot P
$$

Donde $$R_{ca}$$ (°C/W) representa la **resistencia térmica cápsula-ambiente**.

La transferencia global unión-ambiente puede caracterizarse mediante una resistencia térmica resultante $$R_{ja}$$, del siguiente modo:

$$
T_j-T_c=R_{jc} \cdot P, \quad T_c-T_a=R_{ca} \cdot P \rightarrow T_j-T_a=R_{ja} \cdot P
$$

$$
R_{ja}=R_{jc}+R_{ca}≈R_{ca}
$$

A ciertos niveles de potencia, el alto valor de $$R_{ca}$$ dará lugar a un gradiente térmico entre la unión y el ambiente que eleve la temperatura de aquélla por encima de su valor máximo, $$(T_j)_{\max}$$, con la consiguiente destrucción del componente.

Para solventar este problema, deben utilizarse **disipadores térmicos** que, en contacto con la cápsula, faciliten la transferencia a la atmósfera circundante el flujo de calor que alcanza aquélla procedente del interior, a través de la drástica reducción de la resistencia térmica cápsula-ambiente, $$R_{ca}$$. En estas condiciones, el proceso global correspondiente a las transferencias cápsula-disipador, $$R_{cs}$$, y disipador-ambiente, $$R_{sa}$$; $$R_{ca}$$ puede descomponerse en esas dos componentes:

$$
R_{ca}=R_{cs}+R_{sa}
$$

Normalmente, $$R_{sa}>R_{cs}$$, por lo que la transferencia de calor cápsula-ambiente puede caracterizarse de la forma:

$$
T_c-T_a=R_{ca} \cdot P=(R_{cs}+R_{sa}) \cdot P \approx R_{sa} \cdot P
$$

## Referencias
1.	V. Fernández, F.J. Pérez, C. Bernal, “Electrónica de Potencia: Teoría, Problemas y Prácticas”. Servicio de publicaciones Universidad de Zaragoza.
2.	A. Barrado, A. Lázaro, “Problemas de Electrónica de Potencia”. Pearson, 2007.
