import json
from app.database import templates_collection, client
from pathlib import Path



db_data_path = Path(__file__).parent / 'db_load.json'

try:
    with open(db_data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if data:
        templates_collection.insert_many(data)
    print("Данные успешно загружены")
except Exception as e:
    print(e)

client.close()
