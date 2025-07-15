from django.http import JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from .models import User
import json
import re

def is_valid_email(email):
    return re.match(r'^[\w.-]+@[\w.-]+\.\w+$', email)

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            age = data.get('age')

            if not name or not email or age is None:
                return JsonResponse({'error': 'Missing required fields'}, status=400)

            if not is_valid_email(email):
                return JsonResponse({'error': 'Invalid email'}, status=400)

            user = User.objects.create(name=name, email=email, age=age)

            return JsonResponse({
                'id': str(user.id),
                'name': user.name,
                'email': user.email,
                'age': user.age
            }, status=201)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({"message": "Send a POST request to create a user."})

@csrf_exempt
def get_all_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        user_list = [{
            'id': str(user.id),
            'name': user.name,
            'email': user.email,
            'age': user.age
        } for user in users]
        return JsonResponse(user_list, safe=False)

@csrf_exempt
def get_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        return JsonResponse({
            'id': str(user.id),
            'name': user.name,
            'email': user.email,
            'age': user.age
        })
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

@csrf_exempt
def update_user(request, user_id):
    if request.method in ['PUT', 'POST']:
        try:
            data = json.loads(request.body)
            user = User.objects.get(id=user_id)

            user.name = data.get('name', user.name)
            user.email = data.get('email', user.email)
            user.age = data.get('age', user.age)

            user.save()

            return JsonResponse({
                'id': str(user.id),
                'name': user.name,
                'email': user.email,
                'age': user.age
            })
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
def delete_user(request, user_id):
    if request.method in ['DELETE', 'POST']:
        try:
            user = User.objects.get(id=user_id)
            user.delete()
            return JsonResponse({'message': 'User deleted successfully'})
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
