from django.shortcuts import render, HttpResponse
from datetime import datetime
from src.models import Inventry, DeviceUser

# Create your views here.
def add_inventry(request):
    if request.method == "POST":
        # Get the values from POST data
        type = request.POST.get('type')
        name = request.POST.get('name')
        serial_number = request.POST.get('serial_number')

        # Check if name is empty
        if not name:
            error_message = "Name cannot be empty."
            return render(request, 'add_inventry.html', {'error_message': error_message, 'type':type, 'name':name, 'serial_number':serial_number})
        if not serial_number:
            error_message = "Serial No cannot be empty."
            return render(request, 'add_inventry.html', {'error_message': error_message, 'type':type, 'name':name, 'serial_number':serial_number})
        # Check if the name already exists in the database
        if Inventry.objects.filter(serial_no=serial_number).exists():
            error_message = f"A inventry with the Serial no '{serial_number}' already exists."
            return render(request, 'add_inventry.html', {'error_message': error_message, 'type':type, 'name':name, 'serial_number':serial_number})

        # Create Inventry object if name is not empty
        inventry = Inventry(type=type,name=name,serial_no=serial_number,status=1,device_status="",created_by=request.user.username,created_at=datetime.today(),updated_at=datetime.today(),updated_by=request.user.username)
        inventry.save()
        # Optionally, you can return a success message
        success_message = "Inventry created successfully."
        return render(request, 'add_inventry.html', {'success_message': success_message})

    return render(request, 'add_inventry.html')

def create_deviceuser(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact_no = request.POST.get('contact_no')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        state = request.POST.get('state')
        created_by = request.user.username  # Assuming you have user authentication
        DeviceUser.objects.create(
            name=name,
            email=email,
            contact_no=contact_no,
            address=address,
            pincode=pincode,
            state=state,
            created_by=created_by
        )
    return render(request, 'add_deviceuser.html')