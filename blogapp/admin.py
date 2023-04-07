from django.contrib import admin
from blogapp.models import Post

# Register your models here.
#admin.site.register(Post)
#defining ModelAdmin class
class PostAdmin(admin.ModelAdmin):

     list_display=['title','sdesc','det','cat','active','is_deleted']
     list_filter=['cat','active','is_deleted']

#Register model with ModelAdmin class

admin.site.register(Post,PostAdmin)

