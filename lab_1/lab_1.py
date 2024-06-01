import random

from docxtpl import DocxTemplate


def product_generator(n=15):
    products = []
    for i in range(n):
        amount = random.randint(1, 1000)
        price = random.randint(1, 100000)
        product = {
            'title': f'Продукт {i+1}',
            'code': str(random.randint(100, 999)),
            'unit': random.choice(['л', 'кг', 'шт']),
            'amount': amount,
            'price': price,
            'sum': amount * price
        }
        products.append(product)
    return products


def context_generator():
    products = product_generator()
    context = {
        'company': 'Компания',
        'check_number': str(random.randint(1, 10000000)),
        'day': str(random.randint(1, 30)),
        'month': random.choice([
            "Январь",
            "Февраль",
            "Март",
            "Апрель",
            "Май",
            "Июнь",
            "Июль",
            "Август",
            "Сентябрь",
            "Октябрь",
            "Ноябрь",
            "Декабрь"
        ]),
        'year': '22',
        'seller': random.choice([
            "Иванов А. Б.",
            "Петров В. Г.",
            "Сидоров Д. Е.",
            "Кузнецов Ж. З.",
            "Смирнов И. К."
        ]),
        'address': "г. Москва, ул. Ленина, д. 25, кв. 12",
        'ORGN': "1037700123456",
        'products': products,
        'general_sum': str(sum(product['sum'] for product in products)) + ' руб.'
    }
    return context


receipts_cnt = 1
contexts = [context_generator() for _ in range(receipts_cnt)]
template = DocxTemplate("tmp.docx")

for j in range(receipts_cnt):
    template.render(contexts[j])
    template.save(f'././receipt{j + 1}.docx')
