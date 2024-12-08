import requests

URL = "http://127.0.0.1:8000/get_form"

test_data = [
    {
        "text": "segwegweg3w",
        "date": "01.01.2000",
    },
    {
        "email": "egwegwe@gmail.com",
        "phone": "+7 999 999 99 99"
    },
    {
        "email": "ewegwegweg@gmail.com",
        "phone": "+7 999 999 99 99",
        "text": "ewgwegwegw",
        "date": "2020-01-01"
    },
    {
        "email": "fewfwegf@gmail.com",
        "phone": "+79999999999",
        "registration_date": "2020-01-01",
        "text": "any text"
    },
    {
        "text": "segwegweg3w",
        "date": "01.01.2000",
        "giga": "mega"
    },
    {
        "email": "fewfwegf@gmail.com",
        "any": "any"
    },
    {
        "any": "any",
        "custom_date": "2020-01-01",
        "custom_email": "fewfwegf@gmail.com",
        "custom_phone": "+79999999999"
    }
]


def send_request(url: str, data: dict) -> requests.Response:
    data = data
    return requests.post(url, data=data)


for d in test_data:
    temp = send_request(URL, d)
    # print("Статус-код:", temp.status_code)
    print("Ответ:", temp.json())
