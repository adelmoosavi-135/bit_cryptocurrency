import requests
from bs4 import BeautifulSoup 


def _start_init():
    try:
        res = requests.post('https://arzdigital.com/coins/')
        res_d = requests.post('https://arzdigital.com/coins/bitcoin/')
    except:
        return "check".lower()
    
    
    if res.status_code == 200 and res_d.status_code == 200:

        soup_d = BeautifulSoup(res_d.text, 'html.parser')
        soup = BeautifulSoup(res.text, 'html.parser')

        curren = soup.find('td',attrs={'arz-coin-table-circulating-supply-td arz-sort-value'})
        bit_D = soup_d.find('span',attrs={'class':'arz-sana-price'})

        ret_d = [str(curren.text).replace(' میلیونBTC', ''), str(bit_D.text)]
        return ret_d
    elif res.status_code != 200:
        return int(res.status_code)
    elif res_d.status_code != 200:
        return int(res_d.status_code)
