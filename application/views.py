from django.shortcuts import render,redirect
from application import models
from django.http import HttpResponse


# Create your views here.
def index(request):
    if request.method == 'POST':
        u = request.POST.get('username', None)  # 获取input标签name为username的输入框所获取得值
        user = {'username': u}  # 将获取的字符串存为字典
        if u != '':
            models.UserInfo.objects.create(
                username=u,
            )
    temp = models.UserInfo.objects.all();
    user_list = []
    for item in temp:
        user_list.append(item.username)
    return render(request, 'index.html', {'user_list': user_list})  # v3为字典值


def article(request):
    return HttpResponse(request.get_raw_uri())


def articles1(request, arg1):
    return HttpResponse(arg1)


def articles2(request, arg1, arg2):
    return HttpResponse(arg1 + '-' + arg2)


def articles3(request, y, m, d):
    return HttpResponse(y + '-' + m + '-' + d)


def articles4(request, yyyy, mm, dd):
    return HttpResponse(yyyy + '-' + mm + '-' + dd)


def login(request, arg):
    if request.method == 'POST':
        u = request.POST.get('username');
        p = request.POST.get('password');
        if u == 'admin' and p == '123456':
            # return HttpResponse('登录成功!')
            # return render(request, 'index.html')
            return redirect('/application/index/', {'arg': arg})  # v3为字典值
    return render(request, 'login.html', {'arg': arg})  # v3为字典值

def home(request):
    return render(request, 'index.html')  # v3为字典值

def ajax_recrive(request):
    if request.method == "POST":
        print(request.POST)
        return HttpResponse(request.POST.get("name"))
    return  HttpResponse("ajax")
