# PID Interfaz Calculadora de Disipadores (c) by Diego Antolín Cañada, and Daniel Enériz Orta
# 
# PID Interfaz Calculadora de Disipadores is licensed under a
# Creative Commons Attribution-ShareAlike 4.0 International License.
# 
# You should have received a copy of the license along with this
# work. If not, see <http://creativecommons.org/licenses/by-sa/4.0/>.

"""
This file contains the functions to calculate the thermal dissipater values in
the following regimes: continuous excitation, unique pulse and train of pulses.
"""

__author__ = "Diego Antolín Cañada, and Daniel Enériz Orta"
__copyright__ = "Copyright (C) 2021 Diego Antolín Cañada, and Daniel Enériz Orta"
__credits__ = ["Diego Antolín Cañada", "Daniel Enériz Orta"]
__license__ = "CC-BY-SA-4.0"
__version__ = "1.0.3"
__maintainer__ = "Daniel Enériz Orta"
__email__ = "eneriz@unizar.es"
__status__ = "Prototype"



# TODO: Revisar las traducciones

def  calculatorRegPer(Tj: float, Ta: float, P: float, Rjc: float, Rcs: float) -> float:
    """This method calculates the thermal dissipater value needed in a device
    under continuous regime.

    Args:
        Tj (float): Junction temperature
        Ta (float): Ambient temperature # ? ¿Quizás mejor Room temperature?
        P (float): Average power
        Rjc (float): Junction-capsule thermic resistance
        Rcs (float): Capsule-dissipater thermic resistance 

    Returns:
        float: The needed dissipater-ambient thermic resistance 
    """

    return ((Tj - Ta) / P) - Rjc - Rcs

def calculatorPulUni(Tjmax: float, Ta: float, Voff: float, IonSob: float,
                     tonSob: float, t1Sob: float, t2Sob: float, D: float,
                     Von: float, Ion: float, f: float, t1: float, t2: float,
                     Zjc: float, Rjc: float, Rcs: float) -> float:
    """This method calculates the thermal dissipater value needed in a device
    under continuous excitation regime with overpower. # ? Overload mejor?

    Args:
        Tjmax (float): Maximum junction temperature
        Ta (float): Ambient temperature
        Voff (float): Maximum acceptable voltage with the device in OFF
        IonSob (float): Overpower current
        tonSob (float): Overpower time duration
        t1Sob (float): Overpower commutation time OFF-ON
        t2Sob (float): Overpower commutation time ON-OFF
        D (float): Device's duty cycle
        Von (float): Voltage of the device in conduction
        Ion (float): Current of the device in conduction
        f (float): Work frequency of the device
        t1 (float): Commutation time OFF-ON
        t2 (float): Commutation time ON-OFF
        Zjc (float): Transient thermic impedance of the unique pulse
        Rjc (float): Junction-capsule thermic resistance
        Rcs (float): Capsule-dissipater thermic resistance

    Returns:
        float: Dissipater-ambient thermic resistance
    """
    # Overpower value
    SobrePot = (1 / 6) * Voff * IonSob * (1 / tonSob) * (t1Sob + t2Sob)

    # Power value under the continuous regime
    P = (D * Von * Ion) + ((1 / 6) * Voff * Ion * f * (t1 + t2))

    # Average junction temperature
    Tj = Tjmax - Zjc * (SobrePot - P)

    return ((Tj - Ta) / P) - Rjc - Rcs


def calculatorTrenPul(Tj: float, Ta: float, Voff: float, Ion: float, f: float, D: float, t1: float, t2: float, Zjc: float, Rcs: float) -> float:
    """This method calculates the thermal dissipater value needed in a device
    under train of pulses. Conduction time is supposed to be much less than the
    thermic temporal constant.

    Args:
        Tj (float): Junction temperature
        Ta (float): Ambient temperature
        Voff (float): Maximum acceptable voltage with the device in OFF
        Ion (float): Current of the device in conduction
        f (float): Work frequency of the device
        D (float): Device's duty cycle
         Commutation time OFF-ON
        t2 (float): Commutation time ON-OFF
        Zjc (float): Transient thermic impedance of the unique pulse
        Rcs (float): Capsule-dissipater thermic resistance

    Returns:
        float: Dissipater-ambient thermic resistance
    """
    # Average power
    P = (1 / 6) * Voff * Ion * f * (t1 + t2)

    # Equivalent power in ON
    Poneq = P / D

    #Average capsule temperature
    Tc = Tj - (Poneq * Zjc)

    return ((Tc - Ta) / P) - Rcs
