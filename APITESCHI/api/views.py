# render es para renderizar y redirect para redireccionar
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .models import Usuario
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password, make_password

# Create your views here.



class index_9(APIView):
    template_name="index_9.html"
    def get(self,request):
        return render(request,self.template_name)

from django.contrib.auth.hashers import make_password

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
        correo = request.POST.get('Correo', '')

        # Verificamos si las contraseñas son iguales
        if contra1 != contra2:
           return render(request, self.template_name, {'error': 'La Contraseña no es la misma, verifique'})

        try:
            # Creamos una instancia de Usuario con los datos del formulario
            user = Usuario(
                Nombre_Usuario=nombre_usuario,
                Nombre=nombre,
                Apellido_Pa=apellido_pa,
                Correo=correo,
                Contrasena=contra1
            )

            # Establecemos la contraseña utilizando make_password
            user.Contrasena = make_password(contra1)

            # Guardamos el usuario en la base de datos
            user.save()

            # Enviamos un correo de bienvenida
            subject = 'Registro para TeschiWATT'
            message = 'Bienvenido a TESCHIWATT, gracias por registrarte en la página de libros más variada para ti'
            from_email = 'teschiwatt@gmail.com'
            recipient_list = [request.POST.get('Correo', '')]

            # Utiliza la plantilla de correo electrónico HTML
            html_message = render_to_string('correo_b.html', {'username': nombre_usuario, 'password': contra1})

            send_mail(subject, message, from_email, recipient_list, html_message=html_message)

            # Redirigimos a la página de inicio de sesión
            return redirect('sign_in')

        except Exception as e:
            # Manejar cualquier excepción y mostrar el mensaje de error apropiado
            return render(request, self.template_name, {'error': f'Error al registrar usuario: {e}'})


# INCIO DE CODIGO PARA INICIAR SESIÓN

class sign_in(APIView):
    template_name = "sign_in.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        correo = request.POST.get('correo', '').strip()
        contrasena = request.POST.get('password', '').strip()

        print(f'Correo: {correo}, Contraseña: {contrasena}')

        try:
            # Autenticar al usuario por correo electrónico
            user = authenticate(request, Correo=correo, password=contrasena)

            if user is not None:
                # Contraseña válida, iniciar sesión
                print(f'Usuario autenticado: {user}')
                login(request, user)
                return redirect('index_9')
            else:
                # Usuario no encontrado o contraseña incorrecta
                print('Autenticación fallida. Usuario:', user)
                return render(request, 'sign_in.html', {'error': 'Correo o contraseña incorrectos.'})

        except Exception as e:
            # Manejar cualquier excepción y mostrar el mensaje de error apropiado
            print(f'Error al autenticar usuario: {e}')
            return render(request, 'sign_in.html', {'error': f'Error al autenticar usuario: {e}'})


# FIN DE CODIGO PARA INICIO DE SESIÓN






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