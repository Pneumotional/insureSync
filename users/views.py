from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User,Group
from django.contrib.admin.views.decorators import staff_member_required
from .forms import AdminUserCreationForm, AdminUserUpdateForm, LoginForm
from .models import UserProfile
from django.core.paginator import Paginator  # Correct import
from django.db.models import Q  # Also add this import
from django.contrib.auth import logout



@login_required
def home_view(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            try:
                user = User.objects.get(username=username)
                
                # If the username exists, check if the password is correct
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')  # Redirect to the home page after successful login
                else:
                    messages.error(request, 'Incorrect password')
            except User.DoesNotExist:
                messages.error(request, 'Username does not exist')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})



# Check if the user is an admin
def is_admin(user):
    return user.is_authenticated and user.is_staff

# User creation view restricted to logged-in admins
@login_required
@user_passes_test(is_admin)
def create_user(request):
    if request.method == 'POST':
        form = AdminUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully.')
            return redirect('user_list')  # Adjust this to your user list view name
    else:
        form = AdminUserCreationForm()
    
    return render(request, 'create_user.html', {'form': form})

# View for updating a user (Only admins can access this view)
@login_required
@user_passes_test(is_admin)
def update_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    profile = user.userprofile
    
    if request.method == 'POST':
        form = AdminUserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated successfully.')
            return redirect('user_list')  # Adjust this to your user list view name
    else:
        form = AdminUserUpdateForm(initial={
            'username': user.username,
            'email': user.email,
            'first_name': profile.first_name,
            'last_name': profile.last_name,
            'phone_number': profile.phone_number,
            'role': profile.groups
        })
    
    return render(request, 'user_update.html', {'form': form, 'user': user})




@user_passes_test(is_admin)
def user_list(request):
    # Get query parameters
    search_query = request.GET.get('search', '')
    group_filter = request.GET.get('group', '')
    
    # Start with all users
    users = UserProfile.objects.select_related('user').prefetch_related('groups')
    
    # Apply search filter
    if search_query:
        users = users.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) | 
            Q(user__username__icontains=search_query) |
            Q(phone_number__icontains=search_query)
        )
    
    # Apply group filter
    if group_filter:
        users = users.filter(groups__name=group_filter)
    
    # Pagination
    paginator = Paginator(users, 10)  # 10 users per page
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    # Get all groups for filtering
    groups = Group.objects.all()
    
    context = {
        'users': page_obj,
        'groups': groups,
        'search_query': search_query,
        'group_filter': group_filter
    }
    
    return render(request, 'user_list.html', context)