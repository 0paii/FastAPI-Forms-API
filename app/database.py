from pymongo import MongoClient
from typing import List, Dict
import os

# Настройка подключения к MongoDB
client = MongoClient(os.getenv('MONGO_URI', 'mongodb://localhost:27017/'))
db = client["Forms"]
templates_collection = db["Filled_forms"]


def get_templates() -> List[Dict]:
    """
    Возвращает список шаблонов из MongoDB

    :return: List[Dict]: Шаблоны
    """
    try:
        return list(templates_collection.find())
    except Exception as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return []
