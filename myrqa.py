import bisect
from response import d1, d2, d3, d4, d5, d6, d7
from response import nd1, nd2, nd3, nd4, nd5, nd6, nd7


def binary(interakcja, osoba, okno=0.25, prog_ciszy=0.5):
	wokalizacje = interakcja.tierDict[osoba].entryList
	current = 0
	end = interakcja.maxTimestamp
	binary_list = []
	while current < end:
		nearest_voc = znajdz_najblizsza_po_czasie(wokalizacje, current)
		if nearest_voc is None:
			binary_list.append("0")
		elif nearest_voc.begin > current + okno:
			binary_list.append("0")
		else:
			binary_list.append("1")
		current = current + okno
	return binary_list


def znajdz_najblizsza_po_czasie(wokalizacje, czas):
	for voc in wokalizacje:
		if voc.begin > czas:
			return voc
	return None
	# dummy_voc = (czas, czas + 1, "ns")
	# index = bisect.bisect_left(wokalizacje, dummy_voc)
	# return wokalizacje[index]

d1_mama = binary(d1, "ma")
d2_mama = binary(d2, "ma")
d3_mama = binary(d3, "ma")
d4_mama = binary(d4, "ma")
d5_mama = binary(d5, "ma")
d6_mama = binary(d6, "ma")
d7_mama = binary(d7, "ma")

d1_dziecko = binary(d1, "inf")
d2_dziecko = binary(d2, "inf")
d3_dziecko = binary(d3, "inf")
d4_dziecko = binary(d4, "inf")
d5_dziecko = binary(d5, "inf")
d6_dziecko = binary(d6, "inf")
d7_dziecko = binary(d7, "inf")

nd1_mama = binary(nd1, "ma")
nd2_mama = binary(nd2, "ma")
nd3_mama = binary(nd3, "ma")
nd4_mama = binary(nd4, "ma")
nd5_mama = binary(nd5, "ma")
nd6_mama = binary(nd6, "ma")
nd7_mama = binary(nd7, "ma")

nd1_dziecko = binary(nd1, "inf")
nd2_dziecko = binary(nd2, "inf")
nd3_dziecko = binary(nd3, "inf")
nd4_dziecko = binary(nd4, "inf")
nd5_dziecko = binary(nd5, "inf")
nd6_dziecko = binary(nd6, "inf")
nd7_dziecko = binary(nd7, "inf")
# d1_dziecko = binary(d1.tierDict["inf"].entryList)
# d2_mama = binary(d2.tierDict["ma"].entryList)
# d2_dziecko = binary(d2.tierDict["inf"].entryList)
# d3_mama = binary(d3.tierDict["ma"].entryList)
# d3_dziecko = binary(d3.tierDict["inf"].entryList)
# d4_mama = binary(d4.tierDict["ma"].entryList)
# d4_dziecko = binary(d4.tierDict["inf"].entryList)
# d5_mama = binary(d5.tierDict["ma"].entryList)
# d5_dziecko = binary(d5.tierDict["inf"].entryList)
# d6_mama = binary(d6.tierDict["ma"].entryList)
# d6_dziecko = binary(d6.tierDict["inf"].entryList)
# d7_mama = binary(d7.tierDict["ma"].entryList)
# d7_dziecko = binary(d7.tierDict["inf"].entryList)

# nd1_mama = binary(nd1.tierDict["ma"].entryList)
# nd1_dziecko = binary(nd1.tierDict["inf"].entryList)
# nd2_mama = binary(nd2.tierDict["ma"].entryList)
# nd2_dziecko = binary(nd2.tierDict["inf"].entryList)
# nd3_mama = binary(nd3.tierDict["ma"].entryList)
# nd3_dziecko = binary(nd3.tierDict["inf"].entryList)
# nd4_mama = binary(nd4.tierDict["ma"].entryList)
# nd4_dziecko = binary(nd4.tierDict["inf"].entryList)
# nd5_mama = binary(nd5.tierDict["ma"].entryList)
# nd5_dziecko = binary(nd5.tierDict["inf"].entryList)
# nd6_mama = binary(nd6.tierDict["ma"].entryList)
# nd6_dziecko = binary(nd6.tierDict["inf"].entryList)
# nd7_mama = binary(nd7.tierDict["ma"].entryList)
# nd7_dziecko = binary(nd7.tierDict["inf"].entryList)

# d1_mama = d1.tierDict["ma"].entryList
# d1_dziecko = d1.tierDict["inf"].entryList
# d2_mama = d2.tierDict["ma"].entryList
# d2_dziecko = d2.tierDict["inf"].entryList
# d3_mama = d3.tierDict["ma"].entryList
# d3_dziecko = d3.tierDict["inf"].entryList
# d4_mama = d4.tierDict["ma"].entryList
# d4_dziecko = d4.tierDict["inf"].entryList
# d5_mama = d5.tierDict["ma"].entryList
# d5_dziecko = d5.tierDict["inf"].entryList
# d6_mama = d6.tierDict["ma"].entryList
# d6_dziecko = d6.tierDict["inf"].entryList
# d7_mama = d7.tierDict["ma"].entryList
# d7_dziecko = d7.tierDict["inf"].entryList
#
# nd1_mama = nd1.tierDict["ma"].entryList
# nd1_dziecko = nd1.tierDict["inf"].entryList
# nd2_mama = nd2.tierDict["ma"].entryList
# nd2_dziecko = nd2.tierDict["inf"].entryList
# nd3_mama = nd3.tierDict["ma"].entryList
# nd3_dziecko = nd3.tierDict["inf"].entryList
# nd4_mama = nd4.tierDict["ma"].entryList
# nd4_dziecko = nd4.tierDict["inf"].entryList
# nd5_mama = nd5.tierDict["ma"].entryList
# nd5_dziecko = nd5.tierDict["inf"].entryList
# nd6_mama = nd6.tierDict["ma"].entryList
# nd6_dziecko = nd6.tierDict["inf"].entryList
# nd7_mama = nd7.tierDict["ma"].entryList
# nd7_dziecko = nd7.tierDict["inf"].entryList

#preparing data to analysis in R
#test
def singleEntryListPreparation(wokalizacja):
	wynik = (wokalizacja.begin,wokalizacja.end)
	return wynik

def entryListPreparation(wokalizacje):
	wynik =[]
	for singleVoc in wokalizacje:
		wynik.append(singleEntryListPreparation(singleVoc))
	return wynik


#st = entryListPreparation(d1_dziecko)

def zapisz(binary_list, katalog, nazwa):
	list_str = "".join(binary_list)
	with open("voc_binary/" + katalog + '/' + nazwa, 'w') as file:
		file.write(list_str)


zapisz(d1_dziecko, "DEP", "d1_dziecko.txt")
zapisz(d2_dziecko, "DEP", "d2_dziecko.txt")
zapisz(d3_dziecko, "DEP", "d3_dziecko.txt")
zapisz(d4_dziecko, "DEP", "d4_dziecko.txt")
zapisz(d5_dziecko, "DEP", "d5_dziecko.txt")
zapisz(d6_dziecko, "DEP", "d6_dziecko.txt")
zapisz(d7_dziecko, "DEP", "d7_dziecko.txt")

zapisz(d1_mama, "DEP", "d1_mama.txt")
zapisz(d2_mama, "DEP", "d2_mama.txt")
zapisz(d3_mama, "DEP", "d3_mama.txt")
zapisz(d4_mama, "DEP", "d4_mama.txt")
zapisz(d5_mama, "DEP", "d5_mama.txt")
zapisz(d6_mama, "DEP", "d6_mama.txt")
zapisz(d7_mama, "DEP", "d7_mama.txt")

zapisz(nd1_dziecko, "NONDEP", "nd1_dziecko.txt")
zapisz(nd2_dziecko, "NONDEP", "nd2_dziecko.txt")
zapisz(nd3_dziecko, "NONDEP", "nd3_dziecko.txt")
zapisz(nd4_dziecko, "NONDEP", "nd4_dziecko.txt")
zapisz(nd5_dziecko, "NONDEP", "nd5_dziecko.txt")
zapisz(nd6_dziecko, "NONDEP", "nd6_dziecko.txt")
zapisz(nd7_dziecko, "NONDEP", "nd7_dziecko.txt")

zapisz(nd1_mama, "NONDEP", "nd1_mama")
zapisz(nd2_mama, "NONDEP", "nd2_mama")
zapisz(nd3_mama, "NONDEP", "nd3_mama")
zapisz(nd4_mama, "NONDEP", "nd4_mama")
zapisz(nd5_mama, "NONDEP", "nd5_mama")
zapisz(nd6_mama, "NONDEP", "nd6_mama")
zapisz(nd7_mama, "NONDEP", "nd7_mama")

x = 1






