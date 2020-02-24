import requests
from bs4 import BeautifulSoup

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
url = 'https://www.wellton-towers.ru/'
#url = 'https://github.com/psf/requests/issues/4256'


def price():
  r = requests.get(url, headers=headers, verify=False, timeout=7)
  if r.status_code == 200:
    soup = BeautifulSoup(r.text, 'lxml')

  elif r.status_code == 404:
    print('Страница не существует!')

if __name__ == "__main__":
  price()
