from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages


def index_lk(request):
    if not request.user.is_authenticated:
        return render(request, 'html/lk.html', {})
    courses = Course.objects.all()
    my_courses = []
    user_email = request.user.email
    ind = 0
    for course in courses:
        for user in course.users.all():
            if user.email_adress == user_email:
                # my_courses.append('<a href="/lk/' + str(ind) + '/">' + str(course) + '</a>')
                my_courses.append((course, ind))
                break
        ind += 1
    return render(request, 'html/lk.html', {'courses': my_courses})


def theme_tasks(request, course_id, theme_id):
    course_id = int(course_id)
    theme_id = int(theme_id)
    courses = Course.objects.all()
    cs = []
    for course in courses:
        cs.append(course)
    # check if user is subscribed
    my_courses = []
    user_email = request.user.email
    for course in courses:
        for user in course.users.all():
            if user.email_adress == user_email:
                my_courses.append(str(course))
                break
    if str(cs[course_id]) not in my_courses:
        return HttpResponse('''
            Вы не зарегистрированы на этот курс
            ''')
    this_course = cs[course_id]
    themes = []
    for theme in this_course.themes.all():
        themes.append(theme)

    this_theme = themes[theme_id]
    tasks = []
    theory = this_theme.theory
    for task in this_theme.tasks.all():
        tasks.append(str(task.text))
    # return HttpResponse(str(this_theme) + '<br>' + '<br>'.join(tasks))
    return render(
        request,
        'html/theme.html',
        {
            'course': this_course,
            'tasks': tasks,
            'theme_name': this_theme.name,
            'theory': theory
        }
    )


def course_themes(request, course_id):
    course_id = int(course_id)
    courses = Course.objects.all() # get all from courses db
    cs = []
    percentage = []
    for course in courses:
        cs.append(course)

    # check if user is subscribed
    my_courses = []
    user_email = request.user.email
    for course in courses:
        for user in course.users.all():
            if user.email_adress == user_email:
                my_courses.append(str(course))
                break

    if str(cs[course_id]) not in my_courses: #give user warning if not subscribed
        print(str(cs[course_id]), my_courses)
        return HttpResponse('''
        Вы не зарегистрированы на этот курс
        ''')

    # percentage count
    #
    # TODO
    #

    # list of themes
    this_course = cs[course_id]
    themes = []
    ind = 0
    for theme in this_course.themes.all():
        themes.append((str(theme), ind, bool(theme.opened)))
        ind += 1
    # return HttpResponse(str(cs[course_id]) + '<br>' + '<br>'.join(themes))

    return render(
                request,
                'html/course.html',
                {
                    'course': this_course,
                    'themes': themes,
                    'course_id': str(course_id),
                }
            )


def logout_user(request):
    logout(request)
    return redirect('login')
