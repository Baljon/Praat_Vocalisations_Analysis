import scipy

__author__ = 'Anna'

from operator import truediv, add

import start
import statistics
from collections import namedtuple
from operator import truediv
from scipy import stats
from sklearn import preprocessing
import matplotlib.pyplot as plt
from mean import DEP_mothervoc_times_norm
from mean import DEP_s_times_norm
from mean import DEP_s_meantime
from mean import DEP_ns_meantime
from mean import NONDEP_ns_meantime
from mean import NONDEP_s_meantime
from mean import DEP_ns_times_norm
from mean import NONDEP_mothervoc_times_norm
from mean import NONDEP_s_times_norm
from mean import NONDEP_ns_times_norm

# DEP_mean_child = DEP_s_meantime + DEP_ns_meantime
# DEP_mean_child2 = []
# DEP_mean_child2.extend([DEP_mean_child]*7)
#
# NON_DEP_mean_child = NONDEP_ns_meantime + NONDEP_s_meantime
# NON_DEP_mean_child2 = []
# NON_DEP_mean_child2.extend([NON_DEP_mean_child]*7)

def dodaj(lista1,lista2):
    wynik=[]
    wynik.extend(map(add, lista1,lista2))
    return wynik

def count_percentage(voc, lengths):
    percentage = []
    percentage.extend(map(truediv, voc, lengths))
    return percentage

DEP_whole = dodaj(DEP_s_times_norm,DEP_ns_times_norm)
NONDEP_whole = dodaj(NONDEP_ns_times_norm, NONDEP_s_times_norm)
DEP_ns_proportion = count_percentage(DEP_ns_times_norm, DEP_whole)
DEP_s_proportion = count_percentage(DEP_s_times_norm, DEP_whole)
NONDEP_s_proportion = count_percentage(NONDEP_s_times_norm, NONDEP_whole)
NONDEP_ns_proportion = count_percentage(NONDEP_ns_times_norm, NONDEP_whole)
#


z =1
# plt.plot([DEP_s_times_norm])
# plt.ylabel('proportion of child vocalisation')
# plt.show()
import numpy as np

plt.ylabel('proportion of child vocalisation')
plt.xlabel('NONDEP')
# d1 = [1,2,3,4,5,6,7]
# # x1 dep_ns_proporition
# x1 = plt.plot([1,2,3,4,5,6,7],[0.1390970928494917, 0.4873271889401076, 0.04809843400447474, 0.2744261055749015, 0.3315763546592444, 0.7358022381163659, 0.49619257162535146], "ro")
# plt.setp(x1, color='skyblue')
# # #x2 dep_s_proportion
# # x2 = plt.plot([1,2,3,4,5,6,7],[0.8609029071505082, 0.5126728110598924, 0.9519015659955252, 0.7255738944250985, 0.6684236453407556, 0.26419776188363414, 0.5038074283746485], "ro")
# # plt.setp(x2,color ='navy')
# # # plt.plot([1,2,3,4], [1,4,9,16], 'ro')
#
# #nondep_s_prop
# x3 = plt.plot([1,2,3,4,5,6,7],[0.7702770396225384, 0.41502227908180017, 0.7113313909145291, 0.4719101123595398, 0.103227359520977, 0.9461003554587282, 0.8313110691317422] ,"ro")
# plt.setp(x3, color='navy')
# # #nondep_ns_prop
# x4 = plt.plot([1,2,3,4,5,6,7],[0.22972296037746162, 0.5849777209181998, 0.28866860908547093, 0.5280898876404603, 0.8967726404790229, 0.05389964454127179, 0.16868893086825779] ,"ro")
# plt.setp(x4, color='skyblue')
#
# plt.show()