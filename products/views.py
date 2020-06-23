from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import ListView
from .models import Product
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings

#class based view which does not take login required for configuring
#the user else takes loginrequiredmixing and also we modify settings.py for it and our urls.py
class HomePageView(ListView):
    template_name='home.html'
    model = Product
    context_object_name='products'

    def get_queryset(self):
        products = super().get_queryset()
        return products




class ProductCreateView(CreateView):
    model=Product
    template_name='create.html'
    fields=['name','age','division']
    def form_valid(self,form):
        instance=form.save(commit=False)
        instance.save()
        return redirect('home')


# in class based like this underneath you have to add form_valid method to save the form and the name of the user who was creating
# and always write pk in class based views.
class ProductUpdateView(UpdateView):
    model=Product
    template_name='update.html'
    fields=['name','age','division']
    def form_valid(self,form):
        instance=form.save()
        return redirect('/',instance.pk)



class ProductDeleteView(DeleteView):
    model=Product
    template_name='delete.html'
    fields=['name','age','division']
    success_url='/'
    # context_object_name='products'



def detail(request,product_id):
    product=get_object_or_404(Product, pk=product_id)
    return render(request,'detail.html',{'product':product})
