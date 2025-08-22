# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
# from django.http import JsonResponse
# from django.views import View
# from django.views.decorators.csrf import csrf_exempt
# import json

# class SignUpView(View):
#     @csrf_exempt
#     def post(self, request):
#         data = json.loads(request.body)
#         username = data.get('username')
#         email = data.get('email')
#         password = data.get('password')

#         if User.objects.filter(username=username).exists():
#             return JsonResponse({'error': 'Username already exists'}, status=400)

#         user = User.objects.create_user(username=username, email=email, password=password)
#         user.save()
#         return JsonResponse({'message': 'User created successfully'}, status=201)

# class SignInView(View):
#     @csrf_exempt
#     def post(self, request):
#         data = json.loads(request.body)
#         username = data.get('username')
#         password = data.get('password')

#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return JsonResponse({'message': 'Login successful'}, status=200)
#         else:
#             return JsonResponse({'error': 'Invalid credentials'}, status=401)

# class SignOutView(View):
#     def post(self, request):
#         logout(request)
#         return JsonResponse({'message': 'Logout successful'}, status=200)
from django.shortcuts import render, redirect
from .models import User

def signup_view(request):
    print("Signup view called") 
    if request.method == 'POST':
        username = request.POST.get('full_name')  # Use full_name as username
        email = request.POST.get('email')
        password = request.POST.get('password')
        # You should hash the password in production!

        # Create and save the user
        User.objects.create(username=username, email=email, password=password)
        return redirect('/admin/')  # or wherever you want to redirect

    return render(request, 'signup.html')