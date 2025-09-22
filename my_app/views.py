from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .models import Plant
from .forms import WateringForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
class Home(LoginView):
    template_name = "home.html"


def about(request):
    return render(request, "about.html")

@login_required
def plant_index(request):
    plants = Plant.objects.filter(user=request.user)
    return render(request, "plants/index.html", {"plants": plants})

@login_required
def plant_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    watering_form = WateringForm()
    return render(
        request, "plants/detail.html", {"plant": plant, "watering_form": watering_form}
    )


class PlantCreate(LoginRequiredMixin, CreateView):
    model = Plant
    fields = ["name", "variety", "category", "date_planted"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PlantUpdate(LoginRequiredMixin, UpdateView):
    model = Plant
    fields = "__all__"


class PlantDelete(LoginRequiredMixin, DeleteView):
    model = Plant
    success_url = "/plants/"

@login_required
def add_watering(request, plant_id):
    form = WateringForm(request.POST)
    if form.is_valid():
        new_watering = form.save(commit=False)
        new_watering.plant_id = plant_id
        new_watering.save()
    return redirect("plant-detail", plant_id=plant_id)


def signup(request):
    error_message = ""
    if request.ethod == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("plant-index")
        else:
            error_message = "Invalid sign up - try again"
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "signup.html", context)
