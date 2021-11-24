## LIMITACIÓN DE POTENCIA MÁXIMA CAPAZ DE DISIPAR UN DISPOSITIVO EN RÉGIMEN DE EXCITACIÓN CONTINUA.
El valor máximo de la temperatura de operación, también denominada TEMPERATURA DE LA UNIÓN, Tj, determina la potencia máxima que puede disipar el componente.
Cuando el componente conduce, se produce una absorción de potencia en las uniones que origina un calentamiento en su estructura interna, de modo que un flujo de calor sale hacia el exterior, su valor resulta proporcional a la diferencia de temperaturas entre el interior, Tj, y la cápsula externa, Tc. En régimen estacionario se establece un equilibrio térmico en el que el flujo hacia el exterior compensa exactamente el que se genera en el interior, siendo éste proporcional a la potencia P disipada en las uniones:

Tj-Tc=Rjc∙P

Donde Rjc (°C/W) representa la RESISTENCIA TÉRMICA unión-cápsula.

Para cada valor de Tc, existe un límite de potencia, PLIM, correspondiente a la MÁXIMA TEMPERATURA DE OPERACIÓN, (Tj)MAX. Ese límite resulta tanto mayor cuanto menor es la temperatura de la cápsula externa, Tc, de modo que el valor mínimo de ésta, coincidente con la temperatura ambiente (típicamente 25°C), Ta, define el valor medio límite de MÁXIMA POTENCIA que puede disipar el componente, PMAX:
P_LIM=(〖(Tj)〗_MAX-Tc)/Rjc, P_MAX=(〖(Tj)〗_MAX-Ta)/Rjc  =(〖(Tj)〗_MAX-25°)/Rjc
La posibilidad de manejar potencias importantes por está condicionada al mantenimiento del encapsulado a una temperatura lo más baja posible, es decir, próxima a la temperatura ambiente, Ta, lo que exige unas buenas condiciones de transferencia calorífica de la cápsula al exterior. Esta transferencia cápsula-ambiente puede caracterizarse por la expresión:
Tc-Ta=Rca∙P
Donde Rca (°C/W) representa la RESISTENCIA TÉRMICA cápsula-ambiente.
La transferencia global unión-ambiente puede caracterizarse mediante una resistencia térmica resultante Rja, del siguiente modo:
Tj-Tc=Rjc∙P,Tc-Ta=Rca∙P□(⇒┬ ) Tj-Ta=Rja∙P,Rja=Rjc+Rca≈Rca
A ciertos niveles de potencia, el alto valor de Rca dará lugar a un gradiente térmico entre la unión y el ambiente que eleve la temperatura de aquélla por encima de su valor máximo, (Tj)MAX, con la consiguiente destrucción del componente.
Para solventar este problema, deben utilizarse DISIPADORES TÉRMICOS que, en contacto con la cápsula, faciliten la transferencia a la atmósfera circundante el flujo de calor que alcanza aquélla procedente del interior, a través de la drástica reducción de la resistencia térmica cápsula-ambiente, Rca. En estas condiciones, el proceso global correspondiente a las transferencias cápsula-disipador, Rcs, y disipador-ambiente, Rsa; Rca puede descomponerse en esas dos componentes:
Rca=Rcs+Rsa
Normalmente, Rsa>Rcs, por lo que la transferencia de calor cápsula-ambiente puede caracterizarse de la forma:
Tc-Ta=Rca∙P=(Rcs+Rsa)∙P≈Rsa∙P

## REFERENCIAS
[1]	V. Fernández, F.J. Pérez, C. Bernal, “Electrónica de Potencia: Teoría, Problemas y Prácticas”. Servicio de publicaciones Universidad de Zaragoza.
[2]	A. Barrado, A. Lázaro, “Problemas de Electrónica de Potencia”. Pearson, 2007 
