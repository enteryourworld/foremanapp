from django.shortcuts import render
from .models import man, Foremans,Equipment
import json
from django.http import JsonResponse

def list(request):
    build = man.objects.all()
    eq = Equipment.objects.all()
    return render(request,'main/list.html', {'build': build,'eq':eq}, )

def projectnew(request):
    return render(request,'main/projectnew.html')
def registration(request):
    return render(request, 'main/reg.html')

def addworker(request):

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            surname = data.get('surname')
            number = data.get("number")
            patronymic = data.get("patronymic")
            status = data.get("status")
            builder = man(name=name,  secondname = surname, number = number, patronymic= patronymic,status=status )
            builder.save()


            # Process the data (e.g., save to the database)
            # For demonstration, we'll just return a JSON response
            return JsonResponse({'message': f'{name}, вы успешно зарегистрированы!'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)



def addforemans(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            surname = data.get('surname')
            number = data.get("number")
            password = data.get("password")
            patronymic = data.get("patronymic")

            foreman = Foremans(name=name,  secondname=surname, number=number, password=password, patronymic=patronymic)
            foreman.save()

            # Process the data (e.g., save to the database)
            # For demonstration, we'll just return a JSON response
            return JsonResponse({'message': f'{name}, вы успешно зарегистрированы!'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

def addequipment(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            names = data.get('names')
            expirydate = data.get('expirydate')
            owner = data.get("owner")
            registersdate = data.get("registersdate")
            equipmentphoto = data.get("equipmentphoto")

            foreman = Equipment(names=names,  registersdate=registersdate, owner=owner, equipmentphoto=equipmentphoto, expirydate=expirydate)
            foreman.save()

            # Process the data (e.g., save to the database)
            # For demonstration, we'll just return a JSON response
            return JsonResponse({''})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)