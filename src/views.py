from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from datetime import datetime
from src.models import Inventry, DeviceUser

# Create your views here.
def list_inventry(request):
    inventries = Inventry.objects.all()
    return render(request, 'inventry.html', {'inventries': inventries})

def get_inventry_by_id(request, inventry_id):
    # Retrieve the inventory item by ID or return a 404 error if not found
    inventry = get_object_or_404(Inventry, pk=inventry_id)

    # Render the template and pass the inventory item to the context
    return render(request, 'update_inventry.html', {'inventry': inventry})
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

def update_inventry_data(request):
    if request.method == 'POST':
        inventry_id = request.POST.get('inventry_id')
        # Retrieve the inventory item by ID or return a 404 error if not found
        inventry = get_object_or_404(Inventry, pk=inventry_id)
        type = request.POST.get('type')
        name = request.POST.get('name')
        serial_number = request.POST.get('serial_number')

        # Update the inventory item with the submitted data
        inventry.type = type
        inventry.name = name
        inventry.serial_no = serial_number
        inventry.updated_at = datetime.today()
        inventry.updated_by = request.user.username
        inventry.save()
        success_message = "Inventry updated successfully."
        return redirect('list_inventry')

    # Render the form template with the inventory item data
    return render(request, 'update_inventry.html', {'inventry': inventry})

def delete_inventry(request, inventry_id):
    inventry = get_object_or_404(Inventry, pk=inventry_id)
    inventry.delete()
    return redirect('list_inventry')
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