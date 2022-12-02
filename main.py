import requests
import pandas as pd

data = pd.read_csv('/Users/ryan/Documents/vscode/school_gaming/websites.csv')
data = data['websites'].tolist()
print(data)

visits = 0

def main():
    # Define user agent
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)" 
            "Chrome/107.0.0.0 Safari/537.36"
    }
    

    # Get html code of the website
    for i in data:
        try:
            response = requests.get(
                url = i,
                headers=headers
            )

            site = i.replace('http://', '')
            print(site, response)
            
        except requests.exceptions.SSLError:
            print("Bad request")


if __name__ == '__main__':
    for i in range(100):
        main()
        visits += 1
        print(visits)
