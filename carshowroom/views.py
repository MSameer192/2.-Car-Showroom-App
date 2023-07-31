from django.shortcuts import get_object_or_404, render
from .models import *

# Create your views here.


def ShowroomListView(request):

    # Get the showrooms object
    showrooms=ShowRoom.objects.all()

    return render (request, 'carshowroom/showroom_list.html', {"showrooms":showrooms})



def ShowroomDetails(request, showroom_id): 

    # Get the showroom object with the specified ID and returning a error 404 if not found
    showroom = get_object_or_404(ShowRoom, id=showroom_id)

    # Get all brands associated with the showroom
    brands = Brand.objects.filter(showroom=showroom)

    # Get all staff members associated with the showroom
    staffs = Staff.objects.filter(showroom=showroom)

    # Create a list of tuples with brand and its models
    brands_with_models = []
    for brand in brands:
        models = Model.objects.filter(brand=brand)
        brands_with_models.append((brand, models))

    return render(request, 'carshowroom/showroom_detail.html', {
        'showroom': showroom,
        'staffs': staffs,
        'brands': brands,
        'brands_with_models': brands_with_models,

    })



def our_team(request, showroom_id):
    # Get the showroom object with the specified ID or return a 404 error if not found
    showroom = ShowRoom.objects.get(id=showroom_id)

    # Get all staff members associated with the specific showroom
    staffs = Staff.objects.filter(showroom=showroom)

    return render(request, 'carshowroom/our_team.html', {
        'showroom': showroom,
        'staffs': staffs,
    })


def car_listing(request, model_id):
    model = get_object_or_404(Model, id=model_id)
    cars = Car.objects.filter(model=model)
    model_name = model.name

    return render(request, 'carshowroom/car_listing.html', {
        'model_name': model_name,
        'cars': cars,
    })