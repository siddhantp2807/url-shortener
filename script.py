import sqlite3
import secrets as sc
import requests


class URLShortener:
    def __init__(self, url):
        self.url = url
        
    def urlValidator(self):
        try:
            res = requests.get(self.url)
            return True
        except:
            return False

    def genkey(self):
        if self.urlValidator():
            self.sUrl = sc.token_urlsafe(6)
        else:
            return None

        return self

    
def verifyGenerateAdd(url, dbAddress = 'keys.db') :
    conn = sqlite3.connect(dbAddress)
    c = conn.cursor()

    with conn :
        c.execute("""CREATE TABLE IF NOT EXISTS keys (
            url TEXT,
            sUrl TEXT
            )""")
        c.execute("SELECT * FROM keys WHERE url = (?)", (url, ))
    x = c.fetchone()
    if x :
        return {'url' : x[0], 'sUrl' : x[1]}
        
        
    while True :
        sUrl = URLShortener(url).genkey()
        if sUrl :      
            with conn :      
                c.execute("SELECT * FROM keys WHERE sUrl = (?)", (sUrl.sUrl, ))
            y = c.fetchone()
            if y :
                continue
            else : 
                with conn :
                    c.execute("INSERT INTO keys VALUES (:url, :sUrl)", sUrl.__dict__)
                
                return sUrl.__dict__
        else :
            return None


def find(sUrl, dbAddress = 'keys.db') :
    conn = sqlite3.connect(dbAddress)
    c = conn.cursor()
    with conn:
        c.execute("SELECT * FROM keys WHERE sUrl = (?)", (sUrl, ))
    x = c.fetchone()
    if x:
        return {'url': x[0], 'sUrl': x[1]}
    else :
        return None



