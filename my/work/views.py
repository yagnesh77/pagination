from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

# Create your views here.

#
def mypost(request):
	all_post =Post.objects.all().order_by('id') # your data come in al l_post admin site data
	paginator =Paginator(all_post,2,orphans=1) # make object and then one page need 3 items data  
	page_number =request.GET.get('page') # int value or another
	page_obj =paginator.get_page(page_number) #vlaue come in page_obj  pass this in to below return render
	return render(request,'work/home.html',{'posts':page_obj})
 