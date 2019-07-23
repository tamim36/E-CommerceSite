from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Listing, Category
from cart.forms import CartAddProductForm

from .choices import price_choices, category_choices, company_choices

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings' : paged_listings
    }

    return render(request, 'listings/listings.html',context)


def category(request , categoryName):
    context = {}
    context['listings'] = Listing.objects.filter(category_ID__categoryName=categoryName)
    return render(request ,'listings/category_view.html' , context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    cart_product_form = CartAddProductForm()

    context = {
        'listing' : listing,
        'cart_product_form' : cart_product_form
    }

    return render(request, 'listings/listing.html', context)


def search(request):

    queryset_list = Listing.objects.order_by('-list_date')

    #Keywords for existing in description
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains = keywords)

    #Product for non case sensitive
    if 'product_name' in request.GET:
        product_name = request.GET['product_name']
        if product_name:
            queryset_list = queryset_list.filter(title = product_name)

    #Category for case sensitive and CATEGORY FOREIGN KEY
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            queryset_list = queryset_list.filter(category_ID__categoryName = category)
    
    #Company for equal or higher number
    if 'company' in request.GET:
        company = request.GET['company']
        if company:
            queryset_list = queryset_list.filter(companyName = company)

    #price for equal or lesss number
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte = price)


    context = {
        'price_choices' : price_choices,
        'category_choices' : category_choices,
        'company_choices' : company_choices,
        'listings' : queryset_list,
        'values' : request.GET,
    }

    return render(request, 'listings/search.html', context)
