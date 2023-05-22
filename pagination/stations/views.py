from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    with open('data-398-2018-08-30.csv', newline='', encoding='UTF-8') as csvfile:
        reader = csv.DictReader(csvfile)
        bus_stations_list = []
        for row in reader:
            bus_stations_list.append(row)
    paginator = Paginator(bus_stations_list, 10)
    page = paginator.get_page(page_number)
    context = {
         'bus_stations': bus_stations_list,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
