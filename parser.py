import json
from decimal import Decimal


class DecimalEncoder(json.JSONEncoder):
   def default(self, o):
       if isinstance(o, Decimal):
           return float(o)
       return super(DecimalEncoder, self).default(o)


def price():
   item = dict(
       complex='Тест',
       type='flat',
       phase=None,
       building=33,
       section='2',
       price_base=Decimal(9000000),
       price_finished=Decimal(10000000),
       price_sale=None,
       price_finished_sale=None,
       area=47.4,
       living_area=20.5,
       number='45',
       number_on_site=None,
       rooms=2,
       floor=14,
       in_sale=1,
       sale_status='в продаже',
       finished='optional',
       ceil=Decimal(3.1),
       article='17Т-4.2',
       finishing_name='White box',
       furniture=None,
       furniture_price=None,
       plan='https://lidgroup.ru/upload/iblock/ac4/ac45a68ec7946d69e39f0e64a9e00591/77b0bd53b77ebe6dca1ed23317b74fee.jpg',
       feature=['ванная с окном', 'с балконом'],
       view=['на Москву', 'на реку'],
       euro_planning=1,
       sale=None,
       discount_percent=None,
       discount=None
   )
   r = [item]
   out = json.dumps(r, cls=DecimalEncoder, indent=1, sort_keys=False, ensure_ascii=False).encode('utf8').decode()
   print(out)

if __name__ == "__main__":
  price()
