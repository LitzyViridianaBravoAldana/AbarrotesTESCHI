from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.


class sing_in(APIView):
    template_name="sign_in.html"
    def get(self,request):
        return render(request,self.template_name)