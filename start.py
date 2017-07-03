from praatio import tgio
from collections import namedtuple

Entry = namedtuple('Entry', ['begin', 'end', 'tag'])

def select_speechlike(inf_entries):
    return [entry for entry in inf_entries if entry.tag == 's']  # list comprehension


def select_nonspeechlike(inf_entries):
    return [entry for entry in inf_entries if entry.tag == 'ns']


def load_file(filename):
    tg = tgio.openTextgrid(filename)
    for tierDictName, tierDict in tg.tierDict.items():
        new_entry_list = []
        for entry in tierDict.entryList:
            if entry[2] not in ['voc', 's', 'ns']:  # check if correct inside tiers names
                raise Exception("Bad entry " + tierDictName + " : " + str(entry))
            new_entry_list.append(Entry(entry[0], entry[1], entry[2]))
        tierDict.entryList = new_entry_list
    return tg


def count_times(list):
    counted = []
    for tuple in list:
        t0 = tuple.begin
        t1 = tuple.end
        t = t1 - t0
        counted.append(t)
    return counted


def count_total_time(counted):
    total = 0
    for single_time in counted:
        total += single_time
    return total


tg = load_file('11093_1_voc.TextGrid')

inf_entries = tg.tierDict['inf'].entryList
mother_voc = tg.tierDict['ma'].entryList
infant_s = select_speechlike(inf_entries)
infant_ns = select_nonspeechlike(inf_entries)
infant_ns_times = count_times(infant_ns)
infant_ns_total_time = count_total_time(infant_ns_times)
infant_s_times = count_times(infant_s)
infant_s_total_time = count_total_time(infant_s_times)

inf_entries_times = count_times(inf_entries)
inf_entries_total_time = count_total_time(inf_entries_times)




# for i in inf_entries_times:
#     print(i)
# assert (speechlike is not None)
