from django.test import TestCase
from .services import scrape_mercadolibre
from .etl import analyze_data

class ScrapingTests(TestCase):
    def test_scrape_mercadolibre(self):
        results = scrape_mercadolibre('laptop')
        self.assertTrue(len(results) > 0)
        self.assertIn('title', results[0])
        self.assertIn('price', results[0])

    def test_analyze_data(self):
        data = [
            {"title": "Item 1", "price": "1000", "url": "", "image": ""},
            {"title": "Item 2", "price": "2000", "url": "", "image": ""},
            {"title": "Item 3", "price": "1500", "url": "", "image": ""}
        ]
        analysis = analyze_data(data)
        self.assertEqual(analysis['min_price']['title'], "Item 1")
        self.assertEqual(analysis['max_price']['title'], "Item 2")
