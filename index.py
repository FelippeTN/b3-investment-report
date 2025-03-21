import requests
from bs4 import BeautifulSoup

url = "https://statusinvest.com.br/acoes/klbn4"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    divs = soup.find_all("div", title=True)

    for div in divs:
        titulo = div["title"]
        valor_tag = div.find("strong", class_="value")

        if valor_tag:
            print(f"{titulo}: {valor_tag.text.strip()}")
    
else:
    print(f"Erro ao acessar o site. Código de status: {response.status_code}")
