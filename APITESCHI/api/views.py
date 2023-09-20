from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from rest_framework.views import APIView
# Create your views here.


class sign_in(APIView):
    template_name="sign_in.html"
    def get(self,request):
        return render(request,self.template_name)
    

#def sign_up(request):
 #   if request.method == 'GET':
  #      print('viendo formulario')
   # else:
    #    print(request.POST)
     #   print('mandando formulario')
#
 #   return render(request, 'sign_up.')
    
class sign_up(APIView):
    template_name="sign_up.html"
    def get(self,request):
        
        if request.method == 'GET':
            print('Viendo formulario')
        else:
            print(request.POST)
            print('mandando datos')



        return render(request,'sign_up.html', {
            'form': UserCreationForm
        })
    
class index_9(APIView):
    template_name="index_9.html"
    def get(self,request):
        return render(request,self.template_name)