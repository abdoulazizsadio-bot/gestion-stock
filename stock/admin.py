from django.contrib import admin
from .models import Commande, Produit

admin.site.register(Produit)
admin.site.register(Commande)
