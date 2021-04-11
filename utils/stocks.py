import http.client
import json

def get_price(symbol):
    "Returns JSON formatted price of a stock. Takes the stock symbol as a parameter."
    conn = http.client.HTTPSConnection("api.iextrading.com")
    conn.request("GET", "/1.0/tops/last?symbols="+symbol)
    res = conn.getresponse()
    data = res.read()
    try:
        return json.loads(data)[0]["price"]
    except IndexError:
        return "Unknown symbol."
