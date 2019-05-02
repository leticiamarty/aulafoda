from django import forms 
from loja.models import Pedido

class Pedidoform(forms.ModelForm):
    class Meta:   # class dentro da classe tipo ter um humano e ele ser brasileiro
        model = Pedido
        fields =[
            'nome',
            'email',
            'endereco',
            'cartao',
            'pagamento',
        ]

# a pessoa vai reencher as coisas por exemplo cabelo=loira, olhos= azul
