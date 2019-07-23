from django.contrib import admin


from .models import Listing
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('categoryID', 'categoryName', 'description')
    list_display_links = ('categoryID', 'categoryName')
    list_filter = ('categoryName',)
    search_fields = ('categoryID', 'categoryName')
    list_per_page = 3

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','product_no', 'title', 'companyName', 'is_published', 'unit_in_stock','price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'price', 'companyName', 'unit_in_stock', 'id')
    list_per_page = 3

admin.site.register(Listing, ListingAdmin)
admin.site.register(Category, CategoryAdmin)
