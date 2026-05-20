from django.contrib import admin
from .models import Produit, Commande

# Register models for admin site
admin.site.register(Produit)
admin.site.register(Commande)
