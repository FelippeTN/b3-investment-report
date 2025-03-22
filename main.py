from app.asset_report import *

if __name__ == "__main__":
    asset_name, links = url_build()
    web_scrapping(asset_name, links)
