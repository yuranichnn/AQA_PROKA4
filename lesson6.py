# Задание №1
student = {
    "name": "Yury",
    "age": 40,
    "subjects": ["math", "history", "english"],
    "average_score": 4.5
}

student["average_score"] = 4.75
student["subjects"].append("physics")
del student["age"]
print(f"Словарь выглядет так - {student}")
print("Ключ \"age\" есть") if "age" in student.keys() else print("Ключа \"age\" нет")
print("Ключ \"gender\" есть") if "gender" in student.keys() else print("Ключа \"gender\" нет")
print(f"Все ключи словаря{list(student.keys())}")
print(f"Все значения словаря{list(student.values())}")

# Задание №2
response = {
    "cartButtonEnabled": True,
    "conditions": {
        "campaign": {
            "id": "unlimited_burn_99rub_prd",
            "info": "Доставка в пункт выдачи от",
            "link": "https://support.avito.ru/articles/2369"
        },
        "destination": "по Дзержинску",
        "discount": 900,
        "minDays": 1,
        "price": 99,
        "terms": "От 1 дня, от",
        "trustfactors": [
            {
                "helpIcon": False,
                "icon": "cod",
                "label": "",
                "text": "Можно оплатить при получении"
            }
        ]
    },
    "services": [
        {
            "available": True,
            "enabled": True,
            "type": "delivery"
        },
        {
            "available": True,
            "enabled": True,
            "type": "deliveryCourier"
        },
        {
            "available": False,
            "enabled": False,
            "type": "deliveryCourierD2D"
        },
    ]
}
print(response["conditions"]["trustfactors"][0]["icon"])
print(response["conditions"]["campaign"]["id"])
print(response["conditions"]["trustfactors"][0]["helpIcon"] is False)
print(response["services"][2]["type"])
