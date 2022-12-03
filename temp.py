import pprint
import requests
import pandas as pd


PATH = '/Users/ryan/Documents/vscode/school_gaming/websites.csv'

HEADERS = {
    'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/98.0.4758.109 Safari/537.36 '
}

urls = pd.read_csv(PATH)
urls = urls['websites'].tolist()
pprint.pprint(urls)
print()

def main():

    visits = 0

    for url in urls:
        try:
            response = requests.get(
                url=url,
                headers=HEADERS
            )

            site = url.replace('http://', '')
            visits += 1

            print(visits, response.status_code, site)

        except requests.exceptions.SSLError:
            print("Bad request")


if __name__ == '__main__':
    for i in range(100):
        main()