from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy A52", "+79001234567"),
    Smartphone("Xiaomi", "Redmi 6 Pro", "+79011234567"),
    Smartphone("HONOR", "V40 5G", "+79021234567"),
    Smartphone("Apple", " iPhone 15 Pro Max", "+79031234567"),
    Smartphone("HUAWEI", "P50 Pro", "+79041234567"),
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
