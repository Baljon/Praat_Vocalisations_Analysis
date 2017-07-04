from response import *

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

    def test_ile_odpowiedzi_na_speechlike(self):
        self.assertEquals(ileOdpowiedziNaSpeechlike(self.tg), 18)

    def test_ile_odpowiedzi_na_nonspeechlike(self):
        self.assertEquals(ileOdpowiedziNaNonSpeechlike(self.tg), 6)

    def test_contingency(self):
        self.assertEquals(contingency(self.tg, 0.5), -0.275)
        self.assertEquals(contingency(self.tg), -0.4125)
        self.assertEquals(contingency(self.tg, 2), -0.6875)

    def test_previous_contigency(self):
        self.assertAlmostEqual(previous_contigency(self.tg, 0.5), 0.0592, 3)
        self.assertAlmostEqual(previous_contigency(self.tg), 0.0457, 3)
        self.assertAlmostEqual(previous_contigency(self.tg, 2), -0.1142, 3)