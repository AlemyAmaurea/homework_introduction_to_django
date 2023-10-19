from django.shortcuts import render

def home_con(request):
    return render(request, 'catalog/home.html')

def contacts_con(request):
    return render(request, 'catalog/contacts.html')

