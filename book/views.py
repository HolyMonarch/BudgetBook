from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse
from book.models import Item


def index(request):
	dic={'Restaurant':0,'Supermarket':0,'Merchandise':0,'Gasoline':0,'Home Improvement':0,'Other':0}
	for i in Item.objects.all():
		if i.item_category == 'R':
			dic['Restaurant']+=float(i.item_price)
		if i.item_category == 'S':
			dic['Supermarket']+=float(i.item_price)
		if i.item_category == 'M':
			dic['Merchandise']+=float(i.item_price)
		if i.item_category == 'G':
			dic['Gasoline']+=float(i.item_price)
		if i.item_category == 'H':
			dic['Home Improvement']+=float(i.item_price)
		if i.item_category == 'O':
			dic['Other']+=float(i.item_price)

	dic_monthly={'Restaurant':0,'Supermarket':0,'Merchandise':0,'Gasoline':0,'Home Improvement':0,'Other':0}
	l=[i for i in Item.objects.all() if i.was_purchased_this_month==True]

	for i in l:	
		if i.item_category == 'R':
			dic_monthly['Restaurant']+=float(i.item_price)
		if i.item_category == 'S':
			dic_monthly['Supermarket']+=float(i.item_price)
		if i.item_category == 'M':
			dic_monthly['Merchandise']+=float(i.item_price)
		if i.item_category == 'G':
			dic_monthly['Gasoline']+=float(i.item_price)
		if i.item_category == 'H':
			dic_monthly['Home Improvement']+=float(i.item_price)
		if i.item_category == 'O':
			dic_monthly['Other']+=float(i.item_price)

#	context={
#		'dic':dic,
#		'l':l,
#	}

#	return render(request,'book/index.html',context)
	output = ['You spend {} on {}.'.format(dic[i],i) for i in dic.keys()]
	output.append('For this month:')
	output.extend(['You spend {} on {} this month.'.format(dic_monthly[j],j) for j in dic_monthly.keys()])
	latest_item_list = Item.objects.order_by('purchase_time')[:5]


	context={'output':output,'latest_item_list':latest_item_list}
#	return HttpResponse(output)
	return render(request,'book/index.html',context)

def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'book/detail.html', {'item': item})




