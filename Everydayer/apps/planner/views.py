import datetime

from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from Everydayer.apps.planner.models import Task
from django.urls import reverse
from datetime import timedelta
from Everydayer.apps.planner.forms import EditForm

month_list = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
              'Декабрь']


def index(request):
    # latest_tasks = Task.objects.order_by('-task_date')
    today = datetime.date.today()
    week = [today, today + timedelta(1), today + timedelta(2), today + timedelta(3), today + timedelta(4),
            today + timedelta(5), today + timedelta(6), today + timedelta(7)]
    latest_tasks = Task.objects.all()
    if week[0].day < week[7].day:
        month = month_list[today.month - 1]
    else:
        month = str(month_list[today.month - 1]) + " - " + str(month_list[today.month])

    return render(request, 'planner/list.html', {'latest_tasks': latest_tasks, 'week': week, 'month': month})


def detail(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except:
        raise Http404("Таск не найден")

    return render(request, 'planner/edit.html', {'task': task})


def create(request):
    if request.POST:
        try:
            task = Task()
        except:
            raise Http404("Таск не удалось создать")

        task.task_title = request.POST['title']
        task.task_description = request.POST['description']
        task.task_date = request.POST['date'] + "+00:00"
        task.task_is_done = False
        task.save()

        return HttpResponseRedirect(reverse('planner:index'))
    # form = EditForm(request.POST or None)
    # if form.is_valid():
    #     form.save()

    return render(request, 'planner/create.html', {})


def delete(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except:
        raise Http404("Таск не найден")

    task.delete()
    return HttpResponse("OK")


def edit(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except:
        raise Http404("Таск не найден")

    task.task_title = request.POST['title']
    task.task_description = request.POST['description']
    task.task_date = request.POST['date'] + "+00:00"
    task.save()

    return HttpResponseRedirect(reverse('planner:index'))


def checkbox(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except:
        raise Http404("Неправильно изменил checkbox")

    task.task_is_done = not task.task_is_done
    task.save()

    return HttpResponse("ok")
