from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.decorators import login_required
from .models import Createlogs, Logs
from django.contrib.auth.models import User
from django.db.models import Count  

@login_required
def index(request):
    email = Logs.objects.filter(transaction = 'email').count()
    network = Logs.objects.filter(transaction = 'network').count()
    jabber = Logs.objects.filter(transaction = 'jabber').count()

    return render(request, 'admin_app/dashboard.html', {'email': email, 'network': network, 'jabber': jabber})

def tables(request):
    return render(request, 'admin_app/tables.html')

def flot(request):
    return render(request, 'admin_app/flot.html')

def morris(request):
    return render(request, 'admin_app/morris.html')

def forms(request):
    return render(request, 'admin_app/forms.html')

def panels_wells(request):
    return render(request, 'admin_app/panels_wells.html')

def buttons(request):
    return render(request, 'admin_app/buttons.html')

def notifications(request):
    return render(request, 'admin_app/notifications.html')

def typography(request):
    return render(request, 'admin_app/typography.html')

def icons(request):
    return render(request, 'admin_app/icons.html') 

def grid(request):
    return render(request, 'admin_app/grid.html')   

def blank(request):
    return render(request, 'admin_app/blank.html')

def login(request):
    return render(request, 'admin_app/login.html')    
@login_required
def create(request):
    context = {
        'logs': Logs.objects.filter(transaction='network').order_by('-logsid')[:10]
    }
   
    return render(request, 'admin_app/create.html', context)
@login_required
def network(request):
    network = {
    'networks': Logs.objects.filter(transaction='network').order_by('-logsid')[:10]
    }
   
    return render(request, 'admin_app/table_network.html', network)
    
@login_required
def jabber(request):
    jabber = {
    'jabbers': Logs.objects.filter(transaction='jabber').order_by('-logsid')[:10]
    }
   
    return render(request, 'admin_app/table_jabber.html', jabber)

@login_required
def email(request):
    email = {
    'emails': Logs.objects.filter(transaction='email').order_by('-logsid')[:10]
    }
   
    return render(request, 'admin_app/table_email.html', email)

def blank(request):
    count = Logs.objects.count()
   
   
    return render(request, 'admin_app/blank.html', {'count': count})

class LogsListView(ListView):
    model = Createlogs
    template_name = 'admin_app/dashboard.html' 

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['logs'] = Createlogs.objects.all().order_by('-logsid')[:6]
        context['countlogs'] = User.objects.annotate(total_logs = Count('createlogs'))
        context['networks'] = Createlogs.objects.exclude(network__isnull=True).exclude(network__exact='').count()
        context['emails'] = Createlogs.objects.exclude(email__isnull=True).exclude(email__exact='').count()
        context['jabbers'] = Createlogs.objects.exclude(jabber__isnull=True).exclude(jabber__exact='').count()
        return context

    
class LogsDetailView(DetailView):
    model = Createlogs   
    template_name = 'admin_app/logs-detail.html'
    context_object_name = 'logs'
    queryset = Createlogs.objects.all()


class LogsCreateView(LoginRequiredMixin, CreateView):
    model = Createlogs
    template_name = 'admin_app/createlogs_form.html'
    fields = ['name', 'job_title','transactiontype','network','jabber','email','internet','description','company','work_order','remarks']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class LogsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Createlogs
    fields = ['name', 'job_title','transactiontype','network','jabber','email','internet','description','company','work_order','remarks']


    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        logs = self.get_object()
        if self.request.user == logs.created_by:
            return True
        return False


class LogsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Createlogs
    success_url = '/'

    def test_func(self):
        logs = self.get_object()
        if self.request.user == logs.created_by:
            return True
        return False
