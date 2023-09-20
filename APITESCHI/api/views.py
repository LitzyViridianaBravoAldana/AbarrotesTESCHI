from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.


class sign_in(APIView):
    template_name="sign_in"
    def get(self,request):
        return render(request,self.template_name)
    
class sign_up(APIView):
    template_name="sign_up.html"
    def get(self,request):
        return render(request,self.template_name)
    
class index_9(APIView):
    template_name="index_9.html"
    def get(self,request):
        return render(request,self.template_name)