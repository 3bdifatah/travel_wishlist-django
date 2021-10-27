from django.shortcuts import render, redirect
from .models import Place
from .forms import NewPlaceForm


# Create your views here.
def place_list(request):

    if request.method == 'POST':
        #create new place
        form = NewPlaceForm(request.POST)   #creating a form from data in the request.
        place = form.save() #creating a model object from form
        if form.is_valid(): #validation against DB constraints
            place.save()    #saves place to db
            return redirect('place_list')   #reloads home page.

    places = Place.objects.filter(visited=False).order_by('name')
    new_place_form = NewPlaceForm() #creats HTML form
    return render(request, 'travel_wishlist/wishlist.html', {'places': places, 'new_place_form': new_place_form})