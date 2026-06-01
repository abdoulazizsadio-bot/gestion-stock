import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestion_stock.settings')
django.setup()
from django.template.loader import render_to_string

rendered = render_to_string('registration/logged_out.html', {'user': None, 'messages': []})
print(rendered[:500])
print('LEN', len(rendered))
