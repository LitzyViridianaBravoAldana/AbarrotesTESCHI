# render es para renderizar y redirect para redireccionar
from imaplib import _Authenticator
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .models import Usuario
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import HttpResponse  
from django.contrib.auth import login
from django.contrib.auth import authenticate, login
# Create your views here.



class index_9(APIView):
    template_name="index_9.html"
    def get(self,request):
        return render(request,self.template_name)

#INCIO DE CODIGO PARA INICIAR SESIÓN
class sign_in(APIView):
    template_name = "sign_in.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('Usuario', '')
        password = request.POST.get('password', '')

        # Autenticar al usuario
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Iniciar sesión
            login(request, user)
            return redirect('index_9')  # Redirigir a la página principal después del inicio de sesión
        else:
            # Si la autenticación falla, mostrar un mensaje de error
            return render(request, self.template_name, {'error': 'Nombre de usuario o contraseña incorrectos.'})
#FIN DE CODIGO PARA INICIO DE SESIÓN
    

#INICIO DE CODIGO PARA REGISTRAR NUEVOS USUARIOS
    


class sign_up(APIView):
    template_name = "sign_up.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        # Obtenemos los datos del formulario
        nombre_usuario = request.POST.get('Usuario', '')
        contra1 = request.POST.get('Contra1', '')
        contra2 = request.POST.get('Contra2', '')
        nombre = request.POST.get('Nombre', '')
        apellido_pa = request.POST.get('ApellidoPa', '')
        apellido_ma = request.POST.get('ApellidoMa', '')
        telefono = request.POST.get('Telefono', '')
        correo = request.POST.get('Correo', '')

        # Verificamos si las contraseñas son iguales
        if contra1 != contra2:
            return HttpResponse('La Contraseña no es la misma, verifique')

        # Creamos una instancia de Usuario con los datos del formulario
        user = Usuario(
            Nombre_Usuario=nombre_usuario,
            Contrasena=contra1,
            Nombre=nombre,
            Apellido_Pa=apellido_pa,
            Apellido_Ma=apellido_ma,
            Telefono=telefono,
            Correo=correo
        )

        # Guardamos el usuario en la base de datos
        user.save()

        # Enviamos un correo de bienvenida
        subject = 'Registro para TeschiWATT'
        message = 'Bienvenido a TESCHIWATT, gracias por registrarte en la pagina de libros más variada para ti'
        from_email = 'teschiwatt@gmail.com'
        recipient_list = [request.POST.get('Correo', '')]

        # Utiliza la plantilla de correo electrónico HTML
        html_message = render_to_string('correo_b.html', {})

        send_mail(subject, message, from_email, recipient_list, html_message=html_message)
        # Redirigimos a la página de inicio de sesión
        return redirect('sign_in')

#FIN DEL CODIGO DE NUEVOS USUARIOS


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
    
class favoritos(APIView):
    template_name="favoritos.html"
    def get(self,request):
        return render(request,self.template_name) 