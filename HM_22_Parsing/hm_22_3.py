import yaml
from pprint import pprint

with open('order.yaml') as f:
    templates = yaml.safe_load(f)

# номер заказа
order_number = templates['invoice']
pprint(order_number)

# адрес доставки
delivery_address = templates['ship-to']
pprint(delivery_address)

# описание посылки, ее стоимость и количество
print("Total price: ", templates['total'])
print("all products len: ", len(templates['product']))
print("")
num = 0
for product in templates['product']:
    num += 1
    print('product: ', num)
    print("Description: ", product['description'])
    print("Price by item: ", product['price'])
    print("Quantity: ", product['quantity'])
    print("Total price by product: ", product['price'] * product['quantity'])
    print("")
