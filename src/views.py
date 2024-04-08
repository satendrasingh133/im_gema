from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from datetime import datetime
from src.models import Inventry, DeviceUser, MacbookInventry
import re
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                success_message = "Incorrect username and password."
                messages.success(request, success_message)
                return render(request, 'index.html')
    else:
        return redirect("dashboard")
    return render(request, 'index.html')

def dashboard(request):
    if request.user.is_anonymous:
        return redirect("/")
    macbookInventry = MacbookInventry.objects.all()
    return render(request, 'dashboard.html', {'macbookInventrys': macbookInventry})

def logout_view(request):
    logout(request)
    # Redirect to a page after logout
    return redirect("/")
def list_inventry(request):
    if request.user.is_anonymous:
        return redirect("/")
    inventries = Inventry.objects.all()
    return render(request, 'inventry.html', {'inventries': inventries})

def get_inventry_by_id(request, inventry_id):
    if request.user.is_anonymous:
        return redirect("/")
    # Retrieve the inventory item by ID or return a 404 error if not found
    inventry = get_object_or_404(Inventry, pk=inventry_id)

    # Render the template and pass the inventory item to the context
    return render(request, 'update_inventry.html', {'inventry': inventry})
def add_inventry(request):
    if request.user.is_anonymous:
        return redirect("/")
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
        messages.success(request, success_message)
        return redirect('list_inventry')

    return render(request, 'add_inventry.html')

def update_inventry_data(request):
    if request.user.is_anonymous:
        return redirect("/")
    if request.method == 'POST':
        inventry_id = request.POST.get('inventry_id')
        # Retrieve the inventory item by ID or return a 404 error if not found
        inventry = get_object_or_404(Inventry, pk=inventry_id)
        type = request.POST.get('type')
        name = request.POST.get('name')
        serial_number = request.POST.get('serial_number')
        status = request.POST.get('status')

        # Update the inventory item with the submitted data
        inventry.type = type
        inventry.name = name
        inventry.serial_no = serial_number
        inventry.status = status
        inventry.updated_at = datetime.today()
        inventry.updated_by = request.user.username
        inventry.save()
        success_message = "Inventry updated successfully."
        messages.success(request, success_message)
        return redirect('list_inventry')

    # Render the form template with the inventory item data
    return render(request, 'update_inventry.html', {'inventry': inventry})

def delete_inventry(request, inventry_id):
    inventry = get_object_or_404(Inventry, pk=inventry_id)
    inventry.delete()
    return redirect('list_inventry')


def create_deviceuser(request):
    if request.user.is_anonymous:
        return redirect("/")
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact_no = request.POST.get('contact_no')
        address = request.POST.get('address').replace(" ", "")
        pincode = request.POST.get('pincode')
        state = request.POST.get('state')
        created_by = request.user.username
        deviceuser = {
            'name': name,
            'email':email,
            'contact_no':contact_no,
            'address':address,
            'pincode':pincode,
            'state':state,
        }
        # Check if name is empty
        if not name:
            error_message_name = "Name cannot be empty."
            return render(request, 'add_deviceuser.html', {'error_message_name': error_message_name, 'deviceuser':deviceuser})
        if not email:
            error_message_email = "Email cannot be empty."
            return render(request, 'add_deviceuser.html', {'error_message_email': error_message_email, 'deviceuser':deviceuser})
        # Check if email format is valid using regular expression
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            error_message_email = "Invalid email format."
            return render(request, 'add_deviceuser.html', {'error_message_email': error_message_email, 'deviceuser':deviceuser})
            # Check if contact_no is empty
        if not contact_no:
            error_message_contact_no = "Contact number cannot be empty."
            return render(request, 'add_deviceuser.html', {'error_message_contact_no': error_message_contact_no, 'deviceuser':deviceuser})
        # Check if contact_no has exactly 10 digits
        if len(contact_no) != 10 or not contact_no.isdigit():
            error_message_contact_no = "Contact number must be a 10-digit number."
            return render(request, 'add_deviceuser.html', {'error_message_contact_no': error_message_contact_no, 'deviceuser':deviceuser})
        # Check if address is empty
        if not address:
            error_message_address = "Address cannot be empty."
            return render(request, 'add_deviceuser.html', {'error_message_address': error_message_address, 'deviceuser':deviceuser})

        # Check if pincode is empty
        if not pincode:
            error_message_pincode = "Pincode cannot be empty."
            return render(request, 'add_deviceuser.html', {'error_message_pincode': error_message_pincode, 'deviceuser':deviceuser})
        # Check if pincode has exactly 6 digits
        if len(pincode) != 6 or not pincode.isdigit():
            error_message_pincode = "Pincode must be a 6-digit number."
            return render(request, 'add_deviceuser.html', {'error_message_pincode': error_message_pincode, 'deviceuser':deviceuser})
        # Check if state is empty
        if not state:
            error_message_state = "State cannot be empty."
            return render(request, 'add_deviceuser.html', {'error_message_state': error_message_state, 'deviceuser':deviceuser})

        # Check if the contact number already exists in the database
        if DeviceUser.objects.filter(contact_no=contact_no).exists():
            error_message = "A user with the contact number '{contact_no}' already exists."
            return render(request, 'add_deviceuser.html', {'error_message': error_message, 'deviceuser':deviceuser})

        # Check if the email already exists in the database
        if DeviceUser.objects.filter(email=email).exists():
            error_message = "A user with the email '{email}' already exists."
            return render(request, 'add_deviceuser.html', {'error_message': error_message, 'deviceuser':deviceuser})

        DeviceUser.objects.create(
            name=name,
            email=email,
            contact_no=contact_no,
            address=address.lstrip().rstrip(),
            pincode=pincode,
            state=state,
            created_by=created_by,
            status=1
        )
        success_message = "User created successfully."
        messages.success(request, success_message)
        return redirect('user_overview')

    return render(request, 'add_deviceuser.html')

def user_overview(request):
    if request.user.is_anonymous:
        return redirect("/")
    deviceuser = DeviceUser.objects.all()
    return render(request, 'user_overview.html', {'deviceuser': deviceuser})


def edit_user(request, user_id):
    if request.user.is_anonymous:
        return redirect("/")
    user = DeviceUser.objects.get(pk=user_id)

    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact_no = request.POST.get('contact_no')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        state = request.POST.get('state')
        deviceuser = {
            'name': name,
            'email': email,
            'contact_no': contact_no,
            'address': address,
            'pincode': pincode,
            'state': state,
        }
        # Check if required fields are empty
        if not name:
            error_message_name = "Name cannot be empty."
            return render(request, 'add_deviceuser.html', {'error_message_name': error_message_name, 'user': user})
        if not email:
            error_message_email = "Email cannot be empty."
            return render(request, 'add_deviceuser.html', {'error_message_email': error_message_email, 'user': user})
        if not contact_no:
            error_message_contact_no = "Contact number cannot be empty."
            return render(request, 'add_deviceuser.html',
                          {'error_message_contact_no': error_message_contact_no, 'user': user})
        if not address:
            error_message_address = "Address cannot be empty."
            return render(request, 'add_deviceuser.html',
                          {'error_message_address': error_message_address, 'user': user})
        if not state:
            error_message_state = "State cannot be empty."
            return render(request, 'add_deviceuser.html', {'error_message_state': error_message_state, 'user': user})
        if not pincode:
            error_message_pincode = "Pincode cannot be empty."
            return render(request, 'add_deviceuser.html',
                          {'error_message_pincode': error_message_pincode, 'user': user})

        # Check if email format is valid using regular expression
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            error_message_email = "Invalid email format."
            return render(request, 'add_deviceuser.html', {'error_message_email': error_message_email, 'user': user})
            # Check if contact_no has exactly 10 digits
        if len(contact_no) != 10 or not contact_no.isdigit():
            error_message_contact_no = "Contact number must be a 10-digit number."
            return render(request, 'add_deviceuser.html',
                          {'error_message_contact_no': error_message_contact_no, 'user': user})
        # Check if pincode has exactly 6 digits
        if len(pincode) != 6 or not pincode.isdigit():
            error_message_pincode = "Pincode must be a 6-digit number."
            return render(request, 'add_deviceuser.html',
                          {'error_message_pincode': error_message_pincode, 'user': user})

            # Update DeviceUser object
        user.name = name
        user.email = email
        user.contact_no = contact_no
        user.address = address
        user.pincode = pincode
        user.state = state
        user.save()
        success_message = "User updated successfully."
        messages.success(request, success_message)
        return redirect('user_overview')
    return render(request, 'add_deviceuser.html', {'deviceuser': user})

def assign_macbook(request):
    if request.user.is_anonymous:
        return redirect("/")
    deviceusers = DeviceUser.objects.filter(status=1)
    laptops = Inventry.objects.filter(type='laptop', status=1)
    adapters = Inventry.objects.filter(type='adapter', status=1)
    if request.method == "POST":
        tracking_slip = request.FILES.get('tracking_slpi')
        tracking_slip_path=""
        if tracking_slip:
            current_datetime_seconds = str(int(timezone.now().timestamp()))
            file_extension = tracking_slip.name.split('.')[-1]
            new_filename = f"{current_datetime_seconds}.{file_extension}"
            fs = FileSystemStorage()
            filename = fs.save(new_filename, tracking_slip)
            tracking_slip_path = fs.url(filename)

        deviceuser_id = request.POST.get('user')
        inventry_id = request.POST.get('device')
        adapter = request.POST.get('adapter')
        tracking_no = request.POST.get('tracking_no')
        datetimes = request.POST.get('datetime')
        other_information = request.POST.get('other_information')
        macbookInventryData = {
            'user': deviceuser_id,
            'device': inventry_id,
            'adapter': adapter,
            'tracking_no': tracking_no,
            'datetime': datetimes,
            'other_information': other_information,
        }
        # Check if required fields are empty
        if not deviceuser_id:
            error_message = "User cannot be empty."
            return render(request, 'assign_macbook.html', {'error_message': error_message, 'macbookInventryData': macbookInventryData, 'deviceusers':deviceusers, 'laptops':laptops, 'adapters':adapters})
        if not inventry_id:
            error_message = "Device cannot be empty."
            return render(request, 'assign_macbook.html', {'error_message': error_message, 'macbookInventryData': macbookInventryData, 'deviceusers':deviceusers, 'laptops':laptops, 'adapters':adapters})
        # if not tracking_no:
        #     error_message = "Tracking No cannot be empty."
        #     return render(request, 'assign_macbook.html', {'error_message': error_message, 'macbookInventryData': macbookInventryData, 'deviceusers':deviceusers, 'inventries':inventries})
        if not datetimes:
            error_message = "Datetime cannot be empty."
            return render(request, 'assign_macbook.html', {'error_message': error_message, 'macbookInventryData': macbookInventryData, 'deviceusers':deviceusers, 'laptops':laptops, 'adapters':adapters})

        macbookInventry = MacbookInventry(macbook_id=inventry_id, usb_id=adapter, deviceuser_id=deviceuser_id, tracking_no=tracking_no, status=1, other_info=other_information,
                            created_by=request.user.username, created_at=datetime.today(), updated_at=datetime.today(),
                            updated_by=request.user.username, datetime=datetimes, photo=tracking_slip_path)
        macbookInventry.save()
        # change status in inventry table
        macbookInventry = get_object_or_404(Inventry, pk=inventry_id)
        macbookInventry.status = 0
        macbookInventry.save()

        adapterInventry = get_object_or_404(Inventry, pk=adapter)
        adapterInventry.status = 0
        adapterInventry.save()

        # change status in deviceuser table
        deviceuser = get_object_or_404(DeviceUser, pk=deviceuser_id)
        deviceuser.status = 0
        deviceuser.save()

        # Optionally, you can return a success message
        success_message = "MacBook assign successfully."
        messages.success(request, success_message)
        return redirect('dashboard')

    return render(request, 'assign_macbook.html', {'deviceusers':deviceusers, 'laptops':laptops, 'adapters':adapters})
def delete_deviceuser(request, user_id):
    user = get_object_or_404(DeviceUser, pk=user_id)
    user.delete()
    return redirect('user_overview')

def asign_and_breakfis(request, id):
    deviceusers = DeviceUser.objects.all()
    laptops = Inventry.objects.filter(type='laptop')
    adapters = Inventry.objects.filter(type='adapter')
    macbookInventryData = get_object_or_404(MacbookInventry, pk=id)
    return render(request, 'asign_and_breakfis.html', {'macbookInventryData': macbookInventryData, 'deviceusers':deviceusers, 'laptops':laptops, 'adapters':adapters})

