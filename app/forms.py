from django import forms
from . models import Product

class MakePost(forms.ModelForm):
    class Meta:
        model=Product
        fields = '__all__'
        labels = {
            'item':'Enter the title',
            'price':"Enter Price",
            'image':'Select Image'
        }