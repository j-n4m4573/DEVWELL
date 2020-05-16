from django.contrib import admin
from .models import *



class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('tip', 'rating', 'user_name', 'comment', 'pub_date')
    list_filter = ['pub_date', 'user_name']
    search_fields = ['comment']

admin.site.register(Tip)
admin.site.register(Review, ReviewAdmin)


