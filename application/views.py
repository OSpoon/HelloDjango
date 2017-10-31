from django.shortcuts import render
from application import models


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
