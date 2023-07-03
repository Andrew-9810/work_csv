from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import OpenData

from django.views.generic.edit import CreateView
from .forms import OpenDataForm
# Импортируем загрузчик.
from django.template import loader


def org_list(request):
    """Страница со списком всех организаций."""
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


# class create(CreateView):
#     """Страница создания объетов модели OpenData."""
#     form_class = OpenDataForm
#     template_name = 'openData_csv/OpenDataForm.html'
#     success_url = '/edit/'
    # if request.method == 'POST':
    #     form = OpenDataForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     return HttpResponse('Сохранил')
    # return render(request,template)

def OpenData_created(request):
    """Страница создания объетов модели OpenData."""
    template = 'openData_csv/OpenDataForm.html'
    if request.method == 'POST':
        form = OpenDataForm(request.POST)
        if form.is_valid():
            # post = form.save(commit=False)
            # post.author = request.user
            form.save()
            # Перенаправь на профиль пользователя через namespace
            # return redirect('posts:profile', username=request.user.username)
        return redirect('open:created')
        # return render(request, template, {'form': form})
    # Если это не РОСТ то выдай пустую форму
    form = OpenDataForm()
    return render(request, template, {'form': form})

def created(request):
    """Страница успешного создания объекта."""
    template = 'openData_csv/OpenDataForm_created.html'
    return render(request, template)


# Нужна страница редактиования.
# Страница редактирования и создания имеют объщий шаблон.
# .

# @login_required
def OpenData_edit(request, post_id):
    """Страница редактирования объетов модели OpenData."""
    template = 'openData_csv/OpenDataForm.html'
    open_data = get_object_or_404(OpenData, pk=post_id)
    if request.method == 'POST':
        form = OpenDataForm(request.POST, instance=open_data)
        if form.is_valid():
            # open_data = form.save(commit=False)
            # open_data.author = request.user
            form.save()
            return redirect('open:created')
            # return redirect('posts:post_detail', post_id)
        return render(request, template, {'form': form})
    # if request.user == open_data.author:
    #     form = OpenDataForm(instance=open_data)
    #     return render(request, template, {'form': form, 'is_edit': True})
    return redirect('open:create')
    # return HttpResponse('Это не Пост запрос!')

