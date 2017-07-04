import scipy
from mean import d1, d2, d3, d4, d5, d6, d7
from mean import nd1, nd2, nd3, nd4, nd5, nd6, nd7
from start import select_speechlike, select_nonspeechlike

__author__ = 'Anna'

def previous_contigency(interakcja, okno=1):
    odpowiedzi = [(czyOdpowiedzMamy(wokalizacja, interakcja, okno), wokalizacja.tag) for wokalizacja in interakcja.tierDict['inf'].entryList]
    poprzednie = []
    for i,_ in enumerate(odpowiedzi):
        poprzednie.append((czy_odpowiedz_poprzedni_tag(i, odpowiedzi), odpowiedzi[i][1]))
    voc_child_s_r_s = len(list((filter(lambda p: p == (True, 's'), poprzednie))))
    voc_child_r_s = len(list((filter(lambda p: p[0] == True, poprzednie))))
    voc_child_s_nor_ns = len(list((filter(lambda p: p == (False, 's'), poprzednie))))
    voc_child_nor_ns = len(list((filter(lambda p: p[0] == False, poprzednie))))
    return (voc_child_s_r_s / voc_child_r_s) - (voc_child_s_nor_ns / voc_child_nor_ns)

def czy_odpowiedz_poprzedni_tag(nr_wokalizacji, odpowiedzi):
    tag = odpowiedzi[nr_wokalizacji][1]
    for i in range(nr_wokalizacji - 1, -1, -1):
        if odpowiedzi[i][1] == tag:
            return odpowiedzi[i][0]
    return False


def contingency(interakcja, okno=1):
    odpowiedzi_speechlike = ileOdpowiedziNaNonSpeechlike(interakcja, okno)
    number_speechlike = len(select_speechlike(interakcja.tierDict['inf'].entryList))
    odpowiedzi_nonspeechlike = ileOdpowiedziNaNonSpeechlike(interakcja, okno)
    number_nonspeechlike = len(select_nonspeechlike(interakcja.tierDict['inf'].entryList))
    return (odpowiedzi_speechlike / number_speechlike) - (odpowiedzi_nonspeechlike / number_nonspeechlike)

def ileOdpowiedziNaSpeechlike(interakcja, okno=1):
    return ileOdpowiedzie(select_speechlike(interakcja.tierDict['inf'].entryList), interakcja, okno)

def ileOdpowiedziNaNonSpeechlike(interakcja, okno=1):
    return ileOdpowiedzie(select_nonspeechlike(interakcja.tierDict['inf'].entryList), interakcja, okno)


def ileOdpowiedzie(wokalizacje, interakcja, okno=1):
    ile = 0
    for wokalizacja_dziecka in wokalizacje:
        if czyOdpowiedzMamy(wokalizacja_dziecka, interakcja, okno):
            ile += 1
    return ile

def czyOdpowiedzMamy(wokalizacja_dziecka, interakcja, okno=1):
    for wokalizacja_mamy in interakcja.tierDict['ma'].entryList:
        if wokalizacja_mamy.begin > wokalizacja_dziecka.begin and wokalizacja_mamy.begin < wokalizacja_dziecka.end + okno:
            return True
        if wokalizacja_mamy.begin > wokalizacja_dziecka.end + okno:
            return False

def liczContingency(listaWczytanychInterakcji,okno):
    contingencies = []
    for interakcja in listaWczytanychInterakcji:
        contingencies.append(contingency(interakcja,okno))
    return contingencies

DEP = [d1,d2,d3,d4,d5,d6,d7]
NONDEP = [nd1,nd2,nd3,nd4,nd5,nd6,nd7]



contingencies1d = liczContingency(DEP,1)
contingencies1nd= liczContingency(NONDEP,1)

con1= scipy.stats.ttest_ind(contingencies1d,contingencies1nd)

#dla innych czasów
contingencies05d = liczContingency(DEP,0.5)
contingencies05nd = liczContingency(NONDEP, 0.5)
contingencies2d = liczContingency(DEP,2)
contingencies2nd = liczContingency(NONDEP,2)
contingencies3d = liczContingency(DEP,3)
contingencies3nd = liczContingency(NONDEP,3)

okna = [0.5,1,2,3]
contingency_okna_DEP = [contingencies05d,contingencies1d,contingencies2d,contingencies3d]
contingency_okna_NONDEP = [contingencies05nd, contingencies1nd, contingencies2nd, contingencies3nd]
def liczPreviousContingencies(listaWczytanychInterakcji, okno):

    prevCont = []
    for interakcja in listaWczytanychInterakcji:
        prevCont.append(previous_contigency(interakcja,okno))
    return prevCont

previous_contigencies1d = liczPreviousContingencies(DEP,1)
previous_contigencies1nd = liczPreviousContingencies(NONDEP,1)
x1= liczContingency(DEP,3)
x2= liczContingency(NONDEP,3)
con2 = scipy.stats.ttest_ind(previous_contigencies1d,previous_contigencies1nd)
con3 = scipy.stats.ttest_ind(x1,x2)
print(con3)


#dla innych czasów
previous_contingencies05d = liczPreviousContingencies(DEP,0.5)
previous_contingencies05nd = liczPreviousContingencies(NONDEP, 0.5)
previous_contingencies2d = liczPreviousContingencies(DEP,2)
previous_contingencies2nd = liczPreviousContingencies(NONDEP,2)
previous_contingencies3d = liczPreviousContingencies(DEP,3)
previous_contingencies3nd = liczPreviousContingencies(NONDEP,3)

prev_cont_dep = [previous_contingencies05d,previous_contigencies1d,previous_contingencies2d,previous_contingencies3d ]
prev_cont_nondep = [previous_contingencies05nd,previous_contigencies1nd,previous_contingencies2nd,previous_contingencies3nd ]



x=1



