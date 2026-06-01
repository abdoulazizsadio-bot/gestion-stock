from django.db import models


class Produit(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantite = models.IntegerField()

    def __str__(self):
        return self.nom


class Commande(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite_commandee = models.IntegerField()
    date_commande = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commande de {self.quantite_commandee} {self.produit.nom} le {self.date_commande}"
