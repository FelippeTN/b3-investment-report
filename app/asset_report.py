from tools.groq_config import groq_call
from tools.web_search import web_search
from tools.email_sender import send_email
import pandas as pd

def url_build():
    url = "https://statusinvest.com.br/"
    links = []
    asset_name = []
    
    data = pd.read_csv('./data/assets.csv', sep=',')
    for k, v in zip(data['type'], data['asset']):
        complete_url = f"{url}{k}/{v}"
        links.append(complete_url)
        asset_name.append(v)
        complete_url = []
    
    return asset_name, links
        
def web_scrapping(asset_name, links):
    x = 0
    if not links:
        print("Empty link list.")
        return None
    
    try:
        for link in links:
            print(asset_name[x], link)
            result = web_search(link)
            bot_response = groq_call(asset_name[x], result)
            send_email(bot_response)
            x=+1
        
    except:
        print('Deu ruim nesse CARAAAAI!')
        

            
        
        

