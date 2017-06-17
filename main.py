from praatio import tgio


def select_speechlike(inf_entries):
    return [entry for entry in inf_entries if entry[2] == 's']

def load_file(filename):
    tg = tgio.openTextgrid(filename)
    for tierDictName, tierDict in tg.tierDict.items():
        for entry in tierDict.entryList:
            if entry[2] not in ['voc', 's', 'ns']:
                raise Exception("Bad entry " + tierDict + " : " + str(entry))
    return tg

tg = load_file('11093_1_voc.TextGrid')
inf_entries = tg.tierDict['inf'].entryList
speechlike = select_speechlike(inf_entries)
assert(speechlike is not None)