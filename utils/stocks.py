import http.client

def get_price(symbol):
    "Returns JSON formatted price of a stock. Takes the stock symbol as a parameter."
    conn = http.client.HTTPSConnection("api.iextrading.com")
    conn.request("GET", "/1.0/tops/last?symbols="+symbol)
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")
