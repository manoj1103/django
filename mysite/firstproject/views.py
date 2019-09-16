
from django.shortcuts import render,redirect
from .forms import ItemForm
from .models import Item

# Create your views here.

def home_view(request):

	return render(request,'emp_temp/home.html',{})

def list_items(request):
	item=Item.objects.all()
	return render(request, 'emp_temp/list.html', {'item':item})

def create_item(request):
	form = ItemForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('/home/')

	return render(request,"emp_temp/items-form.html", {'form': form})

def update_item(request,id):
	item = Item.objects.get(EMP_ID=id )
	form = ItemForm(request.POST or None, instance=item)

	if form.is_valid():
		form.save()
		return redirect('/home/')

	return render(request,'emp_temp/items-form.html',{'form':form,'item':item})


def delete_item(request,id=None):
	item = Item.objects.get(EMP_ID=id)

	if request.method == 'POST':
		item.delete()
		return redirect('/home/')

	return render(request,'emp_temp/item-delete-confirm.html',{'item':item})


