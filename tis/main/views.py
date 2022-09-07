from distutils.log import error
from tabnanny import check
from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница сайта'})


def about(request):
    return render(request, 'main/about.html')


def Registration(request):
    submitbutton = request.POST.get("submit")
    global User_class
    User_check = ''
    User_name = ''
    User_surname = ''
    User_patronimic = ''
    User_mail = ''
    User_school = ''
    User_class = ''
    User_latter = ''
    error = ''
    if request.method == 'POST':
        User = RegisterForm(request.POST or None)
        if User.is_valid():
            User_class = User.cleaned_data.get("number")
            if User.cleaned_data.get("certificate") == True:
                User_name = User.cleaned_data.get("name")
                User_surname = User.cleaned_data.get("surname")
                User_patronimic = User.cleaned_data.get("patronimic")
                User_mail = User.cleaned_data.get("mail")
                User_school = User.cleaned_data.get("school")
                User_latter = User.cleaned_data.get("latter")
            return redirect('test')
        else:
            error = 'Данные были неверно заполнены'

    register = RegisterForm()
    return render(request, 'main/Registration.html', {'register': register, 'error': error})


def test(request):
    submitbutton = request.POST.get("submit")
    global true_answer, false_answer
    User_answer = []
    true_answer = []
    true_list = []
    false_answer = []
    User_answer_1 = ''
    User_answer_2 = ''
    User_answer_3 = ''
    User_answer_4 = ''
    User_answer_5 = ''
    User_answer_6 = ''
    User_answer_7 = ''
    User_answer_8 = ''
    User_answer_9 = ''
    User_answer_10 = ''
    error = ''
    Our_answer = Task.objects.all()

    if User_class == '5':
        check = 0
        for j in range(0, 10):
            true_list.append(Our_answer[j].task)
    if User_class == '6':
        check = 10
        for j in range(10, 20):
            true_list.append(Our_answer[j].task)
    if User_class == '7':
        check = 20
        for j in range(20, 30):
            true_list.append(Our_answer[j].task)
    if User_class == '8':
        check = 30
        for j in range(30, 40):
            true_list.append(Our_answer[j].task)
    else:
        check = 30
        for j in range(30, 40):
            true_list.append(Our_answer[j].task)
    if request.method == 'POST':
        User_answer_form = AnswerForm(request.POST)
        if User_answer_form.is_valid():
            User_answer_1 = str(User_answer_form.cleaned_data.get("answer_1"))
            User_answer_2 = str(User_answer_form.cleaned_data.get("answer_2"))
            User_answer_3 = str(User_answer_form.cleaned_data.get("answer_3"))
            User_answer_4 = str(User_answer_form.cleaned_data.get("answer_4"))
            User_answer_5 = str(User_answer_form.cleaned_data.get("answer_5"))
            User_answer_6 = str(User_answer_form.cleaned_data.get("answer_6"))
            User_answer_7 = str(User_answer_form.cleaned_data.get("answer_7"))
            User_answer_8 = str(User_answer_form.cleaned_data.get("answer_8"))
            User_answer_9 = str(User_answer_form.cleaned_data.get("answer_9"))
            User_answer_10 = str(
                User_answer_form.cleaned_data.get("answer_10"))
            User_answer = [User_answer_1, User_answer_2, User_answer_3, User_answer_4, User_answer_5,
                           User_answer_6, User_answer_7, User_answer_8, User_answer_9, User_answer_10]

            for i in range(len(true_list)):
                if str(User_answer[i]) == str(true_list[i]):
                    true_answer.append(i)
                else:
                    false_answer.append(i+1)
            return redirect('results')
        else:
            error = 'Данные были неверно заполнены'
    tasks_1 = Our_answer[check].title
    tasks_2 = Our_answer[check+1].title
    tasks_3 = Our_answer[check+2].title
    tasks_4 = Our_answer[check+3].title
    tasks_5 = Our_answer[check+4].title
    tasks_6 = Our_answer[check+5].title
    tasks_7 = Our_answer[check+6].title
    tasks_8 = Our_answer[check+7].title
    tasks_9 = Our_answer[check+8].title
    tasks_10 = Our_answer[check+9].title
    answer = AnswerForm()
    return render(request, 'main/test.html', {'title': 'Тестирование', 'tasks_1': tasks_1, 'tasks_2': tasks_2, 'tasks_3': tasks_3, 'tasks_4': tasks_4, 'tasks_5': tasks_5, 'tasks_6': tasks_6, 'tasks_7': tasks_7, 'tasks_8': tasks_8, 'tasks_9': tasks_9, 'tasks_10': tasks_10, 'answer': answer, 'error': error})


def Results(request):
    fl = ''
    score = (len(true_answer) * 10)
    false_list = ''
    if len(false_answer) > 0:
        fl = 'Не правильно были выполнены задания номер '
        for el in false_answer:
            false_list += str(el) + ' '
    else:
        false_list = 'Вы молодец , все ответы правильные'
    return render(request, 'main/results.html', {'title': 'Результаты', 'score': score, 'false_list': false_list, 'fl': fl})
