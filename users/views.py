from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, render, reverse, redirect
from django.views import generic
from django.contrib import messages
from users.models import (User, Company,Employee_Location)
from .forms import (CreateUser, UpdateUser, CompanyForm)
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# User Create View
@method_decorator(login_required, name='dispatch')
class UserCreateView(generic.CreateView):
    template_name = 'user/user_create.html'
    form_class = CreateUser

    def get_success_url(self):
        messages.success(self.request, 'User Created Sucessfully')
        return reverse("UserList")


def Dashboard(request):
    return render(request,"dashboard/dashboard.html")
    
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
            return redirect('UserList')
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
