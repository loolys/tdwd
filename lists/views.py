from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List
from django.core.exceptions import ValidationError
# Create your views here.
def home_page(request):
    return render(request, 'home.html')
    
def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'], list=list_)
        return redirect('/lists/%d/' % (list_.id,))
    return render(request, 'list.html', {'list': list_})
    
def new_list(request):
    list_ = List.objects.create()
    try:
        Item.objects.create(text=request.POST['item_text'], list=list_)
    except ValidationError:
        error_text = "You can't have an empty list item"
        return render(request, "home.html", {"error": error_text})
    return redirect('/lists/%d/' % (list_.id,))
    #return redirect('/lists/the-only-list-in-the-world/')
    
"""def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect("/lists/%d/" % (list_.id,))"""