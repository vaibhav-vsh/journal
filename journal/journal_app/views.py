from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView
from django.views.generic.edit import UpdateView,DeleteView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from journal_app.forms import SignupForm,NewEntryForm
from journal_app.models import Entry
from django.views.generic.list import ListView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'journal_app/home.html'

class AboutView(TemplateView):
    template_name = 'journal_app/about.html'

class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'journal_app/signup.html'
    success_url = reverse_lazy('home')

class LoginUserView(LoginView):
    template_name = 'journal_app/login.html'

def create_entry(request):
    form = NewEntryForm()
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit = False)
            entry.author = request.user
            entry.save()
            return redirect('list')
    else:
        return render(request,'journal_app/create_entry.html',{'form':form})

class EntryList(ListView):
    model = Entry
    template_name = 'journal_app/entry_list.html'

    def get_queryset(self):
        user = self.request.user
        return Entry.objects.filter(author=user.pk).order_by('-publish_date')

class EntryEdit(UpdateView):
    model = Entry
    fields = ['title','content']
    template_name = 'journal_app/entry_edit.html'

class DeleteEntry(DeleteView):
    model = Entry
    success_url = reverse_lazy('list')
