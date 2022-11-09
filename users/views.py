from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, render, reverse, redirect
from django.views import generic
from django.contrib import messages
from users.models import (User, Company,Employee_Location)
from .forms import (CreateUser, UpdateUser, CompanyForm)
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from product.models import Hardware, Software

# User Create View
@method_decorator(login_required, name='dispatch')
class UserCreateView(generic.CreateView):
    template_name = 'user/user_create.html'
    form_class = CreateUser

    def get_success_url(self):
        messages.success(self.request, 'User Created Sucessfully')
        return reverse("UserList")
    
# User List View

@method_decorator(login_required, name='dispatch')
class UserListView(generic.ListView):
    template_name = "user/user_list.html"
    queryset = User.objects.all()
    context_object_name = "user"

# User Detail View


@method_decorator(login_required, name='dispatch')
class UserDetailView(generic.DetailView):
    template_name = "user/user_detail.html"
    model = User

    def get_context_data(self, *args,  **kwargs):
        user = User.objects.all()
        context = super(UserDetailView, self,
                        ).get_context_data(*args, **kwargs)
        profile = get_object_or_404(User, id=self.kwargs['pk'])

        context[profile] = profile
        return context


# User Update View

@method_decorator(login_required, name='dispatch')
class UserUpdateView(generic.UpdateView):
    template_name = "user/user_update.html"
    form_class = UpdateUser
    queryset = User.objects.all()
    context_object_name = "user"

    def get_success_url(self):
        return reverse("UserList")


# User Login view

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Dashboard')
        else:
            messages.info(request, 'Username Or Password Is Incorrect')

    context = {}
    return render(request, 'registration/login.html', context)


# User Logout View

def LogoutUser(request):
    logout(request)
    return redirect('Login')


@method_decorator(login_required, name='dispatch')
class Dashboard(generic.TemplateView):
    template_name = "dashboard/dashboard.html"


@login_required
def load_emp_location(request):
    branch_id = request.GET.get('branch_id')
    location = Employee_Location.objects.filter(branch_id=branch_id)
    return render(request, 'user/location_dropdown_list.html', {'location': location})

def Dashboard(request):
    hardware = Hardware.objects.all()
    hardware_count =hardware.count()
    software = Software.objects.all()
    software_count =software.count()
    in_stock = Hardware.objects.exclude(assigned_to__id = None)
    in_stock_count =in_stock.count()    
    assign = Hardware.objects.filter(assigned_to__id = None)
    assign_count =assign.count()
    context = {
         'in_stock' : in_stock,
         'hardware' : hardware,
         'software' : software,
         'assign' : assign,
         'in_stock_count' : in_stock_count,
         'hardware_count' : hardware_count,
         'software_count' : software_count,
         'assign_count' : assign_count,
     }
    
    return render(request,'dashboard/dashboard.html', context)
