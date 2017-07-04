__author__ = 'Anna'
from response import czyOdpowiedzMamy
from start import select_speechlike, select_nonspeechlike

def liczResponseLag(interakcja,okno=1):
    responseLag = []
    wokalizacjeDziecka = select_speechlike(interakcja)
    for wokalizacjaDziecka in wokalizacjeDziecka:
        if czyOdpowiedzMamy(wokalizacjaDziecka,interakcja):
            wokalizacjeMamy = interakcja.tierDict['ma']
            for voc in wokalizacjeMamy:
                if voc.begin > wokalizacjaDziecka.begin and wokalizacjaDziecka.end + okno > voc.begin:
                    lag = voc.begin - wokalizacjaDziecka.begin
                    responseLag.append(lag)
    return responseLag
