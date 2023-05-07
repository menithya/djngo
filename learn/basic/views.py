from django.shortcuts import render
from .models import Menu
from .forms import BookingForm

# Create your views here.

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def menu(request):
    menu_data = Menu.objects.all()
    return render(request, 'menu.html', {'menu':menu_data})

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        # import pdb
        # pdb.set_trace()
        print("Post for is called")
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}

    return render(request, 'book.html', context)

def display_menu_item(request, pk=None):
    try:
        menu_item = Menu.objects.get(pk=pk)
    except Menu.DoesNotExist:
        menu_item = ""
    # context = {"menu_item"}
    context={'menu_item':menu_item}
    return render(request,'menu_item.html',context)