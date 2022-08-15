from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context={
        'variable':'Im Abignya',
        'variable1':'BE 6th sem'
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')    

def contact(request):
    return render(request,'contact.html')

def sih(request):
    return render(request,'sih.html')

def travel_destination(request):
    return render(request,'travel_destination.html')    

def destination_details(request):
    return render(request,'destination_details.html')    

def shnongpdeng(request):
    return render(request,'shnongpdeng.html')      
