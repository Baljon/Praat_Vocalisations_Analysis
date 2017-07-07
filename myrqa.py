import bisect
from response import d1, d2, d3, d4, d5, d6, d7
from response import nd1, nd2, nd3, nd4, nd5, nd6, nd7


def binary(wokalizacje, okno=0.25, prog_ciszy=0.5):
	current = wokalizacje[0].begin
	end = wokalizacje[-1].end
	binary_list = []
	while current < end:
		nearest_voc = znajdz_najblizsza_po_czasie(wokalizacje, current)
		if nearest_voc is None:
			binary_list.append(0)
		elif nearest_voc.begin > current + okno:
			binary_list.append(0)
		# ilosc czasu zajetego przez wokalizacje wzgledem okno
		elif (nearest_voc.begin - current) / okno > prog_ciszy:
			binary_list.append(0)
		else:
			binary_list.append(1)
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

d1_mama = binary(d1.tierDict["ma"].entryList)
d1_dziecko = binary(d1.tierDict["inf"].entryList)
d2_mama = binary(d2.tierDict["ma"].entryList)
d2_dziecko = binary(d2.tierDict["inf"].entryList)
d3_mama = binary(d3.tierDict["ma"].entryList)
d3_dziecko = binary(d3.tierDict["inf"].entryList)
d4_mama = binary(d4.tierDict["ma"].entryList)
d4_dziecko = binary(d4.tierDict["inf"].entryList)
d5_mama = binary(d5.tierDict["ma"].entryList)
d5_dziecko = binary(d5.tierDict["inf"].entryList)
d6_mama = binary(d6.tierDict["ma"].entryList)
d6_dziecko = binary(d6.tierDict["inf"].entryList)
d7_mama = binary(d7.tierDict["ma"].entryList)
d7_dziecko = binary(d7.tierDict["inf"].entryList)

nd1_mama = binary(nd1.tierDict["ma"].entryList)
nd1_dziecko = binary(nd1.tierDict["inf"].entryList)
nd2_mama = binary(nd2.tierDict["ma"].entryList)
nd2_dziecko = binary(nd2.tierDict["inf"].entryList)
nd3_mama = binary(nd3.tierDict["ma"].entryList)
nd3_dziecko = binary(nd3.tierDict["inf"].entryList)
nd4_mama = binary(nd4.tierDict["ma"].entryList)
nd4_dziecko = binary(nd4.tierDict["inf"].entryList)
nd5_mama = binary(nd5.tierDict["ma"].entryList)
nd5_dziecko = binary(nd5.tierDict["inf"].entryList)
nd6_mama = binary(nd6.tierDict["ma"].entryList)
nd6_dziecko = binary(nd6.tierDict["inf"].entryList)
nd7_mama = binary(nd7.tierDict["ma"].entryList)
nd7_dziecko = binary(nd7.tierDict["inf"].entryList)


x = 1






