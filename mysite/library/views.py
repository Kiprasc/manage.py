from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Paslauga, Product, Fencing, QuoteInstance, Hotel
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic.edit import FormMixin
from .forms import UserUpdateForm, UserQuoteInstanceCreateForm
from django.contrib.auth.decorators import login_required

def index(request):
    num_paslaugos = Paslauga.objects.count()
    num_products = Product.objects.all()


    context = {
        "num_paslaugos": num_paslaugos,
        "num_products": num_products,
    }

    return render(request, 'index.html', context=context)


class ProductListView(generic.ListView):
    model = Product
    paginate_by = 4
    template_name = 'products.html'
    context_object_name = "products"


class FencingListView(generic.ListView):
    model = Fencing
    paginate_by = 4
    template_name = 'fencings.html'
    context_object_name = "fencings"


class PaslaugaListView(generic.ListView):
    model = Paslauga
    paginate_by = 4
    template_name = 'paslaugos.html'
    context_object_name = "paslaugos"


def search(request):
    query = request.GET.get('query')
    search_results = Paslauga.objects.filter(
        Q(title__icontains=query) | Q(summary__icontains=query) | Q(product__first_name__icontains=query) | Q(
            product__last_name__icontains=query))
    return render(request, 'search.html', context={'paslaugos': search_results, 'query': query})


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                # messages.error(request, _(f'Vartotojo vardas {username} užimtas!'))
                messages.error(request, ('Username %s already exists!') % username)
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    # messages.error(request, _(f'Vartotojas su el. paštu {email} jau užregistruotas!'))
                    messages.error(request, ('Email %s already exists!') % email)
                    return redirect('register')
                else:
                    User.objects.create_user(username=username, email=email, password=password)
                    # messages.info(request, _(f'Vartotojas {username} užregistruotas!'))
                    messages.info(request, ('User %s registered!') % username)
                    return redirect('login')
        else:
            # messages.error(request, _('Slaptažodžiai nesutampa!'))
            messages.error(request, ('Passwords do not match!'))
            return redirect('register')
    else:
        return render(request, 'registration/register.html')


@login_required
def profilis(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, "Profilis atnaujintas")
            return redirect('profilis')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
    }
    return render(request, 'profilis.html', context=context)

class UserQuoteInstanceCreateView(LoginRequiredMixin, generic.CreateView):
    model = QuoteInstance
    # fields = ['book', 'due_back', 'status']
    success_url = "/library/userquotes/"
    template_name = "user_quoteinstance_form.html"
    form_class = UserQuoteInstanceCreateForm

    def form_valid(self, form):
        form.instance.reader = self.request.user
        form.save()
        return super().form_valid(form)



def display_hotel_images(request):
    if request.method == 'GET':
        Hotels = Hotel.objects.all()
        return render(request, 'display_hotel_images.html', {'hotel_images': Hotels})

