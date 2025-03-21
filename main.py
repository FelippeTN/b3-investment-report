import uvicorn
from api import api
from app.asset_report import *

app = api.app


asset_name, links = url_build()

web_scrapping(asset_name, links)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
