from django.shortcuts import render, redirect
from django.views import View  
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView
from django.views.generic import CreateView
from .forms import UserCreateForm, LoginForm, ContentsCreateForm
from .models import UserDB, ContentsDB


class Search_View(View):  
    def get(self, request, *args, **kwargs):  
        return render(request, 'fill_in_time_app/search.html')


class Time_line_View(View):
    def get(self, request, *args, **kwargs):  
        return render(request, 'fill_in_time_app/time_line.html')


class History_View(View):
    def get(self, request, *args, **kwargs):  
        return render(request, 'fill_in_time_app/history.html')


class Registed_View(View):
    def get(self, request, *args, **kwargs):  
        return render(request, 'fill_in_time_app/registed.html')


class Saved_View(View):
    def get(self, request, *args, **kwargs):  
        return render(request, 'fill_in_time_app/saved.html')


class Notlogin_View(View):
    def get(self, request, *args, **kwargs):  
        return render(request, 'fill_in_time_app/notlogin.html')


class Registed_login_View(View):
    def get(self, request, *args, **kwargs):  
        return render(request, 'fill_in_time_app/registed/login.html')


class Registed_personal_View(View):
    def get(self, request, *args, **kwargs):  
        return render(request, 'fill_in_time_app/registed/personal.html')


class Registed_login_terms_View(View):
    def get(self, request, *args, **kwargs):  
        return render(request, 'fill_in_time_app/registed/login/terms.html')


# 会員登録
class Registed_login_create_View(CreateView):
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            #フォームから'username'を読み取る
            username = form.cleaned_data.get('username')
            # フォームから'email'を読み取る
            email = form.cleaned_data.get('email')
            #フォームから'password1'を読み取る
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, email=email, password=password)
            login(request, user)
            return redirect('/')
        return render(request, 'fill_in_time_app/registed/login/create.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        return render(request, 'fill_in_time_app/registed/login/create.html', {'form': form,})


# #ログイン機能
class Registed_login_login_View(View):
    def post(self, request, *arg, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = UserDB.objects.get(username=username)
            login(request, user)
            return redirect('/')
        return render(request, 'fill_in_time_app/registed/login/login.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'fill_in_time_app/registed/login/login.html', {'form': form,})


class Logout_View(LogoutView):
    template_name = 'fill_in_time_app/search.html'

class Contents_Create_View(CreateView):
    def post(self, request, *args, **kwargs):
        form = ContentsCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            address = form.cleaned_data.get('address')
            homepage = form.cleaned_data.get('homepage')
            classification = form.cleaned_data.get('classification')
            telephone = form.cleaned_data.get('telephone')
            picture = form.cleaned_data.get('picture')
            price = form.cleaned_data.get('price')
            detail = form.cleaned_data.get('detail')
            open_time = form.cleaned_data.get('open_time')
            not_open_day = form.cleaned_data.get('not_open_day')
            min_stay_time = form.cleaned_data.get('min_stay_time')
            max_stay_time = form.cleaned_data.get('max_stay_time')
            how_come = form.cleaned_data.get('how_come')
            commnts = form.cleaned_data.get('comments')
            star = form.cleaned_data.get('star')
            
            contents = authenticate(name=name, address=address, homepage=homepage, classification=classification, telephone=telephone, picture=picture, price=price, detail=detail, open_time=open_time, not_open_day=not_open_day, min_stay_time=min_stay_time, max_stay_time=max_stay_time, how_come=how_come, comments=commnts, star=star)
            login(request, contents)
            return redirect('/')
        return render(request, 'fill_in_time_app/create_contents.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = ContentsCreateForm(request.POST)
        return  render(request, 'fill_in_time_app/create_contents.html', {'form': form,})


search = Search_View.as_view()
time_line = Time_line_View.as_view()
history = History_View.as_view()
registed = Registed_View.as_view()
saved = Saved_View.as_view()
notlogin = Notlogin_View.as_view()
registed_login = Registed_login_View.as_view()
registed_personal = Registed_personal_View.as_view()
registed_login_terms = Registed_login_terms_View.as_view()
registed_login_login = Registed_login_login_View.as_view()
registed_login_create = Registed_login_create_View.as_view()
logout = Logout_View.as_view()
create_contents = Contents_Create_View.as_view()