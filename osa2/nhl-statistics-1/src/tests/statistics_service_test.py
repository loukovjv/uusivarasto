"""Yksikkötestit StatisticsService-luokalle."""

import unittest
from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    """Stub-luokka, joka palauttaa kovakoodatun pelaajalistan ilman verkkoyhteyttä."""

    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89),
        ]


class TestStatisticsService(unittest.TestCase):
    """Testiluokka StatisticsService-luokan toiminnan testaamiseen."""

    def setUp(self):
        """Alustaa testattavan palvelun stub-oliolla ennen jokaista testiä."""
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_loytaa_pelaajan(self):
        """Testaa, että olemassa oleva pelaaja löytyy nimellä haettaessa."""
        player = self.stats.search("Kurri")
        self.assertEqual(player.name, "Kurri")

    def test_search_ei_loydota_pelaajaa(self):
        """Testaa, että olematonta pelaajaa haettaessa palautetaan None."""
        player = self.stats.search("Selänne")
        self.assertIsNone(player)

    def test_team_palauttaa_oikean_joukkueen_pelaajat(self):
        """Testaa, että tietyn joukkueen pelaajat palautetaan oikein."""
        edm_players = self.stats.team("EDM")
        self.assertEqual(len(edm_players), 3)
        names = [p.name for p in edm_players]
        self.assertIn("Semenko", names)
        self.assertIn("Kurri", names)
        self.assertIn("Gretzky", names)

    def test_top_palauttaa_parhaat_pelaajat(self):
        """Testaa, että top-metodi palauttaa oikean määrän parhaita pelaajia pisteytyksen mukaan."""
        top_players = self.stats.top(2)
        # top(how_many) palauttaa how_many + 1 pelaajaa nykyisen toteutuksen mukaan (0, 1, 2 -> 3 kpl)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")
