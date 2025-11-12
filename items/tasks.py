import pandas as pd
from celery import shared_task
from .models import Item


@shared_task
def import_items():
    local_path = '/app/data/test.csv'  # путь к локальному файлу

    # Читаем напрямую из локального файла
    df = pd.read_csv(local_path)

    df = df.rename(columns={"Имя": "name", "Категория": "category", "Цена": "price", "Обновлён": "updated_at"})

    for _, row in df.iterrows():
        Item.objects.update_or_create(
            name=row['name'], category=row['category'],
            defaults={'price': row['price'], 'updated_at': row['updated_at']}
        )
    print("import completed")