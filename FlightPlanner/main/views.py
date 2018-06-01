from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import *
import utm
# Create your views here.

def upload_file(request):
    if request.method == 'POST':
        from django.core.files import File
        try:
            k_file = request.FILES['k_file']
            new_k_file = File(k_file)
            kml_file = KMLFile.objects.create(name=str(KMLFile.objects.count()))
            kml_file.file_path.save('kmlfile{}.kml'.format(kml_file.name), new_k_file)
            return redirect(reverse("main:render_map", kwargs = {"name":kml_file.name}))
        except:
            pass
    return render(request, 'main/upload_file.html')

def render_map(request, name):
    return render(request, 'main/render_map.html', {"name":'kmlfile' + name+'.kml'})

def test(request):
    return render(request, 'main/test.html')

####################################    Main Functions    ####################################

import csv
import simplekml


def get_grid_list(x_resolution, y_resolution, x1, y1, x2, y2, x3, y3, x4, y4, GSD, pixel_to_km=0.00001, img_overlap=0.2):
    coordinates = []
    per_X = GSD * x_resolution * pixel_to_km
    per_Y = GSD * y_resolution * pixel_to_km
    y = y1
    while (y <= y3):
        x = x4
        while (x <= x2):
            coordinates.append({'X':x, 'Y':y})
            x = x - img_overlap + per_X
        y = y - img_overlap + per_Y


def generate_kml(filename):
    inputfile = csv.reader(open('coords.csv','r'))
    kml=simplekml.Kml()
    ls = kml.newlinestring(name="Journey path")

    inputfile.next()
    for row in inputfile:
		ls.coords.addcoordinates([(row[0],row[1],row[2])])
		print row[2]
    ls.extrude = 1
    ls.tessellate = 1
    ls.altitudemode = simplekml.AltitudeMode.absolute
    ls.style.linestyle.color = '7f00ffff'   #aabbggrr
    ls.style.linestyle.width = 4
    ls.style.polystyle.color = '7f00ff00'
    kml.save('fooline.kml')










