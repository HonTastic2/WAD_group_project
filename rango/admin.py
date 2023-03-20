from django.contrib import admin
from rango.models import Movie, Page, UserProfile

class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

admin.site.register(Movie, MovieAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)

