from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Person
from .forms import Personform
from django.db.models import Q
# Create your views here.


def person_list_view(response):
    if 'q' in response.GET:
        q=response.GET['q']
        if q =="" :
            people = Person.objects.all()
        else:
            people = Person.objects.filter(Q(first_name=q) | Q(last_name=q) | Q(email=q) | Q(phone_number=q))
    else:
        people = Person.objects.all()
    return render(response, "main/list.html",{"Person":people})

def create(response):
    if response.method == "POST":
        form = Personform(response.POST)
        if form.is_valid():
            f_n = form.cleaned_data["first_name"]
            l_n = form.cleaned_data["last_name"]
            e = form.cleaned_data["email"]
            p = form.cleaned_data["phone_number"]
            person = Person(first_name=f_n, last_name=l_n, email=e, phone_number=p)
            person.save()
        return HttpResponseRedirect("/")
    else:
        form = Personform()
    return render(response, "main/create.html", {"form" : form} )


def edit(response, id):
    person = Person.objects.get(id=id)
    init_dir = {"first_name": person.first_name,
                "last_name": person.last_name,
                "email": person.email,
                "phone_number": person.phone_number}
    if response.method == "POST":
        form = Personform(response.POST)
        if form.is_valid():
            person.first_name = form.cleaned_data["first_name"]
            person.last_name = form.cleaned_data["last_name"]
            person.email = form.cleaned_data["email"]
            person.phone_number = form.cleaned_data["phone_number"]
            person.save()
        return HttpResponseRedirect("/")
    else:
        form = Personform(initial = init_dir)
    return render(response, "main/edit.html", {"form" : form,"id":person.id} )


def delete_person(response, id):
    person = Person.objects.get(id=id)
    person.delete()
    return HttpResponseRedirect("/")

