from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from .forms import PlanoForm, TopicoForm, AdicionalForm, AcaoForm, BibliotecaForm
from .models import Plano, Topico, Adicional, Acao, Biblioteca

def index(request):
    # Carrega a página principal
    return render(request, 'index.html')

def municipio(request, municipio):
    # Busca os planos existentes para o município
    planos = Plano.objects.filter(municipio=municipio)
    context = {'municipio': municipio, 'planos': planos}
    return render(request, 'municipio.html', context)

# def criar_plano(request, municipio):
#     # Criar formsets para cada tipo de form que você está usando
#     TopicoFormSet = modelformset_factory(Topico, form=TopicoForm, extra=1)
#     AdicionalFormSet = modelformset_factory(Adicional, form=AdicionalForm, extra=1)
#     AcaoFormSet = modelformset_factory(Acao, form=AcaoForm, extra=1)
#     BibliotecaFormSet = modelformset_factory(Biblioteca, form=BibliotecaForm, extra=1)

#     if request.method == 'POST':
#         # Instanciar os formulários com os dados da requisição POST
#         form = PlanoForm(request.POST)
#         formset_topico = TopicoFormSet(request.POST, request.FILES, queryset=Topico.objects.none(), prefix='topico')
#         formset_adicional = AdicionalFormSet(request.POST, request.FILES, queryset=Adicional.objects.none(), prefix='adicional')
#         formset_acao = AcaoFormSet(request.POST, queryset=Acao.objects.none(), prefix='acao')
#         formset_biblioteca = BibliotecaFormSet(request.POST, request.FILES, queryset=Biblioteca.objects.none(), prefix='biblioteca')

#         # Verificar se todos os formulários são válidos
#         if form.is_valid() and formset_topico.is_valid() and formset_adicional.is_valid() and formset_acao.is_valid() and formset_biblioteca.is_valid():
#             # Salvar o formulário principal (PlanoForm)
#             plano = form.save(commit=False)
#             plano.municipio = municipio
#             plano.save()

#             # Salvar os dados relacionados usando os formsets
#             for form in formset_topico:
#                 topico = form.save(commit=False)
#                 topico.plano = plano
#                 topico.save()

#             for form in formset_adicional:
#                 adicional = form.save(commit=False)
#                 adicional.plano = plano
#                 adicional.save()

#             for form in formset_acao:
#                 acao = form.save(commit=False)
#                 acao.plano = plano
#                 acao.save()

#             for form in formset_biblioteca:
#                 biblioteca = form.save(commit=False)
#                 biblioteca.plano = plano
#                 biblioteca.save()

#             # Redirecionar para a página de visualização de planos
#             return redirect('municipio', municipio=municipio)

#     else:
#         # Se a requisição não for POST, criar formulários vazios
#         form = PlanoForm()
#         formset_topico = TopicoFormSet(queryset=Topico.objects.none(), prefix='topico')
#         formset_adicional = AdicionalFormSet(queryset=Adicional.objects.none(), prefix='adicional')
#         formset_acao = AcaoFormSet(queryset=Acao.objects.none(), prefix='acao')
#         formset_biblioteca = BibliotecaFormSet(queryset=Biblioteca.objects.none(), prefix='biblioteca')

#     # Renderizar o template com os formulários e formsets
#     return render(request, 'criar_plano.html', {
#         'form': form,
#         'formset_topico': formset_topico,
#         'formset_adicional': formset_adicional,
#         'formset_acao': formset_acao,
#         'formset_biblioteca': formset_biblioteca,
#         'municipio': municipio,
#     })


def criar_plano(request, municipio):
    TopicoFormSet = modelformset_factory(Topico, form=TopicoForm, extra=1)
    AdicionalFormSet = modelformset_factory(Adicional, form=AdicionalForm, extra=1)
    AcaoFormSet = modelformset_factory(Acao, form=AcaoForm, extra=1)
    BibliotecaFormSet = modelformset_factory(Biblioteca, form=BibliotecaForm, extra=1)
    if request.method == 'POST':
        form = PlanoForm(request.POST)
        formset = TopicoFormSet(request.POST, request.FILES, queryset=Topico.objects.none())
        formset_topico = TopicoFormSet(request.POST, request.FILES, queryset=Topico.objects.none(), prefix='topico')
        formset_adicional = AdicionalFormSet(request.POST, request.FILES, queryset=Adicional.objects.none(), prefix='adicional')
        formset_acao = AcaoFormSet(request.POST, queryset=Acao.objects.none(), prefix='acao')
        formset_biblioteca = BibliotecaFormSet(request.POST, request.FILES, queryset=Biblioteca.objects.none(), prefix='biblioteca')
        if form.is_valid() and formset.is_valid():
            plano = form.save(commit=True)
            plano.municipio = municipio  # Assume que o modelo Plano tem um campo `municipio`
            plano.save()
            for form in formset:
                topico = form.save(commit=True)
                topico.plano = plano
                topico.save()
            for form in formset_adicional:
                 adicional = form.save(commit=True)
                 adicional.plano = plano
                 adicional.save()

            for form in formset_acao:
                acao = form.save(commit=True)
                acao.plano = plano
                acao.save()

            for form in formset_biblioteca:
                 biblioteca = form.save(commit=True)
                 biblioteca.plano = plano
                 biblioteca.save()
            return redirect('listar_planos') 
    else:
        form = PlanoForm()
        formset = TopicoFormSet(queryset=Topico.objects.none())
    return render(request, 'criar_plano.html', {'form': form, 'formset': formset,'formset_topico': formset_topico,'formset_adicional': formset_adicional,"formset_acao":formset_acao,"formset_biblioteca":formset_biblioteca, 'municipio': municipio})
