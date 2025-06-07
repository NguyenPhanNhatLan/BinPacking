import pandas as pd
from models.item import Item
import os

def load_items_from_excel(filepath):
    df = pd.read_excel(filepath)
    items = []
    for _, row in df.iterrows():
        item = Item(
            sku=row['sku'],
            name=row['name'],
            category=row.get('category', 'default'),
            length=row['length'],
            width=row['width'],
            height=row['height'],
            volume=row['volume'],
            weight=row['weight'],
            value=row['value'],
            fragile=row.get('fragile', False),
            sensitive=row.get('sensitive', False),
            priority=row.get('priority', 0),
            quantity=row.get('quantity', 1),
            is_dangerous=row.get('is_dangerous', False),
            max_stack=row.get('max_stack', 1)
        )
        items.append(item)
    return items
