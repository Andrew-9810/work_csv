from django.shortcuts import render
from django.http import HttpResponse
from .models import OpenData
# from .forms import OpenDataForm
# Импортируем загрузчик.
from django.template import loader


def org_list(request):
    template = 'openData_csv/org_list.html'
    title = 'Организации'
    data = OpenData.objects.all()

    data_name = []
    for d in data:
        data_name.append(d.orgname)
    context = {
        'title': title,
        'text': data_name,
    }
    return render(request, template, context)


# def create(request):
#     """Страница создания обетов модели OpenData"""
#     template = 'openDataCreate/OpenDataForm.html'
#     if request.method == 'POST':
#         form = OpenDataForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return HttpResponse('Сохранил')
#     return render(request,template)
