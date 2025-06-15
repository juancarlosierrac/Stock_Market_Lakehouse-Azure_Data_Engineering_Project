import requests
import json
import time
from azure.eventhub import EventHubProducerClient, EventData
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("TWELVE_DATA_API_KEY")
EVENT_HUB_CONNECTION_STR = os.getenv("EVENT_HUB_CONNECTION_STR")
EVENT_HUB_NAME = os.getenv("EVENT_HUB_NAME")

STOCK_SYMBOLS = ["AAPL", "MSFT", "GOOGL", "MELI", "TSLA", "VOO", "QQQ"]

def get_stock_time_series(symbol):
    params = {
        "symbol": symbol,
        "interval": "1min",
        "outputsize": "1",
        "apikey": API_KEY
    }
    url = "https://api.twelvedata.com/time_series"
    resp = requests.get(url, params=params)
    data = resp.json()
    values = data.get("values", [{}])[0]
    meta = data.get("meta", {})
    return {
        "symbol": symbol,
        "timestamp": values.get("datetime"),
        "open": values.get("open"),
        "high": values.get("high"),
        "low": values.get("low"),
        "close": values.get("close"),
        "volume": values.get("volume"),
        "exchange": meta.get("exchange"),
        "currency": meta.get("currency")
    }

def send_to_eventhub(event_data):
    producer = EventHubProducerClient.from_connection_string(
        conn_str=EVENT_HUB_CONNECTION_STR,
        eventhub_name=EVENT_HUB_NAME
    )
    batch = producer.create_batch()
    batch.add(EventData(json.dumps(event_data)))
    producer.send_batch(batch)
    producer.close()

def main():
    while True:
        for symbol in STOCK_SYMBOLS:
            stock_data = get_stock_time_series(symbol)
            print(f"Enviando: {stock_data}")
            send_to_eventhub(stock_data)
        time.sleep(60)

if __name__ == "__main__":
    main()

