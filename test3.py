# encode: utf-8
""" By Daath """


update = {
    'name': 123
}


def add(x=None):
    x = x or {}
    x['no1'] = 456


add(update)
print update
