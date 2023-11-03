from django.contrib import admin
from mysite.models import Post,Team
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=('title', 'slug', 'pub_date', 'writer')
class Teammate(admin.ModelAdmin):
    list_display=('member', )
admin.site.register(Post, PostAdmin)
admin.site.register(Team, Teammate)
