## IMPEDANCIA TÉRMICA TRANSITORIA (TREN DE PULSOS).

La aproximación ideal de la onda de potencia supone incluir en el valor permanente de conducción la contribución de los transitorios de conmutación.
Por tanto, se utiliza un VALOR EQUIVALENTE DE LA POTENCIA INSTANTANEA EN CONDUCCIÓN, Pon, relacionado con la potencia media, P.
P=1/T ∫_0^ton▒〖Pon∙dt〗=D∙Pon, Pon=P/D; D=ton/T
Donde P es la resultante de los términos estacionario y de conmutación.
 
Con la excitación indicada, la situación puede explicarse mediante un proceso repetitivo de carga-descarga de las capacidades del circuito equivalente, en correspondencia con los intervalos de calentamiento y enfriamiento, respectivamente, de modo que el gradiente térmico unión-cápsula, Tjc, va elevándose hasta estabilizarse en un régimen permanente de sucesivas fluctuaciones (rizado) alrededor de un valor medio, donde éste es la respuesta estacionaria a la componente continua de excitación y, por consiguiente, con los condensadores en circuito abierto. Sin embargo, ese valor medio del gradiente térmico puede ser poco relevante en el caso de que las fluctuaciones sean importantes, por lo que resulta de interés determinar el correspondiente valor máximo.
Debido al mayor valor de las capacidades, se despreciarán en régimen permanentes las variaciones térmicas de la cápsula y del posible disipador, lo que significa aproximar los condensadores asociados como cortocircuito a todos los armónicos de la onda rectangular de excitación, mientras que a la componente continua de ésta actúan, obviamente, como circuito abierto. De este modo, la cápsula y el disipador pueden suponerse a temperaturas fijas, determinadas por los valores de las correspondientes resistencias térmicas y de la potencia media, mientras que las fluctuaciones quedan restringidas a la unión.
MODELO DE CIRCUITO ELÉCTRICO TRANSITORIO EQUIVALENTE
 p(t)=P+∑_(n=1)^∞▒〖P_n w_n 〗
Cj<<Cc<<Cs
Las impedancias de los condensadores son del tipo |Z|=1/(C∙ω). Cc y Cs son lo suficientemente grandes como para considerar que a frecuencias bajas Zc y Zs tienden a 0, se comportan como cortocircuitos.
Dado que el problema puede dividirse en una situación continua más una variable en régimen permanente con un nivel de continua asociado y cada una puede asociarse a distintos elementos del circuito, dividimos el circuito y analizamos el problema por separado.
COMPONENTE INTREMENTAL
 
Circuito asociado a las variaciones de temperatura en la unión.
COMPONENTE ASOCIADA AL NIVEL MEDIO EN RÉGIMEN PERMANENTE
 
Circuito asociado a las temperaturas constantes de la cápsula y el disipador.
ANALIZANDO LA SICUACIÓN DE LA UNIÓN:
	Intervalo ton → Intervalo de carga de Cj:
Tjc(t)=Tjc(∞)+[Tjc(0)-Tjc(∞)] e^(-t⁄τ)
Tjc(t)=Pon∙Rjc+[Tjc(0)-Pon∙Rjc] e^(-t⁄τ)
	Intervalo toff → Intervalo de descarga de Cj:
Tjc(t)=Tjc(0)e^(-t⁄τ)
De estas expresiones se obtiene:
〖(Tjc)〗_MAX=Pon∙Rjc (1-e^(-ton⁄τ))/(1-e^(-T⁄τ) )=Pon∙Zjc
Siendo Pon la potencia instantánea equivalente en conducción y Zjc la IMPEDANCIA TÉRMICA TRANSITORIA UNIÓN-CÁPSULA EN SITUACIÓN PULSANTE.
Esta impedancia depende del tiempo de conducción, ton y del ciclo de trabajo D del componente, de modo que:
Zjc=Zjc(ton,D)=Rjc (1-e^(-ton⁄τ))/(1-e^(-T⁄τ) )=Rjc (1-e^(-ton⁄τ))/(1-e^(-ton⁄Dτ) )<Rjc
De acuerdo con este resultado, las curvas de impedancia térmica Zjc(ton,D) relativas a la correspondiente resistencia Rjc y, por tanto, normalizadas a la unidad, se representan en la siguiente figura, tomando el ciclo de trabajo D como parámetro.
 
REFERENCIAS
[1]	V. Fernández, F.J. Pérez, C. Bernal, “Electrónica de Potencia: Teoría, Problemas y Prácticas”. Servicio de publicaciones Universidad de Zaragoza.
[2]	A. Barrado, A. Lázaro, “Problemas de Electrónica de Potencia”. Pearson, 2007 
