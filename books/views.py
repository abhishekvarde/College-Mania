from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Ad, Email
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.core.mail import send_mail
from SellMyBook import view
from django.contrib.auth import authenticate
# from django.http import HttpResponse

# Create your views here.


def home(request):
    search = request.GET.get('search')

    if request.user.is_authenticated:
        products = Ad.objects.exclude(owner=request.user).filter(active=True)
    else:
        products = Ad.objects.all().filter(active=True)

    if search is not None:
        products = products.filter(Q(name__icontains=search) | Q(des__icontains=search))

    paginator = Paginator(products, 6)  # Show 3 contacts per page

    page = request.GET.get('page')
    products = paginator.get_page(page)

    return render(request, "books/index.html", {'products': products, 'search': search})


def product_page(request):
    id = request.GET.get('id')
    product_details = Ad.objects.get(id=id)
    return render(request, "books/product_page.html", {"product_details": product_details})


def add(request):
    if request.user.is_authenticated:
        print("\n\n\n\n" + str(request.user))
        return render(request, "books/add1.html")
    else:
        message = "Login is must to add Ads."
        return render(request, 'login_page.html', {"messege": message})


def dataentry(request):
    if request.method == "POST":
        name = request.POST.get("name")
        des = request.POST.get("des")
        price = request.POST.get("price")
        # image = request.POST.get('image')
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)
        owner = request.user
        contact_no = request.POST.get("contact_no")
        address = request.POST.get("address")
        if name == "" or des == "" or price == "" or owner == "" or contact_no == "" or address == "":
            message = "fill all the parameters."
            return render(request, 'books/add1.html', {'message': message})
        obj = Ad(name=name, des=des, price=price, image=uploaded_file_url, owner=owner, contact_no=contact_no, address=address)
        obj.save()
    return home(request)


def remove(request):
    id = request.GET.get('id')
    fetch = Ad.objects.get(id=id)#.update(active)
    fetch.active = False
    fetch.save(update_fields=['active'])
    return myads(request)


def emailentry(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        send_mail(
            'Quick contact registered.',
            "We will contact you soon. \nYou message is below : \n" + message,
            'miniprojectsdl@gmail.com',
            [email],
            fail_silently=False,
        )
        obj = Email(name=name, email=email, message=message)
        obj.save()
    return view.home(request)


def myads(request):
    if request.user.is_authenticated:
        products = Ad.objects.filter(owner=request.user)

        paginator = Paginator(products, 6)  # Show 3 contacts per page

        page = request.GET.get('page')
        products = paginator.get_page(page)

        return render(request, "books/myads.html", {'products': products})
    else:
        messages.error(request, "You must login first.")
        return render(request, 'login_page.html')

