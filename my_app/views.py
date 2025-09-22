from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .models import Plant
from .forms import WateringForm


# Create your views here.
class Home(LoginView):
    template_name = "home.html"


def about(request):
    return render(request, "about.html")


def plant_index(request):
    plants = Plant.objects.all()
    return render(request, "plants/index.html", {"plants": plants})


def plant_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    watering_form = WateringForm()
    return render(
        request, "plants/detail.html", {"plant": plant, "watering_form": watering_form}
    )


class PlantCreate(CreateView):
    model = Plant
    fields = ["name", "variety", "category", "date_planted"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PlantUpdate(UpdateView):
    model = Plant
    fields = "__all__"


class PlantDelete(DeleteView):
    model = Plant
    success_url = "/plants/"


def add_watering(request, plant_id):
    form = WateringForm(request.POST)
    if form.is_valid():
        new_watering = form.save(commit=False)
        new_watering.plant_id = plant_id
        new_watering.save()
    return redirect("plant-detail", plant_id=plant_id)
