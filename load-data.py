import random
import time
import requests


def generate_random_data():
    return {
        "temperature": random.randint(5, 95),
        "humidity": random.randint(5, 95),
        "gas": random.randint(5, 95),
    }


def main():
    while True:
        requests.post("http://localhost:8000/api/", json=generate_random_data())
        print("Data sent")
        time.sleep(5)


if __name__ == "__main__":
    main()
