import requests

def get_country_info(country_name):
    url = f"https://countries.dev/name/{country_name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if not data:
            print("Country not found.")
            return

        country = data[0]

        print(f"Name: {country['name']}")
        print(f"Capital: {country['capital']}")
        print(f"Region: {country['region']}")

        borders = country.get('borders', [])
        print(f"Borders: {borders if borders else 'None'}")
        print(f"Population: {country['population']}")

        print("Currencies:")
        for currency in country['currencies']:
            print(f"  - {currency['name']} ({currency['code']})")

        print("Languages:")
        for language in country['languages']:
            print(f"  - {language['name']}")

        print(f"Flag: {country['flag']}")
    else:
        print("Country not found.")

while True:
    country_name = input("Enter a country name (or 'quit' to exit): ")
    if country_name.lower() == "quit":
        break
    get_country_info(country_name)




