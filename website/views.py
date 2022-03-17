from django.shortcuts import render
from django.core.mail import send_mail
# from django.views.decorators.csrf import csrf_protect

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

# @csrf_protect
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # send an email
        send_mail(
            'message from ' + name, #subject
            message, # message
            email, #from email
            ['priyarohitsharma20@gmail.com'], #to Email
        )

        return render(request, 'contact.html', {'name':name})
    else:
        return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about-us.html', {})

def project(request):
    return render(request, 'project.html', {})

def project_details(request):
    return render(request, 'project-details.html', {})

def service(request):
    return render(request, 'service.html', {})

def appointment(request):
    return render(request, 'appointment.html', {})

def book(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        address = request.POST.get('address')
        service = request.POST.get('service')
        details = request.POST.get('details')


        # send an email
        booking = "Name: " + name + " Phone: " + number + " Email: " + email + " Address: " + address + " Service: " + service + " Service Details: " + details
        send_mail(
            'Booking Request', #subject
            booking, # message
            email, #from email
            ['priyarohitsharma20@gmail.com'], #to Email
        )

        return render(request, 'book.html', {'name': name,
                                            'number': number,
                                            'email': email,
                                            'address': address,
                                            'service': service,
                                            'details': details})
    else:
        return render(request, 'home.html', {})
