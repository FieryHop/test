import os

import pandas as pd
from django.test import TestCase
from items.tasks import import_items

import os

import pandas as pd
from django.test import TestCase
from items.tasks import import_items

class TestImportItems(TestCase):
    def test_import_items(self):
        os.makedirs('data', exist_ok=True)
        data = [
            {'name': 'Test1', 'category': 'TestCat', 'price': 100, 'updated_at': '2025-11-11'},
            {'name': 'Test2', 'category': 'Food', 'price': 50, 'updated_at': '2025-11-10'},
            {'name': 'Test3', 'category': 'Food', 'price': 30, 'updated_at': '2025-11-09'},
            {'name': 'Test4', 'category': 'Electronics', 'price': 200, 'updated_at': '2025-11-08'},
            {'name': 'Test5', 'category': 'Books', 'price': 15, 'updated_at': '2025-11-07'}
        ]
        df = pd.DataFrame(data)
        df.to_csv('data/test.csv', index=False)

