from django.shortcuts import render
from django.http import HttpResponse, response
from .models import Order, Product,Contact,OrderUpdate
from math import ceil
import json
def index(request):
    products= Product.objects.all()
    allProds=[]
    catprods= Product.objects.values('category', 'id')
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1,nSlides), nSlides])

    params={'allProds':allProds }
    return render(request,"shop/index.html", params)

def about(request):
    return render(request,'shop/about.html')


def contact(request):
    if request.method=='POST':
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')

        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        success=True
        return render(request,'shop/contact.html',{'success':success})
    return render(request,'shop/contact.html')





def search(request):
    return render(request,'shop/search.html')



def productView(request,myid):
    #fetch the product using id
    product=Product.objects.filter(id=myid)

    return render(request,'shop/prodview.html',{'product':product[0]})



def checkout(request):
    if request.method=='POST':
        itemsJson=request.POST.get('itemsJson','')
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        locality=request.POST.get('locality','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zip=request.POST.get('zip','')
        address=request.POST.get('address','')
        order=Order(name=name,email=email,address=address,locality=locality,city=city,state=state,zip=zip,phone=phone,item_json=itemsJson)
        order.save()
        order_update=OrderUpdate(order_id=order.order_id,update_desc="The order has been placed")
        order_update.save()
        thank=True
        id=order.order_id
        return render(request,'shop/checkout.html',{'thank':thank,'id':id})
    return render(request,'shop/checkout.html')






def tracker(request):
    if request.method=='POST':
        orderId=request.POST.get('orderId','')
        email=request.POST.get('email','')
        # return HttpResponse(f"{orderId} and {email}")
        try:
            order=Order.objects.filter(order_id=orderId,email=email)
            if len(order)>0:
                update=OrderUpdate.objects.filter(order_id=orderId)
                updates=[]
                for item in update:
                    updates.append({'text':item.update_desc,'time':item.timestamp})
                    response=json.dumps([updates,order[0].item_json],default=str)
                return HttpResponse(response)
            else:
                return HttpResponse("{}")
                
        except Exception as e:
            return HttpResponse('{}')


    return render(request,'shop/tracker.html')














