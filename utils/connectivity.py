import urllib.request

# Connectivity check
def internet():
    try:
        urllib.request.urlopen('http://google.com')
        return True
    except:
        return False
