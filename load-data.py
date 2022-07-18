import random
import time
import requests


def generate_random_data():
    return {
        "temperature": random.randint(13, 24),
        "humidity": random.randint(90, 99),
        "gas": random.randint(5, 95),
    }


# URL = "https://nigelminesafety.pythonanywhere.com/api/data-readings/"
URL = "http://localhost:8000/api/data-readings/"

def main():
    while True:
        requests.post(URL, json=generate_random_data())
        print("Data sent")
        time.sleep(5)


if __name__ == "__main__":
    main()
