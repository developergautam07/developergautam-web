from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(requests):
    #return HttpResponse("This is Home Page (/home)")
    context = {"name":"Gautam", "framework":"Django"}
    return render(requests, 'home.html', context)

def about(requests):
    #return HttpResponse("This is Home Page (/about)")
    return render(requests, 'about.html')

def projects(requests):
    #return HttpResponse("This is Home Page (/projects)")
    return render(requests, 'projects.html')


def contact(requests):
    if requests.method == "POST":
        name = requests.POST['name']
        email = requests.POST['email']
        phone = requests.POST['phone']
        desc = requests.POST['desc']
        #print(name, email, phone, desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        print("Data Has Been Written to the DB")

    #return HttpResponse("This is Home Page (/contact)")
    return render(requests, 'contact.html')

