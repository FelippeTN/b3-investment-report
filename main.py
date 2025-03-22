import datetime, time, pytz, schedule
from app.asset_report import *

brt = pytz.timezone('America/Sao_Paulo')

def perform_task():
    now = datetime.datetime.now(brt).strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{now}] Performing Task...")
    asset_name, links = url_build()
    web_scrapping(asset_name, links)

schedule.every().day.at("09:00").do(perform_task)

while True:
    schedule.run_pending()
    time.sleep(60)  