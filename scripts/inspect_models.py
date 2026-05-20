import os, traceback
os.environ['DJANGO_SETTINGS_MODULE'] = 'gestion_stock.settings'
try:
    import django
    django.setup()
    import importlib
    m = importlib.import_module('stock.models')
    print('module file:', m.__file__)
    print('attrs:', [a for a in dir(m) if not a.startswith('_')])
except Exception:
    traceback.print_exc()
