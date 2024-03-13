from django.shortcuts import render, HttpResponseRedirect
from Blog.models import Post
from website.forms import contact_form, QuoteForm
import sweetify
from django.urls import reverse
from django.shortcuts import redirect


# Create your views here.
def index_view(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Quote sent!')
            # Redirect to a success page or do something else
        else:
            sweetify.error(request, 'Quote didnt send!')
    else:
        form = QuoteForm()
        
    context = {'form':form}
    return render(request, 'web/index.html', context)


def about_view(request):
    return render(request, 'web/about.html')


def contact_view(request):
    if request.method == 'POST':
        post_data = request.POST.copy()
        post_data['name'] = 'unknown'
        form = contact_form(post_data)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Submitted successfully!')     
            return redirect('website:contact')  # Redirect back to the form page
        else:
            sweetify.error(request, 'Submit failed!')
            return redirect('website:contact')  # Redirect back to the form page
    else:
        form = contact_form()
    return render(request, 'web/contact.html', {'form': form})

