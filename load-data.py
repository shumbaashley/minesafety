import random
import time
import requests


def generate_random_data():
    return {
        "temperature": random.randint(5, 95),
        "humidity": random.randint(5, 95),
        "gas": random.randint(5, 95),
    }


PROD = "https://nigelminesafety.pythonanywhere.com/api/data-readings/"
DEV = "http://localhost:8000/api/data-readings/"

def main():
    while True:
        requests.post(DEV, json=generate_random_data())
        print("Data sent")
        time.sleep(5)


if __name__ == "__main__":
    main()
