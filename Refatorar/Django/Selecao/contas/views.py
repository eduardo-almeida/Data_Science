from django.shortcuts import render
from .models import Transacao
from .form import TransacaoForm
import datetime

def home(request):
    data = {}
    data['trasacoes'] = ["t1", "t2", "t3"]
    data['now'] = datetime.datetime.now()
    #html = "<html>A hora é %s</html>" % now
    #return HttpResponse(html)
    return render(request, 'contas/home.html', data)

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)

def nova_transacao(request):
    form = TransacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return listagem(request)
    return render(request, 'contas/form.html', {'form': form})