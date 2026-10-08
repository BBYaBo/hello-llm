import requests


def main():
    url = "https://httpbin.org/json"
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()
    print("请求成功")
    print(data)


if __name__ == "__main__":
    main()