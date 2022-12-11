import requests
from bs4 import BeautifulSoup


def trade_spider():
    url = 'https://bnr.ro/Cursul-de-schimb-524.aspx'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, features="lxml")
    count = 0
    result = dict()
    result[' Leul romanesc'] = float(1)
    table_body = soup.find('table' , {'class' : 'cursTable'}).tbody
    for tr_line in table_body.findAll('tr'):
        count = 0
        key = ''
        value = list()
        for td_item in tr_line.findAll('td'):
            if td_item.text:
                if count == 1 :
                    key = str(td_item.text)
                elif count == 0:
                    value.append(str(td_item.text))  
                else:
                    value.append(float(str(td_item.text).replace(',','.')))  
            count = count + 1       
        result[value[0]] = value[5]    
    return result   
    