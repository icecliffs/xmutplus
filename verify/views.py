import json
import re
import uuid
from http import HTTPStatus

from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from verify.models import Students
from verify.utils import attestation

def contains_sensitive_keywords(input_string):
    keywords = [
        r'select', r'table', r'insert', r'update', r'delete', r'and', r'or',
        r'\'', r'\/\*', r'\*', r'\.\.\/', r'\.\/',
        r'union', r'into', r'load_file', r'outfile', r'dumpfile',
        r'sub', r'hex', r'=', r'or', r'||'
    ]

    pattern = r'|'.join(keywords)
    result = re.search(pattern, input_string, re.IGNORECASE)

    return result is not None
# Create your views here.
@csrf_protect
def generate(request):
    if 'token' not in request.session and 'username' not in request.session:
        return JsonResponse({
            'status': False,
            'messgae': '请先登录'
        }, status=HTTPStatus.UNAUTHORIZED)
    qq = request.POST.get('qq_number', '')
    try:
        token = attestation.generate(qq)
        return JsonResponse({'success': True, 'token': token})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)
def qq(request):
    if 'token' not in request.session and 'username' not in request.session:
        return JsonResponse({
            'status': False,
            'messgae': '请先登录'
        }, status=HTTPStatus.UNAUTHORIZED)
    return render(request, 'verify/index.html', {
    })
def authorizes(request):
    # return HttpRe
    # return JsonResponse({
    #     'status': False,
    #     'message': "内网部署，请访问 src.xmut.edu.cn（在建）"
    # })
    if request.method == "POST":
        contains_sensitive_keywords
        studentName = str(request.POST.get('student_name')).lower()
        studentId = str(request.POST.get('student_id')).lower()
        if studentName == "":
            return JsonResponse({
                'status': False,
                'message': "姓名不能为空哦"
            })
        if studentId == "":
            return JsonResponse({
                'status': False,
                'message': "学号不能为空哦"
            })
        if contains_sensitive_keywords(studentName) or contains_sensitive_keywords(studentId):
            return JsonResponse({
                'status': False,
                'message': "你注你🐎呢😅"
            })
        print(studentName)
        print(studentId)
        try:
            verifyCerticate = Students.objects.filter(realname=studentName, student_id=studentId)
            print(verifyCerticate)
            if verifyCerticate.exists():
                request.session['token'] = "icecliffs"
                request.session['username'] = studentName
                return JsonResponse({
                    'status': True,
                    'message': "身份校验成功！跳转中..."
                })
            else:
                return JsonResponse({
                    'status': False,
                    'message': "你确定你是我们厦门理工学院的？"
                })
        except:
            return JsonResponse(
                {
                    'status': False,
                    'message': "未知错误，请联系管理员！"
                }
            )
def logoutForm(request):
    logout(request)
    return JsonResponse({
        'message': '退出成功！'
    })