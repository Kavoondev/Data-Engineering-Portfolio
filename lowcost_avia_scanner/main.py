from amadeus_data import AmadeusClient

def main():
    # Ініціалізація клієнта
    amadeus = AmadeusClient()

    # Для розробки: читаємо з локального файлу
    # flight_data = amadeus.read_flight_offers_from_file()

    # Для продакшену: розкоментувати цей рядок, а попередній закоментувати
    flight_data = amadeus.fetch_flight_offers_from_api()

    if flight_data:
        print("Операція успішна, дані отримано")
    else:
        print("Не вдалося отримати дані")

if __name__ == "__main__":
    main()