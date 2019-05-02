from django.db import models

# Create your models here. 

#isso cria caracteristicas de coisas por exemplo coisas dessa classe tem que ter nome preco 
#se fosse class humano cada "coisa" seria uma pessoa que teria olhos cabelos perna braco...

class Produto (models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(decimal_places=200, max_digits=200)
    descricao = models.TextField(blank=True, null=True)
    em_estoque = models.BooleanField(default=True)
#aqui e tipo vc  escolhe oque vc quer por outras palavras
#tipo rv rovailes (rv) significa rotvailer
    def __str__(self):
        return self.none


class Pedido(models.Model):
    pagamento_a_vista = 'av'
    pagamento_2x = 'p2'
    pagamento_3x = 'p3'
    pagamento_4x = 'p4'
    pagamento_5x = 'p5'
# aqui sao por exemplos opcoes pessoa magra gorda ...
    pagamento_opcoes = [
        (pagamento_a_vista, 'Pagamento à vista'),
        (pagamento_2x, 'Parcelado em 2 vezes'),
        (pagamento_3x, 'Parcelado em 3 vezes'),
        (pagamento_4x, 'Parcelado em 4 vezes'),
        (pagamento_5x, 'Parcelado em 5 vezes')
    ]
#aqui seria a definicao por exemplo  uma pessoa com cabelo preto, dois olhos no maximo ...
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    endereco = models.CharField(max_length=150)
    cartao = models.IntegerField()
    pagamento = models.CharField(max_length=2, choices=pagamento_opcoes)

    def __str__(self):
        return self.nome