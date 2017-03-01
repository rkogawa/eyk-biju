from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse

from accounts.admin import ClienteCreationForm


def criar_usuario(request):
    if request.method == 'POST':
        form = ClienteCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_user = authenticate(username=user.email, password=user.password)
            if auth_user is not None:
                login(request, auth_user)
            #else send an error message

    return HttpResponseRedirect(reverse('pagamentos:finalizar_pedido'))
