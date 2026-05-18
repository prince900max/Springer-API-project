"""
Django views for the users app.
"""
from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserForm

def user_list(request):
    """View to display list of all users"""
    users = User.objects.all().order_by('-created_at')
    return render(request, 'user_list.html', {'users': users})

def user_detail(request, pk):
    """View to display individual user profile"""
    user = get_object_or_404(User, pk=pk)
    return render(request, 'user_detail.html', {'user': user})

def user_create(request):
    """View to create a new user"""
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})

def user_update(request, pk):
    """View to update user information"""
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_detail', pk=user.pk)
    else:
        form = UserForm(instance=user)
    return render(request, 'user_form.html', {'form': form, 'user': user})

def user_delete(request, pk):
    """View to delete a user"""
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'user_confirm_delete.html', {'user': user})
