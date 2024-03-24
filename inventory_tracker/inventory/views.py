from django.shortcuts import render,redirect
from django.views.generic import TemplateView, View
from django.contrib.auth import authenticate,login
from inventory_tracker.inventory.forms import AdminRegisterForm
 
class Index(TemplateView):
    template_name = 'inventory/index.html'

class SignUpView(View):
    def get(self,request):
        form = AdminRegisterForm()
        return render(request, 'inventory/signup.html' ,{'form': form})
        
    def post(self,request):
        form = AdminRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            user = authenticate(
                name = form.cleaned_data['name'],
                password = form.cleaned_data['password1']
            )

            login(request, user)
            return redirect('Index')
        
        return render(request, 'inventory/signup.html' , {'form':form})