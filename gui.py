# PID Interfaz Calculadora de Disipadores (c) by Diego Antolín Cañada, and Daniel Enériz Orta
# 
# PID Interfaz Calculadora de Disipadores is licensed under a
# Creative Commons Attribution-ShareAlike 4.0 International License.
# 
# You should have received a copy of the license along with this
# work. If not, see <http://creativecommons.org/licenses/by-sa/4.0/>.

"""
   Graphical User Interface of the project PID Interfaz Calculadora de
   Disipadores
"""

from PySimpleGUI import Text, Button, Input, Window, HorizontalSeparator, WINDOW_CLOSED
from os import startfile
from calc import *

__author__ = "Diego Antolín Cañada, and Daniel Enériz Orta"
__copyright__ = "Copyright (C) 2021 Diego Antolín Cañada, and Daniel Enériz Orta"
__credits__ = ["Diego Antolín Cañada", "Daniel Enériz Orta"]
__license__ = "CC-BY-SA-4.0"
__version__ = "1.0.3"
__maintainer__ = "Daniel Enériz Orta"
__email__ = "eneriz@unizar.es"
__status__ = "Prototype"


def MainMenu():
    """Implementation of the interaction with the main menu.
    """

    # Define the window's contents
    mainmenu_layout = [[Text('Calculador de disipadores', justification='center', font=("Helvetica", 30))],

          [Button('Instrucciones del programa', font=("Helvetica", 20))],

          [HorizontalSeparator()],

          [ Text('Régimen excitación continua', size=(30,1)),
            Button('Teoría', key="-TEORIACONT-"),
            Button('Calculador', key="-CALCCONT-")
          ],
          
          [ Text('Pulso único', size=(30,1)),
            Button('Teoría', key="-TEORIAUNIC-"),
            Button('Calculador', key="-CALCUNIC-")
          ],

          [Text('Tren de pulsos', size=(30,1)),
           Button('Teoría', key="-TEORIATREN-"),
           Button('Calculador', key="-CALCTREN-")
          ],

          [Text('', key='-ERROR-', text_color='#9D252F', size=(45,2))],

          [Button('Salir')]
         ]

    # Create the main menu window
    window = Window('Calculador de disipadores - Menú Inicio', mainmenu_layout, font=('Helvetica', 18))

    # Display and interact with the home menu using an Event Loop
    while True:

        #---------------------------------------------------------------------------
        #                           QUIT PROGRAM
        #--------------------------------------------------------------------------

        event, values = window.read()
        # See if user wants to quit or window was closed
        if event == WINDOW_CLOSED or event == 'Salir':
            window.close()
            break

        #---------------------------------------------------------------------------
        #                       DISPLAY INTRUCTIONS/THEORY
        #---------------------------------------------------------------------------
        
        # See if user wants to open the instructions file
        if event == 'Instrucciones del programa':
            # Open the PDF with the OS default program
            try:
                startfile('Instrucciones.pdf')
            except(FileNotFoundError):
                window['-ERROR-'].update('La documentación en PDF debe estar disponible en la\nmisma raiz de ejecución del programa')

        # See if user wants to open the theory file of the continuous excitation
        # regime
        if event == '-TEORIACONT-':
            # Open the PDF with the OS default program
            try:
                startfile('RegPer.pdf')
            except(FileNotFoundError):
                window['-ERROR-'].update('La documentación en PDF debe estar disponible en la\nmisma raiz de ejecución del programa')

        # See if user wants to open the theory file of the unique pulse regime
        if event == '-TEORIAUNIC-':
            # Open the PDF with the OS default program
            try:
                startfile('PulUni.pdf')
            except(FileNotFoundError):
                window['-ERROR-'].update('La documentación en PDF debe estar disponible en la\nmisma raiz de ejecución del programa')

        # See if user wants to open the theory file of the train of pulses regime
        if event == '-TEORIATREN-':
            # Open the PDF with the OS default program
            try:
                startfile('TrenPul.pdf')
            except(FileNotFoundError):
                window['-ERROR-'].update('La documentación en PDF debe estar disponible en la\nmisma raiz de ejecución del programa')

        # See if user wants to use the continuous regime calculator
        if event == '-CALCCONT-':
            # Close main menu window
            window.close()
            # Launch continuous regime calculator menu
            CalcCont()

        # See if user wants to use the unique pulse regime calculator
        if event == '-CALCUNIC-':
            # Close main menu window
            window.close()
            # Launch unique pulse regime calculator menu
            CalcUnic()

        # See if user wants to use the train of pulses regime calculator
        if event == '-CALCTREN-':
            # Close main menu window
            window.close()
            # Launch train of pulses regime calculator menu
            CalcTren()


def CalcCont():
    """Continuous regime calculator interface
    """

    calccont_layout = [   

                [Text('Régimen de continua', justification='center', font=("Helvetica", 25))],

                [HorizontalSeparator()],

                [   Text('Temperatura de la unión (Tj):', size=(50,1)),
                    Input(key='-TJ-',
                             size=(5,1),
                             enable_events=True,
                             tooltip='Temperatura de la unión expresada en ºC, por ejemplo 150 ºC'),
                    Text('ºC')
                ],

                [   Text('Temperatura ambiente (Ta):', size=(50,1)),
                    Input(key='-TA-',
                             size=(5,1),
                             enable_events=True,
                             tooltip='Temperatura ambiente expresada en ºC, por ejemplo 25 ºC'),
                    Text('ºC')
                ],

                [   Text('Potencia a disipar por el componente (P):', size=(50,1)),
                    Input(key='-P-',
                             size=(5,1),
                             enable_events=True,
                             tooltip='Potencia a disipar por el componente en W, por ejemplo 3.5 W'),
                    Text('W')
                ],

                [   Text('Resistencia térmica unión-cápsula (Rjc):', size=(50,1)),
                    Input(key='-RJC-',
                             size=(5,1),
                             enable_events=True,
                             tooltip='Resistencia térmica unión-cápsula en ºC/W, por ejemplo 1.6 ºC/W'),
                    Text('ºC/W')
                ],

                [   Text('Resistencia térmica cápsula-disipador (Rcs):', size=(50,1)),
                    Input(key='-RCS-',
                             size=(5,1),
                             enable_events=True,
                             tooltip='Resistencia térmica cápsula-disipador en ºC/W, por ejemplo 2.6 ºC/W'),
                    Text('ºC/W')
                ],

                [Text('', key='-ERROR-', text_color='#9D252F')],

                [   Text('Resistencia térmica disipador ambiente (Rsa):', size=(47,1), font=(None,18,'bold')),
                    Text('--.--', 
                            font=(None,18,'bold'),
                            key='-RSA-',
                            size=(5,1),
                            tooltip='Resistencia térmica disipador ambiente expresada en ºC/W y calculada con los parámetros introducidos'),
                    Text('ºC/W',  font=(None,18,'bold'))
                ],

                [Button('Inicio'), Button('Calcular'), Button('Salir')]

            ]

    # Create the home layout window
    window = Window('Calculador de disipadores - Régimen de continua', calccont_layout, font=('Helvetica', 18))

    # Keys in this layout
    keys = ['-TJ-', '-TA-', '-P-', '-RJC-', '-RCS-']

    # Display and interact with the home menu using an Event Loop
    while True:

        #-----------------------------------------------------------------------
        #                           QUIT PROGRAM
        #-----------------------------------------------------------------------

        event, values = window.read()
        # See if user wants to quit or window was closed
        if event == WINDOW_CLOSED or event == 'Salir':
            window.close()
            break

        #-----------------------------------------------------------------------
        #                    VALDIATE USER NUMERIC INPUTS
        #-----------------------------------------------------------------------
        error = False
        # See if there is any event in the input text boxes
        if event in keys:
            window['-RSA-'].update('--.--')
            # Check if the decimal separator is ',' and display an error if so
            if ',' in values[event]:
                window['-ERROR-'].update('Debes usar el punto (.) como separador de decimales.')
                error = True
            
            # Check if the input is numeric (or blank) and display an error if not
            elif not (values[event].replace('.','',1).replace('-','',1).isdigit() or values[event].replace('-','',1)==''):
                window['-ERROR-'].update('Sólo puedes introducir números.')
                error = True

            else:
                window['-ERROR-'].update('')
        

        #-----------------------------------------------------------------------
        #                   CALCULATE AND DISPLAY OUTPUT
        #-----------------------------------------------------------------------

        # See if user wants to calculate the Rsa and do so if there is no error in the inputs
        if event == 'Calcular' and not error:
            # Check that all the parameters have a value
            if '' in [values[key].replace('-','',1) for key in keys]:
                window['-ERROR-'].update('Debes introducir todos los datos.')
            else:
                # Read the values
                Tj  = float(values['-TJ-'])
                Ta  = float(values['-TA-'])
                P   = float(values['-P-'])
                Rjc = float(values['-RJC-'])
                Rcs = float(values['-RCS-'])

                # Calculate the Rsa value and display it
                Rsa = calculatorRegPer(Tj, Ta, P, Rjc, Rcs)
                window['-RSA-'].update('{:.2f}'.format(Rsa))

                # Check if the Rsa value is negative and display an error if so
                if Rsa < 0:
                    window['-ERROR-'].update('La resistencia térmica disipador ambiente no puede ser negativa.\nRevisa los datos que has introducido.')

        # See if user wants to back home
        if event == 'Inicio':
            # Close submenu window
            window.close()
            # Launch train of pulses regime calculator menu
            MainMenu()


def CalcUnic():
    """Unique pulse regime calculator interface
    """

    calcunic_layout = [   

                [Text('Púlso único', justification='center', font=("Helvetica", 25))],

                [HorizontalSeparator()],

                [   Text('Máxima temperatura de la unión (Tjmax):', size=(50,1)),
                    Input(key='-TJMAX-',
                             size=(5,1),
                             enable_events=True,
                             tooltip='Máxima temperatura de la unión expresada en ºC, por ejemplo 150 ºC'),
                    Text('ºC')
                ],

                [   Text('Temperatura ambiente (Ta):', size=(50,1)),
                    Input(key='-TA-',
                             size=(5,1),
                             enable_events=True,
                             tooltip='Temperatura ambiente expresada en ºC, por ejemplo 25 ºC'),
                    Text('ºC')
                ],

                [   Text('Tension del dispositivo en OFF (Voff):', size=(50,1)),
                    Input(key='-VOFF-',
                             size=(5,1),
                             enable_events=True,
                             tooltip='Tension del dispositivo en OFF en V, por ejemplo 3.5 V'),
                    Text('V')
                ],

                [   Text("Corriente en ON de la sobrepotencia (Ion'):", size=(50,1)),
                    Input(key='-IONSOB-',
                             size=(5,1),
                             enable_events=True,
                             tooltip='Corriente en ON de la sobrepotencia en A, por ejemplo 0.25 A'),
                    Text('A')
                ],

                [   Text("Tiempo en ON de la sobrepotencia (ton'):", size=(50,1)),
                    Input(key='-TONSOB-',
                             size=(5,1),
                             enable_events=True,
                             tooltip='Tiempo en ON de la sobrepotencia en s, por ejemplo 0.15 s'),
                    Text('s')
                ],

                [   Text("Tiempo de conmutación OFF-ON de la sobrepotencia (t1'):", size=(50,1)),
                    Input(key='-T1SOB-',
                             size=(5,1),
                             enable_events=True,
                             tooltip='Tiempo de conmutación OFF-ON de la sobrepotencia en s, por ejemplo 0.01 s'),
                    Text('s')
                ],

                [   Text("Tiempo de conmutación ON-OFF de la sobrepotencia (t2'):", size=(50,1)),
                    Input(key='-T2SOB-',
                             size=(5,1),
                             enable_events=True,
                             tooltip='Tiempo de conmutación ON-OFF de la sobrepotencia en s, por ejemplo 0.01 s'),
                    Text('s')
                ],

                [   Text('Ciclo de trabajo (D):', size=(50,1)),
                    Input(key='-D-',
                             size=(5,1),
                             enable_events=True,
                             tooltip='Ciclo de trabajo (adimensional), por ejemplo 0.25')
                ],

                [   Text('Tension del dispositivo en ON (Von):', size=(50,1)),
                    Input(key='-VON-',
                             size=(5,1),
                             enable_events=True,
                             tooltip='Tension del dispositivo en ON en V, por ejemplo 3.5 V'),
                    Text('V')
                ],

                [   Text("Corriente por el dispositivo en ON (Ion):", size=(50,1)),
                    Input(key='-ION-',
                             size=(5,1),
                             enable_events=True,
                             tooltip='Corriente por el dispositivo en ON en A, por ejemplo 0.25 A'),
                    Text('A')
                ],

                [   Text("Frecuencia de operación del dispositivo (f):", size=(50,1)),
                    Input(key='-F-',
                             size=(5,1),
                             enable_events=True,
                             tooltip='Frecuencia de operación del dispositivo en Hz, por ejemplo 1500000 Hz'),
                    Text('Hz')
                ],

                [   Text("Tiempo de conmutación OFF-ON (t1):", size=(50,1)),
                    Input(key='-T1-',
                             size=(5,1),
                             enable_events=True,
                             tooltip='Tiempo de conmutación OFF-ON en s, por ejemplo 0.01 s'),
                    Text('s')
                ],

                [   Text("Tiempo de conmutación ON-OFF (t2):", size=(50,1)),
                    Input(key='-T2-',
                             size=(5,1),
                             enable_events=True,
                             tooltip='Tiempo de conmutación ON-OFF en s, por ejemplo 0.01 s'),
                    Text('s')
                ],

                [   Text('Impedancia térmica transitoria de púlso único (Zjc(ton)):', size=(50,1)), # ? En las capturas aparecen dos nombres
                    Input(key='-ZJC-',
                             size=(5,1),
                             enable_events=True,
                             tooltip='Impedancia térmica transitoria de púlso único en ºC/W, por ejemplo 1.6 ºC/W'),
                    Text('ºC/W')
                ],

                [   Text('Resistencia térmica equivalente unión-cápsula (Rjc) o\nimpedancia térmica transitoria en régimen de\ntrabajo de tren de pulsos (Zjc(ton,D)):', size=(50,3)),
                    Input(key='-RJC-',
                             size=(5,1),
                             enable_events=True,
                             tooltip='Resistencia térmica equivalente unión-cápsula (Rjc) o impedancia térmica transitoria en régimen de trabajo de tren de pulsos (Zjc(ton,D)) en ºC/W, por ejemplo 1.6 ºC/W'),
                    Text('ºC/W')
                ],

                [   Text('Resistencia térmica cápsula-disipador (Rcs):', size=(50,1)),
                    Input(key='-RCS-',
                             size=(5,1),
                             enable_events=True,
                             tooltip='Resistencia térmica cápsula-disipador en ºC/W, por ejemplo 2.6 ºC/W'),
                    Text('ºC/W')
                ],

                [Text('', key='-ERROR-', text_color='#9D252F')],

                [   Text('Resistencia térmica disipador ambiente (Rsa):', size=(47,1), font=(None,18,'bold')),
                    Text('--.--', 
                            font=(None,18,'bold'),
                            key='-RSA-',
                            size=(5,1),
                            tooltip='Resistencia térmica disipador ambiente expresada en ºC/W y calculada con los parámetros introducidos'),
                    Text('ºC/W',  font=(None,18,'bold'))
                ],

                [Button('Inicio'), Button('Calcular'), Button('Salir')]

            ]

    # Create the home layout window
    window = Window('Calculador de disipadores - Púlso único', calcunic_layout, font=('Helvetica', 18))

    # Keys in this layout
    keys = ['-TJMAX-', '-TA-', '-VOFF-', '-IONSOB-', '-TONSOB-', '-T1SOB-', '-T2SOB-', '-D-', '-VON-', '-ION-', '-F-', '-T1-', '-T2-', '-ZJC-', '-RJC-', '-RCS-']

    # Display and interact with the home menu using an Event Loop
    while True:

        #-----------------------------------------------------------------------
        #                           QUIT PROGRAM
        #-----------------------------------------------------------------------

        event, values = window.read()
        # See if user wants to quit or window was closed
        if event == WINDOW_CLOSED or event == 'Salir':
            window.close()
            break

        #-----------------------------------------------------------------------
        #                    VALDIATE USER NUMERIC INPUTS
        #-----------------------------------------------------------------------
        error = False
        # See if there is any event in the input text boxes
        if event in keys:
            window['-RSA-'].update('--.--')
            # Check if the decimal separator is ',' and display an error if so
            if ',' in values[event]:
                window['-ERROR-'].update('Debes usar el punto (.) como separador de decimales.')
                error = True
            
            # Check if the input is numeric (or blank) and display an error if not
            elif not (values[event].replace('.','',1).replace('-','',1).isdigit() or values[event].replace('-','',1)==''):
                window['-ERROR-'].update('Sólo puedes introducir números.')
                error = True

            else:
                window['-ERROR-'].update('')
        

        #-----------------------------------------------------------------------
        #                   CALCULATE AND DISPLAY OUTPUT
        #-----------------------------------------------------------------------

        # See if user wants to calculate the Rsa and do so if there is no error in the inputs
        if event == 'Calcular' and not error:
            # Check that all the parameters have a value
            if '' in [values[key].replace('-','',1) for key in keys]:
                window['-ERROR-'].update('Debes introducir todos los datos.')
            else:
                # Read the values
                Tjmax  = float(values['-TJMAX-'])
                Ta  = float(values['-TA-'])
                Voff = float(values['-VOFF-'])
                Ionsob = float(values['-IONSOB-'])
                tonsob = float(values['-TONSOB-'])
                t1sob = float(values['-T1SOB-'])
                t2sob = float(values['-T2SOB-'])
                D   = float(values['-D-'])
                Von = float(values['-VON-'])
                Ion = float(values['-ION-'])
                f = float(values['-F-'])
                t1 = float(values['-T1-'])
                t2 = float(values['-T2-'])
                Zjc = float(values['-ZJC-'])
                Rjc = float(values['-RJC-'])
                Rcs = float(values['-RCS-'])

                # Calculate the Rsa value and display it
                Rsa = calculatorRegPer(Tjmax, Ta, Voff, Ionsob, tonsob, t1sob,
                                       t2sob, D, Von, Ion, f, t1, t2, Zjc, Rjc,
                                       Rcs)
                window['-RSA-'].update('{:.2f}'.format(Rsa))

                # Check if the Rsa value is negative and display an error if so
                if Rsa < 0:
                    window['-ERROR-'].update('La resistencia térmica disipador ambiente no puede ser negativa.\nRevisa los datos que has introducido.')

        # See if user wants to back home
        if event == 'Inicio':
            # Close submenu window
            window.close()
            # Launch train of pulses regime calculator menu
            MainMenu()


def CalcTren():
    """Train of pulses calculator interface
    """

    calctren_layout = [   

                [Text('Tren de pulsos', justification='center', font=("Helvetica", 25))],

                [HorizontalSeparator()],

                [   Text('Temperatura de la unión (Tj):', size=(50,1)),
                    Input(key='-TJ-',
                             size=(5,1),
                             enable_events=True,
                             tooltip='Temperatura de la unión expresada en ºC, por ejemplo 150 ºC'),
                    Text('ºC')
                ],

                [   Text('Temperatura ambiente (Ta):', size=(50,1)),
                    Input(key='-TA-',
                             size=(5,1),
                             enable_events=True,
                             tooltip='Temperatura ambiente expresada en ºC, por ejemplo 25 ºC'),
                    Text('ºC')
                ],

                [   Text('Tension del dispositivo en OFF (Voff):', size=(50,1)),
                    Input(key='-VOFF-',
                             size=(5,1),
                             enable_events=True,
                             tooltip='Tension del dispositivo en OFF en V, por ejemplo 3.5 V'),
                    Text('V')
                ],                

                [   Text("Corriente por el dispositivo en ON (Ion):", size=(50,1)),
                    Input(key='-ION-',
                             size=(5,1),
                             enable_events=True,
                             tooltip='Corriente por el dispositivo en ON en A, por ejemplo 0.25 A'),
                    Text('A')
                ],

                [   Text("Frecuencia de operación del dispositivo (f):", size=(50,1)),
                    Input(key='-F-',
                             size=(5,1),
                             enable_events=True,
                             tooltip='Frecuencia de operación del dispositivo en Hz, por ejemplo 1500000 Hz'),
                    Text('Hz')
                ],

                [   Text("Tiempo de conmutación OFF-ON (t1):", size=(50,1)),
                    Input(key='-T1-',
                             size=(5,1),
                             enable_events=True,
                             tooltip='Tiempo de conmutación OFF-ON en s, por ejemplo 0.01 s'),
                    Text('s')
                ],

                [   Text("Tiempo de conmutación ON-OFF (t2):", size=(50,1)),
                    Input(key='-T2-',
                             size=(5,1),
                             enable_events=True,
                             tooltip='Tiempo de conmutación ON-OFF en s, por ejemplo 0.01 s'),
                    Text('s')
                ],

                [   Text('Ciclo de trabajo (D):', size=(50,1)),
                    Input(key='-D-',
                             size=(5,1),
                             enable_events=True,
                             tooltip='Ciclo de trabajo (adimensional), por ejemplo 0.25')
                ],

                [   Text('Impedancia térmica transitoria en situación pulsante (Zjc):', size=(50,1)),
                    Input(key='-ZJC-',
                             size=(5,1),
                             enable_events=True,
                             tooltip='Impedancia térmica transitoria en situación pulsante en ºC/W, por ejemplo 1.6 ºC/W'),
                    Text('ºC/W')
                ],

                [   Text('Resistencia térmica cápsula-disipador (Rcs):', size=(50,1)),
                    Input(key='-RCS-',
                             size=(5,1),
                             enable_events=True,
                             tooltip='Resistencia térmica cápsula-disipador en ºC/W, por ejemplo 2.6 ºC/W'),
                    Text('ºC/W')
                ],

                [Text('', key='-ERROR-', text_color='#9D252F')],

                [   Text('Resistencia térmica disipador ambiente (Rsa):', size=(47,1), font=(None,18,'bold')),
                    Text('--.--', 
                            font=(None,18,'bold'),
                            key='-RSA-',
                            size=(5,1),
                            tooltip='Resistencia térmica disipador ambiente expresada en ºC/W y calculada con los parámetros introducidos'),
                    Text('ºC/W',  font=(None,18,'bold'))
                ],

                [Button('Inicio'), Button('Calcular'), Button('Salir')]

            ]

    # Create the home layout window
    window = Window('Calculador de disipadores - Tren de pulsos', calctren_layout, font=('Helvetica', 18))

    # Keys in this layout
    keys = ['-TJ-', '-TA-', '-D-', '-VOFF-', '-ION-', '-F-', '-T1-', '-T2-', '-ZJC-', '-RCS-']

    # Display and interact with the home menu using an Event Loop
    while True:

        #-----------------------------------------------------------------------
        #                           QUIT PROGRAM
        #-----------------------------------------------------------------------

        event, values = window.read()
        # See if user wants to quit or window was closed
        if event == WINDOW_CLOSED or event == 'Salir':
            window.close()
            break

        #-----------------------------------------------------------------------
        #                    VALDIATE USER NUMERIC INPUTS
        #-----------------------------------------------------------------------
        error = False
        # See if there is any event in the input text boxes
        if event in keys:
            window['-RSA-'].update('--.--')
            # Check if the decimal separator is ',' and display an error if so
            if ',' in values[event]:
                window['-ERROR-'].update('Debes usar el punto (.) como separador de decimales.')
                error = True
            
            # Check if the input is numeric (or blank) and display an error if not
            elif not (values[event].replace('.','',1).replace('-','',1).isdigit() or values[event].replace('-','',1)==''):
                window['-ERROR-'].update('Sólo puedes introducir números.')
                error = True

            else:
                window['-ERROR-'].update('')
        

        #-----------------------------------------------------------------------
        #                   CALCULATE AND DISPLAY OUTPUT
        #-----------------------------------------------------------------------

        # See if user wants to calculate the Rsa and do so if there is no error in the inputs
        if event == 'Calcular' and not error:
            # Check that all the parameters have a value
            if '' in [values[key].replace('-','',1) for key in keys]:
                window['-ERROR-'].update('Debes introducir todos los datos.')
            else:
                # Read the values
                Tj  = float(values['-TJ-'])
                Ta  = float(values['-TA-'])
                D   = float(values['-D-'])
                Voff = float(values['-VOFF-'])
                Ion = float(values['-ION-'])
                f = float(values['-F-'])
                t1 = float(values['-T1-'])
                t2 = float(values['-T2-'])
                Zjc = float(values['-ZJC-'])
                Rcs = float(values['-RCS-'])

                # Calculate the Rsa value and display it
                Rsa = calculatorRegPer(Tj, Ta, Voff, Ion, f, D, t1, t2, Zjc, Rcs)
                window['-RSA-'].update('{:.2f}'.format(Rsa))

                # Check if the Rsa value is negative and display an error if so
                if Rsa < 0:
                    window['-ERROR-'].update('La resistencia térmica disipador ambiente no puede ser negativa.\nRevisa los datos que has introducido.')

        # See if user wants to back home
        if event == 'Inicio':
            # Close submenu window
            window.close()
            # Launch train of pulses regime calculator menu
            MainMenu()


# Launch main menu at the start
MainMenu()