from scipy import mean
from mean import d1

__author__ = 'Anna'
from response import czyOdpowiedzMamy
from start import select_speechlike, select_nonspeechlike
from response import DEP, NONDEP

def liczResponseLag(interakcja,okno=1):
    responseLag = []
    inf_entries = interakcja.tierDict['inf'].entryList
    wokalizacjeDziecka = select_speechlike(inf_entries)
    for wokalizacjaDziecka in wokalizacjeDziecka:
        if czyOdpowiedzMamy(wokalizacjaDziecka,interakcja):
            wokalizacjeMamy = interakcja.tierDict['ma'].entryList
            for voc in wokalizacjeMamy:
                if voc.begin > wokalizacjaDziecka.begin and wokalizacjaDziecka.end + okno > voc.begin:
                    lag = voc.begin - wokalizacjaDziecka.begin
                    responseLag.append(lag)
    return responseLag

test = liczResponseLag(d1)

def zliczWszystkieResponseLagi(listaInterakcji,okno=1):
    listaLagow =[]
    for interakcja in listaInterakcji:
        lagiInterakcji=[]
        lagiInterakcji.extend(liczResponseLag(interakcja))
        listaLagow.append(lagiInterakcji)
    return listaLagow

DEPlags = zliczWszystkieResponseLagi(DEP)
NONDEPlags = zliczWszystkieResponseLagi(NONDEP)

def liczWascSrednia(laglist):
    srednie = []
    for interakcja in laglist:
        x = mean(interakcja)
        srednie.append(x)
    return srednie

DEPlags_means = liczWascSrednia(DEPlags)
NONDEPlags_means = liczWascSrednia(NONDEPlags)
x=1