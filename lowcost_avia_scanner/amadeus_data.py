import requests
import json
from config import API_KEY, API_SECRET, TOKEN_URL, FLIGHT_OFFERS_URL, FLIGHT_OFFERS_SAVED, FLIGHT_OFFERS_OUTPUT

class AmadeusClient:
    def __init__(self):
        self.api_key = API_KEY
        self.api_secret = API_SECRET
        self.token_url = TOKEN_URL
        self.flight_offers_url = FLIGHT_OFFERS_URL
        self.saved_file = FLIGHT_OFFERS_SAVED
        self.output_file = FLIGHT_OFFERS_OUTPUT

    def fetch_flight_offers_from_api(self):
        """
        Отримує дані про пропозиції рейсів з API Amadeus і зберігає їх у файли.
        """
        # Отримання токена
        payload = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        response = requests.post(url=self.token_url, data=payload, headers=headers)

        if response.status_code != 200:
            print(f"Помилка при отриманні токена: {response.status_code}, {response.text}")
            return None

        token_data = response.json()
        access_token = token_data["access_token"]
        print(f"Access Token: {access_token}")

        # Збереження токена
        try:
            with open("save_token.txt", mode="w") as file:
                json.dump(token_data, file, indent=4)
            print(f"Токен збережено у save_token.txt")
        except Exception as e:
            print(f"Помилка при збереженні токена: {str(e)}")

        # Запит до API для отримання пропозицій рейсів
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        response = requests.get(self.flight_offers_url, headers=headers)

        if response.status_code != 200:
            print(f"Помилка при виклику API: {response.status_code}, {response.text}")
            return None

        flight_data = response.json()

        # Збереження результату у FLIGHT_OFFER_SAVED.json
        try:
            with open(self.saved_file, mode="w") as file:
                json.dump(flight_data, file, indent=4)
            print(f"Дані збережено у {self.saved_file}")
        except Exception as e:
            print(f"Помилка при збереженні у {self.saved_file}: {str(e)}")

        # Збереження результату у FLIGHT_OFFER.txt
        try:
            with open(self.output_file, mode="w") as file_offer:
                json.dump(flight_data, file_offer, indent=4)
            print(f"Дані збережено у {self.output_file}")
        except Exception as e:
            print(f"Помилка при збереженні у {self.output_file}: {str(e)}")

        return flight_data

    def read_flight_offers_from_file(self):
        """
        Читає дані з локального JSON-файлу і зберігає їх у FLIGHT_OFFER.txt.
        """
        try:
            with open(self.saved_file, 'r') as file:
                flight_data = json.load(file)
            # print("Дані про пропозиції рейсів:", flight_data)

            # Збереження даних у FLIGHT_OFFER.txt
            with open(self.output_file, mode="w") as file_offer:
                json.dump(flight_data, file_offer, indent=4)
            print(f"Дані успішно збережено у {self.output_file}")

            return flight_data

        except FileNotFoundError:
            print(f"Помилка: Файл {self.saved_file} не знайдено")
            return None
        except json.JSONDecodeError:
            print(f"Помилка: Некоректний формат JSON у файлі {self.saved_file}")
            return None
        except Exception as e:
            print(f"Помилка при обробці файлу: {str(e)}")
            return None