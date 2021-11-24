IMPEDANCIA TÉRMICA TRANSITORIA (PULSO ÚNICO)
El modelo de conducción térmica caracterizado por un circuito puramente resistivo, solamente es válido con una excitación estática en régimen permanente y se corresponde con la situación de equilibrio térmico entre el flujo de calor generado en el interior y el que se propaga hacia el exterior. La inercia propia del sistema a la elevación de temperaturas, con el consiguiente proceso transitorio de propagación, puede caracterizarse mediante la inclusión de condensadores en el correspondiente circuito térmico equivalente. 
 
La inercia térmica aumenta con la superficie de las zonas que soportan el flujo de propagación, por lo que la capacidad asociada al nudo de la unión será de menor valor que las restantes del circuito.
La cápsula y el disipador presentan fuertes inercias a variaciones de temperatura por lo que la cápsula y el disipador permanecen a temperatura ambiente, Ta, en el caso de pulso único.
De acuerdo con el teorema de superposición, cualquier variable de un circuito se expresa en el campo transformado como la superposición de los generadores independientes, las temperaturas de la unión y de la cápsula, así como su diferencia, vendrán dadas por:
Tj(s)=P(s)∙Z'j(s),Tc(s)=P(s)∙Z^' c(s)
Tj(s)-Tc(s)=P(s)∙[Z^' j(s)-Z^' c(s)]
Tjc(s)=P(s)∙Z'jc(s)
Donde Z’jc(s) es la impedancia térmica operacional.
Suponiendo una excitación estática, la situación puede expresarse de la forma:
P(s)=P/S; Tjc(s)=P∙[(Z^' jc(s))/S], Tjc(t)=P∙£^(-1) [(Z^' jc(s))/S]=P∙Zjc(t)
Donde P=Pon, potencia en el nivel alto del pulso y Zjc(t) es la IMPEDANCIA TÉRMICA TRANSITORIA UNIÓN-CÁPSULA DE PULSO ÚNICO.
Para un pulso de larga duración, puede considerarse el efecto único de la capacidad térmica asociada a la unión, dado su menor valor, mientras que los otros condensadores pueden suponerse cortocircuitos, lo que significa admitir que la cápsula y el posible disipador permanecen a temperatura ambiente, consecuentemente con la inercia propia de estas regiones. En estas condiciones el sistema resulta de primer orden, con lo cual:
Zjc=Zjc(t)=Rjc(1-e^(-ton⁄τ))
Tjc(t)=P∙Zjc(t)=P∙Rjc(1-e^(-ton⁄τ) )<P∙Rjc
 
El gradiente térmico unión-cápsula tiende al valor de régimen permanente P·Rjc, de acuerdo con el modelo de circuito resistivo, siendo valores típicos de la constante de tiempo esencialmente inferiores a 1s en componentes de alta potencia. En relación con la expresión anterior, el gradiente térmico máximo unión-cápsula, (Tjc)MAX, correspondiente a la temperatura máxima de la unión, (Tj)MAX, establecerá el límite de potencia PLIM, de pulso de duración ton:
P_LIM=〖(Tjc)〗_MAX/(Zjc(ton))=(〖(Tj)〗_MAX-Ta)/(Zjc(ton))>(〖(Tj)〗_MAX-Ta)/Rjc=P_MAX
ton≪τ: Zjc(ton)≈Rjc(ton/τ)
P_LIM=τ/ton  ((Tj)_MAX-Ta)/Rjc=τ/ton P_MAX≫P_MAX
Siendo PMAX la potencia máxima en operación continua.
Por consiguiente, para tiempos de conducción (ton≪τ), el hecho de que la impedancia térmica resulte muy inferior al valor de la correspondiente resistencia, Zjc(ton)≪Rjc, determina que la potencia disipada pueda ser bastante mayor que el valor máximo en régimen de operación continua, sin que ello suponga la elevación de la temperatura de la unión por encima de su valor máximo, (Tj)MAX, lo que supondría la destrucción del componente.
Sin embargo, el caso más habitual de pulso único de corta duración e intensidad elevada corresponde a un proceso transitorio superpuesto a una situación de conducción limitada. Análogamente a la situación analizada con anterioridad, la temperatura de la cápsula, Tc, puede suponerse inalterada por el transitorio, por lo que las variaciones térmicas asociadas a un incremento de potencia ΔP quedan restringidas a la unión, de modo que puede considerarse como superposición a un régimen permanente.
 
Por consiguiente, la disponibilidad límite de potencia, ΔPLIM, asociada a la máxima variación del gradiente térmico unión-cápsula, resulta determinada por el margen entre la temperatura de la unión correspondiente al proceso permanente, Tj, y su valor máximo (Tj)MAX, de la forma:
〖∆(Tjc)〗_MAX=〖(∆Tj)〗_MAX-Tc=〖(Tj)〗_MAX-Tj=〖∆P〗_LIM∙Zjc(ton)
〖∆P〗_LIM=(〖(Tj)〗_MAX-Tj)/(Zjc(ton))
De modo que esta expresión coincide con la correspondiente a una conducción de pulso único, situación con anterioridad, sin más que hacer Tj=Ta.
Se deduce, pues, que la posibilidad de soportar picos importantes de potencia es función tanto de la impedancia térmica transitoria de pulso único, Zjc, cuya dependencia temporal es dada por el fabricante, como del hecho de establecer una operación permanente con una temperatura de la unión, Tj, esencialmente inferior a su valor máximo.
REFERENCIAS
[1]	V. Fernández, F.J. Pérez, C. Bernal, “Electrónica de Potencia: Teoría, Problemas y Prácticas”. Servicio de publicaciones Universidad de Zaragoza.
[2]	A. Barrado, A. Lázaro, “Problemas de Electrónica de Potencia”. Pearson, 2007 

