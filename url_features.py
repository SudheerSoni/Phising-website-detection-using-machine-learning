import tldextract
import whois
import requests
from bs4 import BeautifulSoup
import re

def extract_features(url):
    features = []
    
    # URL length
    features.append(len(url))
    
    # Hostname length
    ext = tldextract.extract(url)
    features.append(len(ext.domain + '.' + ext.suffix))
    
    # IP address
    try:
        ip_address = socket.gethostbyname(ext.domain + '.' + ext.suffix)
        features.append(1)
    except:
        features.append(-1)
    
    # Number of dots, hyphens, at symbols, question marks, ampersands,vertical bar, equal signs, underscores, tildes, percent signs, slashes, Asterisk, colons, commas, semicolons, dollar signs, spaces, 'www', 'com', double slashes
    features.append(url.count('.'))
    features.append(url.count('-'))
    features.append(url.count('@'))
    features.append(url.count('?'))
    features.append(url.count('&'))
    features.append(url.count('|'))
    features.append(url.count('='))
    features.append(url.count('_'))
    features.append(url.count('~'))
    features.append(url.count('%'))
    features.append(url.count('/'))
    features.append(url.count('*'))
    features.append(url.count(':'))
    features.append(url.count(','))
    features.append(url.count(';'))
    features.append(url.count('$'))
    features.append(url.count(' '))
    features.append(1 if 'www' in url else 0)
    features.append(1 if '.com' in url else 0)
    features.append(url.count('//'))
    
    # Domain age
    try:
        domain = ext.domain + '.' + ext.suffix
        w = whois.whois(domain)
        creation_date = w.creation_date
        if type(creation_date) == list:
            creation_date = creation_date[0]
        delta = (creation_date - datetime.datetime.now()).days
        features.append(delta)
    except:
        features.append(-1)
    
    # Web traffic
    try:
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html.parser')
        script = soup.find('script', string=re.compile('ALEXA'))
        if script:
            rank = int(re.search(r'\d+', script.string).group())
           # if rank < 100000:
            features.append(rank)
           # else:
             #   features.append(0)
        else:
            features.append(-1)
    except:
        features.append(0)
    
    # DNS record
    try:
        w = whois.whois(ext.domain + '.' + ext.suffix)
        features.append(int(bool(w.domain_name)))
        print("dns number ",int(bool(w.domain_name)))
    except:
        features.append(0)

    
    # Google index
    try:
        html = requests.get(f'https://www.google.com/search?q=site:{ext.domain + "." + ext.suffix}').text
        if 'did not match any documents' in html:
            features.append(1)
        else:
            features.append(0)
    except:
        features.append(-1)
    
    return features
