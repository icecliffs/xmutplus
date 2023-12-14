from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    views_list = [
        "入侵验证",
        "QQ群索引"
    ]
    return render(request, "index.html", {
        "views_list": views_list
    })
def verify(request):
    return render(request, 'verify.html')
def groups(request):
    return render(request, 'groups.html')
def test(request):
    return HttpResponse("Hello XMUTSEC!")
def disclaimer(request):
    return render(request, 'disclaimer.html')
def bot(request):
    return render(request, 'bot.html')
def page_not_found(request):
    return render(request, '404.html')