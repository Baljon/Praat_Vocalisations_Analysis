import scipy

__author__ = 'Anna'

import start
import statistics
from collections import namedtuple
from operator import truediv
from scipy import stats
from sklearn import preprocessing
import matplotlib.pyplot as plt



d1 = start.load_file("voc/DEP/11042_1_voc.TextGrid")
d2 = start.load_file("voc/DEP/11052_1_voc.TextGrid")
d3 = start.load_file("voc/DEP/11064_1_voc.TextGrid")
d4 = start.load_file("voc/DEP/11092_1_voc.TextGrid")
d5 = start.load_file("voc/DEP/11093_1_voc.TextGrid")
d6 = start.load_file("voc/DEP/11107_1_voc.TextGrid")
d7 = start.load_file("voc/DEP/11122_1_voc.TextGrid")
nd1 = start.load_file("voc/NON-DEP/11036_1_voc.TextGrid")
nd2 = start.load_file("voc/NON-DEP/11037_1_voc.TextGrid")
nd3 = start.load_file("voc/NON-DEP/11041_1_voc.TextGrid")
nd4 = start.load_file("voc/NON-DEP/11043_1_voc.TextGrid")
nd5 = start.load_file("voc/NON-DEP/11096_1_voc.TextGrid")
nd6 = start.load_file("voc/NON-DEP/11108_1_voc.TextGrid")
nd7 = start.load_file("voc/NON-DEP/11115_1_voc.TextGrid")

DEP_len = [d1.maxTimestamp, d2.maxTimestamp, d3.maxTimestamp, d4.maxTimestamp, d5.maxTimestamp, d6.maxTimestamp, d7.maxTimestamp]
NON_DEP_len = [nd1.maxTimestamp, nd2.maxTimestamp, nd3.maxTimestamp, nd4.maxTimestamp, nd5.maxTimestamp, nd6.maxTimestamp, nd7.maxTimestamp]
DEP_mean = statistics.mean(DEP_len)
NON_DEP_mean = statistics.mean(NON_DEP_len)

Entry = namedtuple('Entry', ['begin', 'end', 'tag'])

def select_inf_speechlike(f):
    inf_entries = f.tierDict['inf'].entryList
    DEP_inf = start.select_speechlike(inf_entries)
    return DEP_inf

def select_inf_nonspeechlike(f):
    inf_entries = f.tierDict['inf'].entryList
    DEP_inf = start.select_nonspeechlike(inf_entries)
    return DEP_inf

def select_ma_voc(f):
    mother_voc = f.tierDict['ma'].entryList
    return mother_voc

d1_mothervoc = select_ma_voc(d1)
d2_mothervoc = select_ma_voc(d2)
d3_mothervoc = select_ma_voc(d3)
d4_mothervoc = select_ma_voc(d4)
d5_mothervoc = select_ma_voc(d5)
d6_mothervoc = select_ma_voc(d6)
d7_mothervoc = select_ma_voc(d7)

d1_inf_s = select_inf_speechlike(d1)
d2_inf_s = select_inf_speechlike(d2)
d3_inf_s = select_inf_speechlike(d3)
d4_inf_s = select_inf_speechlike(d4)
d5_inf_s = select_inf_speechlike(d5)
d6_inf_s = select_inf_speechlike(d6)
d7_inf_s = select_inf_speechlike(d7)

d1_inf_ns = select_inf_nonspeechlike(d1)
d2_inf_ns = select_inf_nonspeechlike(d2)
d3_inf_ns = select_inf_nonspeechlike(d3)
d4_inf_ns = select_inf_nonspeechlike(d4)
d5_inf_ns = select_inf_nonspeechlike(d5)
d6_inf_ns = select_inf_nonspeechlike(d6)
d7_inf_ns = select_inf_nonspeechlike(d7)

nd1_mothervoc = select_ma_voc(nd1)
nd2_mothervoc = select_ma_voc(nd2)
nd3_mothervoc = select_ma_voc(nd3)
nd4_mothervoc = select_ma_voc(nd4)
nd5_mothervoc = select_ma_voc(nd5)
nd6_mothervoc = select_ma_voc(nd6)
nd7_mothervoc = select_ma_voc(nd7)


nd1_inf_s = select_inf_speechlike(nd1)
nd2_inf_s = select_inf_speechlike(nd2)
nd3_inf_s = select_inf_speechlike(nd3)
nd4_inf_s = select_inf_speechlike(nd4)
nd5_inf_s = select_inf_speechlike(nd5)
nd6_inf_s = select_inf_speechlike(nd6)
nd7_inf_s = select_inf_speechlike(nd7)

nd1_inf_ns = select_inf_nonspeechlike(nd1)
nd2_inf_ns = select_inf_nonspeechlike(nd2)
nd3_inf_ns = select_inf_nonspeechlike(nd3)
nd4_inf_ns = select_inf_nonspeechlike(nd4)
nd5_inf_ns = select_inf_nonspeechlike(nd5)
nd6_inf_ns = select_inf_nonspeechlike(nd6)
nd7_inf_ns = select_inf_nonspeechlike(nd7)


def count_voc_time(v):
    times = start.count_times(v)
    total = start.count_total_time(times)
    return total

DEP_s_times = [count_voc_time(d1_inf_s),count_voc_time(d2_inf_s),count_voc_time(d3_inf_s),count_voc_time(d4_inf_s),count_voc_time(d5_inf_s),count_voc_time(d6_inf_s), count_voc_time(d7_inf_s)]
DEP_s_meantime = statistics.mean(DEP_s_times)

DEP_ns_times = [count_voc_time(d1_inf_ns),count_voc_time(d2_inf_ns),count_voc_time(d3_inf_ns),count_voc_time(d4_inf_ns),count_voc_time(d5_inf_ns),count_voc_time(d6_inf_ns), count_voc_time(d7_inf_ns)]
DEP_ns_meantime = statistics.mean(DEP_ns_times)

DEP_mothervoc_times = [count_voc_time(d1_mothervoc),count_voc_time(d2_mothervoc),count_voc_time(d3_mothervoc),count_voc_time(d4_mothervoc),count_voc_time(d5_mothervoc),count_voc_time(d6_mothervoc), count_voc_time(d7_mothervoc)]
DEP_mothervoc_meantime = statistics.mean(DEP_mothervoc_times)

NONDEP_s_times = [count_voc_time(nd1_inf_s),count_voc_time(nd2_inf_s),count_voc_time(nd3_inf_s),count_voc_time(nd4_inf_s),count_voc_time(nd5_inf_s),count_voc_time(nd6_inf_s), count_voc_time(nd7_inf_s)]
NONDEP_s_meantime = statistics.mean(NONDEP_s_times)

NONDEP_ns_times = [count_voc_time(nd1_inf_ns),count_voc_time(nd2_inf_ns),count_voc_time(nd3_inf_ns),count_voc_time(nd4_inf_ns),count_voc_time(nd5_inf_ns),count_voc_time(nd6_inf_ns), count_voc_time(nd7_inf_ns)]
NONDEP_ns_meantime = statistics.mean(NONDEP_ns_times)

NONDEP_mothervoc_times = [count_voc_time(nd1_mothervoc),count_voc_time(nd2_mothervoc),count_voc_time(nd3_mothervoc),count_voc_time(nd4_mothervoc),count_voc_time(nd5_mothervoc),count_voc_time(nd6_mothervoc), count_voc_time(nd7_mothervoc)]
NONDEP_mothervoc_meantime = statistics.mean(NONDEP_mothervoc_times)

DEP_s_std = statistics.stdev(DEP_s_times)
DEP_ns_std = statistics.stdev(DEP_ns_times)
DEP_mothervoc_std = statistics.stdev(DEP_mothervoc_times)
NONDEP_s_std = statistics.stdev(NONDEP_s_times)
NONDEP_ns_std = statistics.stdev(NONDEP_s_times)
NONDEP_mothervoc_std = statistics.stdev(NONDEP_mothervoc_times)

#wszystko fajnie ale te wartosci nic nam nie dadza
#zrobmy moze procenty?

# interakcja -> suma wokalizacji czas -> podzielić przez długość interakcji
# srednia procentow
#i to samo dla drugiej grupy

DEP_s_times
DEP_ns_times
DEP_interaction_lengths = [d1.maxTimestamp, d2.maxTimestamp, d3.maxTimestamp, d4.maxTimestamp, d5.maxTimestamp, d6.maxTimestamp, d7.maxTimestamp]
NONDEP_s_times
NONDEP_ns_times
NONDEP_interaction_lengths = [nd1.maxTimestamp, nd2.maxTimestamp, nd3.maxTimestamp, nd4.maxTimestamp, nd5.maxTimestamp, nd6.maxTimestamp, nd7.maxTimestamp]

TOTAL_interactions_time = sum(DEP_interaction_lengths) + sum(NONDEP_interaction_lengths)
TOTAL_interactions_time_minutes = TOTAL_interactions_time/60
TOTAL_interactions_time_hours = TOTAL_interactions_time_minutes/60


def count_percentage(voc, lengths):
    percentage = []
    percentage.extend(map(truediv, voc, lengths))
    return percentage

DEP_s_percentage = count_percentage(DEP_s_times, DEP_interaction_lengths)
DEP_ns_percentage = count_percentage(DEP_ns_times,DEP_interaction_lengths)
NONDEP_s_percentage = count_percentage(NONDEP_s_times, NONDEP_interaction_lengths)
NONDEP_ns_percentage = count_percentage(NONDEP_ns_times, NONDEP_interaction_lengths)

mean_percentage_dep_s = statistics.mean(DEP_s_percentage)
mean_percentage_dep_ns = statistics.mean(DEP_ns_percentage)
mean_percentage_dep_whole = (mean_percentage_dep_ns + mean_percentage_dep_s)/2

mean_percentage_nondep_s = statistics.mean(NONDEP_s_percentage)
mean_percentage_nondep_ns = statistics.mean(NONDEP_ns_percentage)
mean_percentage_nondep_whole = (mean_percentage_nondep_ns + mean_percentage_nondep_s)/2

#no dobra to może teraz dla sprawdzenia mamy?
DEP_mothervoc_percentage = count_percentage(DEP_mothervoc_times, DEP_interaction_lengths)
NONDEP_mothervoc_percentage = count_percentage(NONDEP_mothervoc_times, NONDEP_interaction_lengths)
mean_percentage_dep_mothervoc = statistics.mean(DEP_mothervoc_percentage)
mean_percentage_nondep_mothervoc = statistics.mean(NONDEP_mothervoc_percentage)

#i cisza..?




#STANDARYZACJA
# z = (x - mean)/ std
def standaryzacja1(lst, mean, std):
    lst2=[]
    for i in lst:
        z = (i - mean)/std
        lst2 = lst2 + [z]
    return lst2


NS = DEP_ns_times + NONDEP_ns_times
NS_mean1 = statistics.mean(NS)
NS_stdev1 = statistics.stdev(NS)
S = DEP_s_times + NONDEP_s_times
VOC = DEP_mothervoc_times + NONDEP_mothervoc_times

NS_standaryzacja = standaryzacja1(NS, NS_mean1, NS_stdev1)

# checkIfNormal_NS = scipy.stats.normaltest(NS)
# checkIfNormal_S = scipy.stats.normaltest(S)
# checkIfNormal_VOC = scipy.stats.normaltest(VOC)
#var= scipy.stats.ttest_ind(DEP_ns_times,NONDEP_ns_times)
#var2=scipy.stats.ttest_ind(DEP_ns_percentage,NONDEP_ns_percentage)
#var3 = scipy.zscore(NS)

#MUSIMY PRZESKALOWAĆ ZMIENNE
# A/B = X/C
# zatem X = (A * C)/B
# A - CZAS WOKALIZACJI (S/NS/VOC)
# B - CZAS INTERAKCJI
# C - ŚREDNI CZAS INTERAKCJI
# X - PRZESKALOWANA ZMIENNA

DEP_mean
NON_DEP_mean

def przeskalowanie(listaCzasówWokalizacji, listaCzasówInterakcji, średniCzasInterakcji):
    x = []
    A = listaCzasówWokalizacji
    B = listaCzasówInterakcji
    C = średniCzasInterakcji
    for czas in A:
        var = czas * C
        x.append(var)
    y = []
    y.extend(map(truediv, x, B))
    return y

DEP_ns_times_norm = przeskalowanie(DEP_ns_times, DEP_interaction_lengths, DEP_mean)
DEP_s_times_norm = przeskalowanie(DEP_s_times, DEP_interaction_lengths, DEP_mean)
DEP_mothervoc_times_norm = przeskalowanie(DEP_mothervoc_times, DEP_interaction_lengths, DEP_mean)

NONDEP_ns_times_norm = przeskalowanie(NONDEP_ns_times, NONDEP_interaction_lengths, NON_DEP_mean)
NONDEP_s_times_norm = przeskalowanie(NONDEP_s_times, NONDEP_interaction_lengths, NON_DEP_mean)
NONDEP_mothervoc_times_norm = przeskalowanie(NONDEP_mothervoc_times, NONDEP_interaction_lengths, NON_DEP_mean)

var= scipy.stats.ttest_ind(DEP_ns_times_norm,NONDEP_ns_times_norm)
var2= scipy.stats.ttest_ind(DEP_s_times_norm,NONDEP_s_times_norm)
var3= scipy.stats.ttest_ind(DEP_mothervoc_times_norm,NONDEP_mothervoc_times_norm)

#nic nie wyszlo
#do tabelek
#test dokładny fishera, chi kwadrat
x=1
