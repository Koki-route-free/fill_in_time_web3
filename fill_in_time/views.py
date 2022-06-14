from django.shortcuts import redirect, reverse
from django.views import View  

class index(View):
    def get(self, request, *args, **kwargs):
        return redirect(reverse('fill_in_time_app:search'))
index = index.as_view()