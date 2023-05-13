from rest_framework.serializers import ModelSerializer
 
from magasin.models import Categorie
from magasin.models import Produit
class CategorySerializer(ModelSerializer):
 
    class Meta:
        model = Categorie
        fields = ['id', 'name']
        
class ProduitSerializer(ModelSerializer):
    model = Produit
    fields = ['id', 'name', 'description', 'id_categorie']