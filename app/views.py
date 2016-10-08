#coding:utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from app.models import User
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
	
	
#测试首页
# def index(request):
# 	string = u"辛爷，你好，好好学习Python!"
# 	new_dict = {'site':u'body/','info':u'百度一下，你就知道'}
# 	return render(request,'app/index.html',{'string':string,'data':new_dict})   #render 是渲染模板；

#首页
def index(request):
	if request.session.get('has_login',False):
		user_forbid=User.objects.filter(user_forbid='1')
		user_noforb=User.objects.filter(user_forbid='0')
		if user_forbid and user_noforb:
			return render(request,'app/index.html',{"user_forbid":user_forbid,"user_noforb":user_noforb,"username":request.session['username']})   #render 是渲染模板；
		return render(request,'app/index.html')   #render 是渲染模板；
	else:
			response = HttpResponseRedirect('/login/')			
			return response

#表单类
class UserForm(forms.Form): 
    username = forms.CharField(initial='Username',widget=forms.TextInput(),max_length=100)
    password = forms.CharField(initial='Password',widget=forms.PasswordInput(),max_length=30)
    email = forms.CharField(initial='E-mail@',widget=forms.EmailInput(),max_length=30)
    
    
#处理登录
@csrf_exempt
def dellogin(request):
	if  request.is_ajax():
			request.session["longitude"] = request.POST['a']
			request.session["latitude"] = request.POST['b']
# 			print(request.session["latitude"])
# 			print(request.session["longitude"])
			return HttpResponse(request.session["longitude"] and request.session["latitude"]) #客户端发来的数据
# 	return render(request,'app/login.html')   #render 是渲染模板；

	if  request.method == 'POST':
            #获取表单用户密码
            username = request.POST['username']
            password = request.POST['password']
            user = User.objects.filter(user_name__exact = username,user_password__exact = password)
            if  request.session.has_key("longitude") and request.session.has_key("latitude"):
            	a=request.session['longitude']
            	b=request.session['latitude']
            	User.objects.filter(user_name= username).update(user_longi=a,user_lati=b)
            if user:
            	request.session['has_login'] =True
            	request.session['username']=username
            	user_forbid=User.objects.filter(user_forbid='1')
            	user_noforb=User.objects.filter(user_forbid='0')
            	return HttpResponseRedirect('/index/',{"user_forbid":user_forbid,"username":username,"user_noforb":user_noforb})   #render 是渲染模板；	
            else:
            	return HttpResponseRedirect('/login/')	
	else:
		uf = UserForm()
	return render_to_response('app/login.html',{'form':uf})#跨站点伪造请求

    
#处理注册
@csrf_exempt
def delregist(request):
	if  request.method == 'POST':
            #获取表单用户密码
            uf = UserForm(request.POST)
            if uf.is_valid():
            	username = uf.cleaned_data['username']
            	password = uf.cleaned_data['password']
            	email = uf.cleaned_data['email']
            	user = User.objects.filter(user_name__exact = username,user_password__exact = password)
            	if user:
            		HttpResponse("该用户已存在！")
            		return HttpResponseRedirect('/login/')
            	else:
            		User.objects.create(user_name= username,user_password=password,user_email=email)
            		request.session['has_login'] =True	
            		HttpResponse('regist success!!')
            		response = HttpResponseRedirect('/login/')
            		return response
            else:
            	return HttpResponse('regist failed!!')
            	response = HttpResponseRedirect('/index/')
            	return response
	else:
		uf = UserForm()
		HttpResponse('regist failed!!')
		return render_to_response('app/login.html',{'form':uf})



#处理登出     
def logout(request):
    try:
        del request.session['has_login']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")
   
   
def delmap(request,longi,lati):
	#return HttpResponse(longi);
	return render(request,'app/map.html',{"longi":longi,"lati":lati})   #render 是渲染模板；


#处理地图
def postmap(request):

	if request.method == 'POST':
		a = request.POST['a']
		b = request.POST['b']
		username= request.POST['name']
		request.session['has_map'] =True
	return HttpResponse(a) #客户端发来的数据


#个人主页
def detail(request):
	if request.session.get('has_login',False):
		username=request.session['username']
		return HttpResponse(username) #客户端发来的数据

# 		return render_(request,'app/detail.html',{'username':username})   #render 是渲染模板；
	else:
		return render(request,'app/login.html')   #render 是渲染模板；

	
