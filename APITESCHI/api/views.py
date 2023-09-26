# render es para renderizar y redirect para redireccionar
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from rest_framework.views import APIView
from .models import Usuario
from django.core.mail import send_mail

# Create your views here.



class index_9(APIView):
    template_name="index_9.html"
    def get(self,request):
        return render(request,self.template_name)
    
class sign_in(APIView):
    template_name="sign_in.html"
    def get(self,request):
        return render(request,self.template_name)
    
class sign_up(APIView):
    template_name="sign_up.html"
    def get(self,request):
        return render(request,self.template_name)
    
    def post (self,request):
        #PARA MANDAR A LLAMAR LA TABLA DE USUARIO SE LLAMA POR LA CLASE NO POR EL TABLE
        User = Usuario(
            #Se coloca el nombre de la 
            Nombre_Usuario = request.POST['Usuario'],
            Contrasena = request.POST['Contra1'],
            Nombre = request.POST['Nombre'],
            Apellido_Pa = request.POST['ApellidoPa'],
            Apellido_Ma = request.POST['ApellidoMa'],
            Telefono = request.POST['Telefono'],
            Correo = request.POST['Correo']
        )
        User.save()
        subject = 'Registro para TeschiWATT '
        message = 'Bienvenido a TESCHIWATT, gracias por registrarte en la pagina de libros más vareada para tí'
        from_email = 'teschiwatt@gmail.com'
        recipient_list = [request.POST["Correo"]]

        send_mail(subject, message, from_email,recipient_list)
                  
        return redirect ('sign_in')
    

class team(APIView):
    template_name="team.html"
    def get(self,request):
        return render(request,self.template_name) 
    
class biblioteca(APIView):
    template_name="biblioteca.html"
    def get(self,request):
        return render(request,self.template_name) 
    

class genero1(APIView):
    template_name="genero1.html"
    def get(self,request):
        return render(request,self.template_name) 
    

class genero2(APIView):
    template_name="genero2.html"
    def get(self,request):
        return render(request,self.template_name) 
    

class genero3(APIView):
    template_name="genero3.html"
    def get(self,request):
        return render(request,self.template_name) 
    

class genero4(APIView):
    template_name="genero4.html"
    def get(self,request):
        return render(request,self.template_name) 
    
class genero5(APIView):
    template_name="genero5.html"
    def get(self,request):
        return render(request,self.template_name) 
    
class genero6(APIView):
    template_name="genero6.html"
    def get(self,request):
        return render(request,self.template_name) 
    

class genero7(APIView):
    template_name="genero7.html"
    def get(self,request):
        return render(request,self.template_name) 
    
class genero8(APIView):
    template_name="genero8.html"
    def get(self,request):
        return render(request,self.template_name) 
    
class genero9(APIView):
    template_name="genero9.html"
    def get(self,request):
        return render(request,self.template_name) 
    
class genero10(APIView):
    template_name="genero10.html"
    def get(self,request):
        return render(request,self.template_name) 
    
    
class editorial1(APIView):
    template_name="editorial1.html"
    def get(self,request):
        return render(request,self.template_name) 
    
class editorial2(APIView):
    template_name="editorial2.html"
    def get(self,request):
        return render(request,self.template_name) 

class editorial3(APIView):
    template_name="editorial3.html"
    def get(self,request):
        return render(request,self.template_name) 
    
class editorial4(APIView):
    template_name="editorial4.html"
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
    
#class sign_up(APIView):
 #   template_name="sign_up.html"
  #  def get(self,request):
        
   #     if request.method == 'GET':
    #        print('Viendo formulario')
     #   else:
      #      print(request.POST)
       #     print('mandando datos')

        #return render(request,'sign_up.html', {
         #  'form': UserCreationForm
        #})


    
