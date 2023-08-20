from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from pedidos.models import Pedido
from carro.carro import Carro
from pedidos.models import LineaPedido, Pedido
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
# Create your views here.
@login_required(login_url="/autenticacion/logear")
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user)
    carro=Carro(request)
    lineas_pedido=list()
    for key, value in carro.carro.items():
        lineas_pedido.append(lineas_pedido(

            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido


        ))

    LineaPedido.objects.bulk_create(lineas_pedido)
    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.username,
        emailusuario=request.user.email
        )
    messages.success(request, "El pedido a ha creado correcta mente")

    return redirect("../tienda")

def enviar_mail(**kwargs):

    asunto="Grecias por el pedido"
    mensaje=render_to_string("emails/pedodo.html",{
        
        "pedido":kwargs.get("pedido"),
        "lineas_pedido":kwargs.get("lines_pedido"),
        "nombreusuario":kwargs.get("nombreusuario")

    })

    mensaje_texto=strip_tags(mensaje)
    from_email="frptodocell@gmail.com"
    to=kwargs.get("emailusuario")

    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)
