from django.contrib import admin


from .models import Item
class ItemAdmin(admin.ModelAdmin):
	list_display=['EMP_ID','EMPLOYEE_NAME','SALARY','DEPARTMENT','DOB','DOJ']
	
admin.site.register(Item,ItemAdmin)