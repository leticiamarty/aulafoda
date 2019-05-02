from django.shortcuts import render
from loja.forms import Pedidoform
# Create your views here.

def fazer_pedido(request):
    formulario =  Pedidoform(request.POST or None)
    msg = ""

    if formulario.is_valid():
        formulario.save()
        formulario = Pedidoform()
        msg = 'pedido realizado com sucesso'


    contexto = {
        'form': formulario,
        'msg' : msg
    }


    return render(request, 'index.html', contexto) # tem que por contexto pra ele mmostrar e se caso vc quiser mudar alguma coisa pelo front ele manda para o nack

#render é carregar  aparecer