import requests
import json
from decimal import Decimal
from bs4 import BeautifulSoup

class DecimalEncoder(json.JSONEncoder):
   def default(self, o):
       if isinstance(o, Decimal):
           return float(o)
       return super(DecimalEncoder, self).default(o)


headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
url = 'https://www.wellton-towers.ru/flats/?mode=cards'


def price():
  #data
  item = dict(
     complex='Тест',
     type='flat',
     phase=None,
     building=None,
     section=None,
     price_base=None,
     price_finished=None,
     price_sale=None,
     price_finished_sale=None,
     area=None,
     living_area=None,
     number=None,
     number_on_site=None,
     rooms=None,
     floor=None,
     in_sale=None,
     sale_status=None,
     finished=None,
     ceil=None,
     article=None,
     finishing_name=None,
     furniture=None,
     furniture_price=None,
     plan=None,
     feature=None,
     view=None,
     euro_planning=None,
     sale=None,
     discount_percent=None,
     discount=None
  )

  #parsing
  r = requests.get(url, headers=headers, verify=False, timeout=7)
  if r.status_code == 200:
    soup = BeautifulSoup(r.text, 'lxml')
    #obj_on_page = soup.find_all('div', class_='flat-list__list js-flats-filter-container active')
    flats_on_page = soup.find_all('div', class_='flat-card js-flat-card')#.findChildren("div" , cass_='flat-card')
    print(soup)

    #transfer final dict to json
    r = [item]
    out = json.dumps(r, cls=DecimalEncoder, indent=1, sort_keys=False, ensure_ascii=False).encode('utf8').decode()
  elif r.status_code == 404:
    print('Страница не существует!')

if __name__ == "__main__":
  price()
