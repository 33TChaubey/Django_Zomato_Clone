from django.shortcuts import render, redirect
from food.models import Item, History, NavbarFrom
from food.forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from users.models import CusOrders, CusRatingFeedback
from django.core.paginator import Paginator

# Create your views here.

#function based index views
#----------------------------------------------------------------------
@login_required
def index(request):
    
    if request.user.is_superuser:
        itemlist = Item.objects.all()

        # for search functionality
        item_name = request.GET.get('item_name')
        if item_name != '' and item_name is not None:
            itemlist = Item.objects.filter(item_name__icontains=item_name)
            
        paginator = Paginator(itemlist, 3)
        page = request.GET.get('page')
        itemlist = paginator.get_page(page)
        
    elif request.user.is_authenticated and request.user.profile.user_type=='Rest':
        itemlist = Item.objects.filter(for_user=request.user.username)

        # for search functionality
        item_name = request.GET.get('item_name')
        if item_name != '' and item_name is not None:
            itemlist = Item.objects.filter(item_name__icontains=item_name)
            
        paginator = Paginator(itemlist, 3)
        page = request.GET.get('page')
        itemlist = paginator.get_page(page)

    elif request.user.is_authenticated and request.user.profile.user_type=='Cust':
        itemlist = Item.objects.all()

        # for search functionality
        item_name = request.GET.get('item_name')
        if item_name != '' and item_name is not None:
            itemlist = Item.objects.filter(item_name__icontains=item_name)
            
        paginator = Paginator(itemlist, 3)
        page = request.GET.get('page')
        itemlist = paginator.get_page(page)

    else:
        itemlist = Item.objects.all()

        # for search functionality
        item_name = request.GET.get('item_name')
        if item_name != '' and item_name is not None:
            itemlist = Item.objects.filter(item_name__icontains=item_name)
            
        paginator = Paginator(itemlist, 3)
        page = request.GET.get('page')
        itemlist = paginator.get_page(page)

    context = {
        'itemlist':itemlist
    }
    
    return render(request, 'food/index.html', context)

#class based index views
#----------------------------------------------------------------------
# class IndexClassView(ListView):
#     model = Item
#     context_object_name = 'itemlist'
#     template_name = 'food/index.html'

#function based detail views
#----------------------------------------------------------------------
@login_required
def detail(request, item_id):
    
    item = Item.objects.get(id=item_id)
    hist = History.objects.filter(
        prod_code = item.prod_code
    )
    crf = CusRatingFeedback.objects.filter(
        prod_code=item.prod_code
    )
    
    
    
    if request.user.profile.user_type == 'rest' or request.user.profile.user_type == 'admin':
        oco = CusOrders.objects.filter(
            prod_code = item.prod_code
        )
        
    elif request.user.profile.user_type == 'cust':
        oco = CusOrders.objects.filter(
            prod_code = item.prod_code,
            username = request.user.username    
        )
    
    context = {
        'item': item,
        'hist':hist,
        'oco':oco,
        'crf':crf
    }
    
    return render(request, 'food/detail.html', context)

#function based detail views
#----------------------------------------------------------------------

# @login_required
# class FoodDetail(DetailView):
#     model = Item
#     context_object_name = 'item'
#     template_name = 'food/detail.html'
    


#function based create item views
#----------------------------------------------------------------------
@login_required
def create_item(request):
    
    form = ItemForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    context = {
        'form': form
    }
    
    return render(request, 'food/item-form.html',context)

#function based create item views
#----------------------------------------------------------------------
@login_required
class CreateItem(CreateView):
    model = Item
    fields = ['prod_code', 'rest_owner' ,'item_name', 'item_desc', 'item_price', 'item_image']
    template_name = "food/item-form.html"
    success_url = reverse_lazy('food:index')
    
    
    
    def form_valid(self, form):
        form.instance.added_by = self.request.user.username
        
        objHist = History(
            username  = self.request.user.username,
            prod_code = self.request.POST['prod_code'],
            item_name = self.request.POST.get('item_name'),
            operation_type = 'created',
            user_type  = self.request.user.profile.user_type
        )
        
        objHist.save()
        
        
        
        return super().form_valid(form)
    
    
#function based update item views
#----------------------------------------------------------------------
@login_required
def update_item(request,item_id):
    
    item = Item.objects.get(id=item_id)
    
    form = ItemForm(request.POST or None, instance=item)
    
    if form.is_valid():
        form.save()
        objHist = History(
            username  = request.user.username,
            prod_code = request.POST['prod_code'],
            item_name = request.POST.get('item_name'),
            operation_type = 'updated',
            user_type  = request.user.profile.user_type
        )
        
        objHist.save()
        return redirect('food:index')
    
    context = {
        'form': form
    }
    
    return render(request, 'food/item-form.html',context)

#function based delete item views
#----------------------------------------------------------------------
@login_required
def delete_item(request,item_id):
    
    item = Item.objects.get(id=item_id)
    
    if request.method == 'POST':
        objHist = History(
            username  = request.user.username,
            prod_code = item.prod_code,
            item_name = item.item_name,
            operation_type = 'delete',
            user_type  = request.user.profile.user_type
        )
        
        objHist.save()
        item.delete()
        return redirect('food:index')
    
    context = {
        'item': item
    }
    
    
    return render(request, 'food/item-delete.html',context)

#Navbar Form View
#-------------------------------------------------------------------
def NavForm(request):
    
    if request.method == 'POST':
        
        path = request.POST['path_name']
        navformdata = request.POST['navformdata']
    
    obj = NavbarFrom(data=navformdata)
    obj.save()
    return redirect(str(path))


