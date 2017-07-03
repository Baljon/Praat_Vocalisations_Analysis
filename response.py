from pyasn1.compat.octets import null
from start import select_speechlike

__author__ = 'Anna'


def ileOdpowiedziNaSpeechlike(interakcja, okno=1):
    ile = 0
    for wokalizacja_dziecka in select_speechlike(interakcja.tierDict['inf'].entryList):
        if czyOdpowiedzMamy(wokalizacja_dziecka, interakcja, okno):
            ile += 1
    return ile



def czyOdpowiedzMamy(wokalizacja_dziecka, interakcja, okno=1):
    for wokalizacja_mamy in interakcja.tierDict['ma'].entryList:
        if wokalizacja_mamy.begin > wokalizacja_dziecka.begin and wokalizacja_mamy.begin < wokalizacja_dziecka.end + okno:
            return True
        if wokalizacja_mamy.begin > wokalizacja_dziecka.end + okno:
            return False
