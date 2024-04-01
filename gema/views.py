from django.shortcuts import render, redirect
from .models import DeviceUser
from .forms import DeviceUserForm

def deviceuser_list(request):
    deviceusers = DeviceUser.objects.all()
    return render(request, 'deviceuser_list.html', {'deviceusers': deviceusers})

def deviceuser_detail(request, pk):
    deviceuser = DeviceUser.objects.get(pk=pk)
    return render(request, 'deviceuser_detail.html', {'deviceuser': deviceuser})

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
        return redirect('deviceuser_list')

def deviceuser_update(request, pk):
    deviceuser = DeviceUser.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeviceUserForm(request.POST, instance=deviceuser)
        if form.is_valid():
            form.save()
            return redirect('deviceuser_list')
    else:
        form = DeviceUserForm(instance=deviceuser)
    return render(request, 'deviceuser_form.html', {'form': form})

def deviceuser_delete(request, pk):
    deviceuser = DeviceUser.objects.get(pk=pk)
    if request.method == 'POST':
        deviceuser.delete()
        return redirect('deviceuser_list')
    return render(request, 'deviceuser_confirm_delete.html', {'deviceuser': deviceuser})
