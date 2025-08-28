from django.shortcuts import render
from travello.models import Destination
# Create your views here.
def index(request):

    # dest1=Destination()
    # dest1.name="Aakash"
    # dest1.desc="He is a good boy"
    # dest1.price=1000
    # dest1.img='destination_5.jpg'
    # dest1.offer=False

    # dest2=Destination()
    # dest2.name="Govinda"
    # dest2.desc="He is a gandey"
    # dest2.price=700
    # dest2.img='destination_6.jpg'
    # dest2.offer=True

    # dest3=Destination()
    # dest3.name="Payal"
    # dest3.desc="He is a good girl"
    # dest3.price=600
    # dest3.img='destination_7.jpg'
    # dest3.offer=False

    # dest4=Destination()
    # dest4.name="Nisha"
    # dest4.desc="He is a girl not good girl"
    # dest4.price=900
    # dest4.img='destination_8.jpg'
    # dest4.offer=False
    
    # dests=[dest1,dest2,dest3,dest4]

    dests=Destination.objects.all()
    
    return render(request, 'index.html',{'dests':dests})