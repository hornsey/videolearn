from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse

def index(request):
	return HttpResponse("这是首页")

#视频详情页
def videoDetail(request,vid):
	return HttpResponse("这是{}视频详情页".format(vid))

#观看历史页
def videoHistory(request):
	return HttpResponse("这是观看历史页")

#视频分类页
def videoCate(request, cateid):
	return HttpResponse("这是{0}分类".format(cateid))

#登录页面
def login(request):
	return HttpResponse("这是登录页")

#注册页面
def register(request):
	return HttpResponse("这是注册页")
