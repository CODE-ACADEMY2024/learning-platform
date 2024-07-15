# Create your views here.
# your_app/views.py
from django.shortcuts import render, redirect
from .forms import MyForm

def my_form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Do something with the data
            return redirect('success')
    else:
        form = MyForm()

    return render(request, 'your_app/form_template.html', {'form': form})
    
def success_view(request):
    return render(request, 'your_app/success.html')