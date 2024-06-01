from docxtpl import DocxTemplate, InlineImage
from faker import Faker

fake = Faker('ru_RU')

template = DocxTemplate('../lab_2/lab2_tmp.docx')
signature = InlineImage(template, 'signature.png')
stamp = InlineImage(template, 'stamp.png')


def context_generator(n=1):
    contexts = []
    for i in range(n):
        context = {
            'initials': fake.name(),
            'conscript_address': fake.address(),
            'date': '12.10.2024',
            'time': '13:30',
            'wedding_address': 'ул. Лесная, д. 25, кв. 7',
            'signature': signature,
            'stamp': stamp
        }
        contexts.append(context)
    return contexts


contexts = context_generator()

for context in contexts:
    template.render(context)
    template.save(f"{context['initials'].replace(' ', '_')}.docx")
