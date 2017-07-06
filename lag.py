__author__ = 'Anna'
import xlwt
from scipy import mean
from response import czyOdpowiedzMamy
from start import select_speechlike, select_nonspeechlike
from response import DEP, NONDEP

#speechlike
def liczResponseLagS(interakcja,okno=1):
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
#nonspeechlike
def liczResponseLagNS(interakcja,okno=1):
    responseLag = []
    inf_entries = interakcja.tierDict['inf'].entryList
    wokalizacjeDziecka = select_nonspeechlike(inf_entries)
    for wokalizacjaDziecka in wokalizacjeDziecka:
        if czyOdpowiedzMamy(wokalizacjaDziecka,interakcja):
            wokalizacjeMamy = interakcja.tierDict['ma'].entryList
            for voc in wokalizacjeMamy:
                if voc.begin > wokalizacjaDziecka.begin and wokalizacjaDziecka.end + okno > voc.begin:
                    lag = voc.begin - wokalizacjaDziecka.begin
                    responseLag.append(lag)
    return responseLag
#all
def liczResponseLagALL(interakcja,okno=1):
    responseLag = []
    inf_entries = interakcja.tierDict['inf'].entryList
    wokalizacjeDziecka = inf_entries
    for wokalizacjaDziecka in wokalizacjeDziecka:
        if czyOdpowiedzMamy(wokalizacjaDziecka,interakcja):
            wokalizacjeMamy = interakcja.tierDict['ma'].entryList
            for voc in wokalizacjeMamy:
                if voc.begin > wokalizacjaDziecka.begin and wokalizacjaDziecka.end + okno > voc.begin:
                    lag = voc.begin - wokalizacjaDziecka.begin
                    responseLag.append(lag)
    return responseLag

def zliczWszystkieResponseLagiS(listaInterakcji,okno=1):
    listaLagow =[]
    for interakcja in listaInterakcji:
        lagiInterakcji=[]
        lagiInterakcji.extend(liczResponseLagS(interakcja,okno))
        listaLagow.append(lagiInterakcji)
    return listaLagow
def zliczWszystkieResponseLagiNS(listaInterakcji,okno=1):
    listaLagow =[]
    for interakcja in listaInterakcji:
        lagiInterakcji=[]
        lagiInterakcji.extend(liczResponseLagNS(interakcja,okno))
        listaLagow.append(lagiInterakcji)
    return listaLagow
def zliczWszystkieResponseLagiALL(listaInterakcji,okno=1):
    listaLagow =[]
    for interakcja in listaInterakcji:
        lagiInterakcji=[]
        lagiInterakcji.extend(liczResponseLagALL(interakcja,okno))
        listaLagow.append(lagiInterakcji)
    return listaLagow

DEPlagsS = zliczWszystkieResponseLagiS(DEP,okno=2)
NONDEPlagsS = zliczWszystkieResponseLagiS(NONDEP,okno=2)
DEPlagsNS = zliczWszystkieResponseLagiNS(DEP,okno=2)
NONDEPlagsNS = zliczWszystkieResponseLagiNS(NONDEP,okno=2)
DEPlagsALL = zliczWszystkieResponseLagiALL(DEP,okno=2)
NONDEPlagsALL = zliczWszystkieResponseLagiALL(NONDEP,okno=2)

def liczWascSrednia(laglist):
    srednie = []
    for interakcja in laglist:
        x = mean(interakcja)
        srednie.append(x)
    return srednie

#DEPlags_means = liczWascSrednia(DEPlags)
#NONDEPlags_means = liczWascSrednia(NONDEPlags)

def robTuple(el):
    listaTupli = []
    for lista in el:
        x = tuple(lista)
        listaTupli.append(x)
    return listaTupli

def robTupleTupli(listaTupli):
    tuplaTupli = tuple(listaTupli)
    return tuplaTupli

DEPtupleS = robTupleTupli(robTuple(DEPlagsS))
NONDEPtupleS = robTupleTupli(robTuple(NONDEPlagsS))
DEPtupleNS = robTupleTupli(robTuple(DEPlagsNS))
NONDEPtupleNS = robTupleTupli(robTuple(NONDEPlagsNS))
DEPtupleALL = robTupleTupli(robTuple(DEPlagsALL))
NONDEPtupleALL = robTupleTupli(robTuple(NONDEPlagsALL))
#NONDEP1 =

def wyeksportuj(DATA,nazwa):
    wb = xlwt.Workbook()
    ws = wb.add_sheet("My Sheet")
    for i, row in enumerate(DATA):
        for j, col in enumerate(row):
            ws.write(i, j, col)
    ws.col(0).width = 256 * max([len(row) for row in DATA])
    return wb.save(nazwa)

wyeksportuj(DEPtupleS,"depS.xls")
wyeksportuj(NONDEPtupleS,"nondepS.xls")
wyeksportuj(DEPtupleNS,"depNS.xls")
wyeksportuj(NONDEPtupleNS,"nondepNS.xls")
wyeksportuj(DEPtupleALL,"depALL.xls")
wyeksportuj(NONDEPtupleALL,"nondepALL.xls")
x=1