from django.shortcuts import render, get_object_or_404

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Car
# Create your views here.

def cars(request):
    cars_queryset = Car.objects.order_by('-created_at')
    paginator = Paginator(cars_queryset, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    model_search=Car.objects.values_list('model', flat=True).distinct()
    city_search=Car.objects.values_list('city', flat=True).distinct()
    year_search=Car.objects.values_list('year', flat=True).distinct()
    body_style_search=Car.objects.values_list('body_style', flat=True).distinct()

    context = {
        'cars': paged_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'cars/cars.html', context=context)


def car_details(request, id):
    car = get_object_or_404(Car, pk=id)

    context = {
        'car_details': car,
    }

    return render(request, 'cars/car_details.html', context=context)

def search(request):
    cars = Car.objects.order_by('-created_at')
    model_search=Car.objects.values_list('model', flat=True).distinct()
    city_search=Car.objects.values_list('city', flat=True).distinct()
    year_search=Car.objects.values_list('year', flat=True).distinct()
    body_style_search=Car.objects.values_list('body_style', flat=True).distinct()
    transmission_search=Car.objects.values_list('transmission', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']

        if keyword:
           cars = cars.filter(description__icontains=keyword)
    
    if 'model' in request.GET:
        model = request.GET['model']

        if model:
           cars = cars.filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']

        if city:
           cars = cars.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']

        if year:
           cars = cars.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']

        if body_style:
           cars = cars.filter(body_style__iexact=body_style)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']

        if min_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    if 'transmission' in request.GET:
        transmission = request.GET['transmission']

        if transmission:
            cars = cars.filter(transmission__iexact=transmission)

    context = {
        'car_list': cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'transmission_search':transmission_search,
    }
    return render(request, 'cars/search_page.html', context=context)
