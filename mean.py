__author__ = 'Anna'

import main
import statistics
from collections import namedtuple
from operator import truediv

d1 = main.load_file("voc/DEP/11042_1_voc.TextGrid")
d2 = main.load_file("voc/DEP/11052_1_voc.TextGrid")
d3 = main.load_file("voc/DEP/11064_1_voc.TextGrid")
d4 = main.load_file("voc/DEP/11092_1_voc.TextGrid")
d5 = main.load_file("voc/DEP/11093_1_voc.TextGrid")
d6 = main.load_file("voc/DEP/11107_1_voc.TextGrid")
d7 = main.load_file("voc/DEP/11122_1_voc.TextGrid")
nd1 = main.load_file("voc/NON-DEP/11036_1_voc.TextGrid")
nd2 = main.load_file("voc/NON-DEP/11037_1_voc.TextGrid")
nd3 = main.load_file("voc/NON-DEP/11041_1_voc.TextGrid")
nd4 = main.load_file("voc/NON-DEP/11043_1_voc.TextGrid")
nd5 = main.load_file("voc/NON-DEP/11096_1_voc.TextGrid")
nd6 = main.load_file("voc/NON-DEP/11108_1_voc.TextGrid")
nd7 = main.load_file("voc/NON-DEP/11115_1_voc.TextGrid")

DEP_len = [d1.maxTimestamp, d2.maxTimestamp, d3.maxTimestamp, d4.maxTimestamp, d5.maxTimestamp, d6.maxTimestamp, d7.maxTimestamp]
NON_DEP_len = [nd1.maxTimestamp, nd2.maxTimestamp, nd3.maxTimestamp, nd4.maxTimestamp, nd5.maxTimestamp, nd6.maxTimestamp, nd7.maxTimestamp]
DEP_mean = statistics.mean(DEP_len)
NON_DEP_mean = statistics.mean(NON_DEP_len)

Entry = namedtuple('Entry', ['begin', 'end', 'tag'])

def select_inf_speechlike(f):
    inf_entries = f.tierDict['inf'].entryList
    DEP_inf = main.select_speechlike(inf_entries)
    return DEP_inf

def select_inf_nonspeechlike(f):
    inf_entries = f.tierDict['inf'].entryList
    DEP_inf = main.select_nonspeechlike(inf_entries)
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
    times = main.count_times(v)
    total = main.count_total_time(times)
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







#STANDARYZACJA
# z = (x - mean)/ std
MEAN = (DEP_mean + NON_DEP_mean)/2
LEN = DEP_len + NON_DEP_len
STD = statistics.stdev(LEN)
def standaryzacja1(lst):
    lst2=[]
    for i in lst:
        z = (i - MEAN)/STD
        lst2 = lst2 + [z]
    return lst2

LEN_2 = []
lEN_2 = LEN_2 + standaryzacja1(LEN)
DEP_len_2 = standaryzacja1(DEP_len)
NON_DEP_len_2 = standaryzacja1(NON_DEP_len)
test1 = statistics.mean(lEN_2)
test2 = statistics.stdev(lEN_2)

#no dobra
#to teraz porównanie dwóch średnich?

x=1