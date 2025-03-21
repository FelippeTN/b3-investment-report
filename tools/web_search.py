import requests
from bs4 import BeautifulSoup


def web_search(url):
    """
    Função de pesquisa na web, onde faz a requisição ao site status invest de acordo com o ativo listado.
    acoes ou fundos-imobiliarios
    """
    url = url
    page_text = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        divs = soup.find_all("div", title=True)

        for div in divs:
            title = div["title"]
            value_tag = div.find("strong", class_="value")

            if value_tag:
                page_text.append((title, value_tag.text.strip()))
                
        return page_text
    
    else:
        print(f"Error, Status Code: {response.status_code}")
        return None