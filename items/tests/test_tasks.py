import os

import pandas as pd
from django.test import TestCase
from items.tasks import import_items

class TestImportItems(TestCase):
    def test_import_items(self):
        os.makedirs('data', exist_ok=True)
        df = pd.DataFrame([{'name': 'Test', 'category': 'TestCat', 'price': 100, 'updated_at': '2025-11-11'}])
        df.to_csv('data/test.csv', index=False)

        # import_items()
        #
        # # Проверяем, что данные сохранены корректно, например:
        # from items.models import Item
        # item = Item.objects.get(name='Test')
        # self.assertEqual(item.category, 'TestCat')
        # self.assertEqual(item.price, 100)
        # self.assertEqual(str(item.updated_at.date()), '2025-11-11')