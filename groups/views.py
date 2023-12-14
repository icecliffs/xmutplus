import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from fake_useragent import UserAgent

from groups.models import Groups, WebSite, Category


# Create your views here.
def group_category(category):
    groups = Groups.objects.filter(category=category)
    websites = WebSite.objects.filter(category=category)
    categories = Category.objects.filter(parent=category)
    return {
        'id': category.id,
        'name': category.name,
        'groups': list(groups) if groups.count() > 0 else None,
        'websites': list(websites) if websites.count() > 0 else None,
    }
def index(request):
    list_groups = []
    list_groups.append(group_category(Category.objects.get(id=4)))
    list_groups.append(group_category(Category.objects.get(id=5)))
    list_groups.append(group_category(Category.objects.get(id=6)))
    list_groups.append(group_category(Category.objects.get(id=7)))
    return render(request, 'groups.html', {
        'groups': list_groups
    })
    # group = Groups.objects.filter()
    # return render(request, 'groups.html', {
    #     'group': group
    # })

def website(request):
    list_website = []
    list_website.append(group_category(Category.objects.get(id=3)))
    list_website.append(group_category(Category.objects.get(id=2)))
    list_website.append(group_category(Category.objects.get(id=1)))
    return render(request, 'website.html', {
        'website': list_website
    })

def calendar(request):
    ua = UserAgent()
    url = "https://jwc.xmut.edu.cn/"
    headers = {
        "User-Agent": ua.random
    }
    proxies = {
        "http": None,
        "https": None
    }
    res = requests.get(url=url, headers=headers, proxies=proxies)
    soup = BeautifulSoup(res.content, 'html.parser')
    links = soup.find_all('a', string='查看校历')
    for link in links:
        xiaoli = link['href']
    xiaoli = "https://jwc.xmut.edu.cn/" + xiaoli
    res = requests.get(url=xiaoli, headers=headers, proxies=proxies)
    soup = BeautifulSoup(res.content, 'html.parser')
    iframe_tag = soup.find('iframe')
    pdf_url = iframe_tag['src']
    pdf_url = 'https://jwc.xmut.edu.cn' + pdf_url
    print(pdf_url)
    return render(request, 'calendar.html', {
        'xiaobao': pdf_url
    })