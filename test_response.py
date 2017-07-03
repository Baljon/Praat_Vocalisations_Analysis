from response import czyOdpowiedzMamy, ileOdpowiedziNaSpeechlike

__author__ = 'Anna'

from unittest import TestCase
from start import load_file, select_speechlike, select_nonspeechlike, count_times, count_total_time


class TestResponse(TestCase):
    def setUp(self):
            self.tg = load_file('11093_1_voc.TextGrid')

    def test_czy_odpowiedz_mamy(self):
        odpowiedz = select_speechlike(self.tg.tierDict['inf'].entryList)[2]
        brak =  self.tg.tierDict['inf'].entryList[4]
        self.assertEquals(czyOdpowiedzMamy(odpowiedz, self.tg), True)
        self.assertEquals(czyOdpowiedzMamy(brak, self.tg), False)

    def test_ile_odpowiedzi(self):
        self.assertEquals(ileOdpowiedziNaSpeechlike(self.tg), 18)