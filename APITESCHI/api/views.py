from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from rest_framework.views import APIView

# Importa tus vistas aquí

class sign_in(APIView):
    template_name='sign_in.html'
    def get(Self,request):
        return render(request.self.template_name)
    
class sign_up(APIView):
    template_name='sign_up.html'
    def get(Self,request):
        return render(request.self.template_name)
    
class index_9(APIView):
    template_name='index_9.html'
    def get(Self,request):
        return render(request.self.template_name)
