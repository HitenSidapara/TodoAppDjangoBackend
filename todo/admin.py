from django.contrib import admin
from todo.models import Todo

# TodoAdmin Class

class TodoAdmin(admin.ModelAdmin):
    list_display = ['title','description','completed']

# Register Model Here

admin.site.register(Todo, TodoAdmin)