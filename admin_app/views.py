from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.decorators import login_required
from .models import Createlogs, Logs, TblTransactionType, TblBranchCompDept
from django.contrib.auth.models import User
from django.db.models import Count  
from whitenoise.storage import CompressedManifestStaticFilesStorage

class ErrorSquashingStorage(CompressedManifestStaticFilesStorage):
    
    def url(self, name, **kwargs):
        try:
            return super(ErrorSquashingStorage, self).url(name, **kwargs)
        except ValueError:
            return name


@login_required
def test(request):
    return render(request, 'admin_app/test.html')

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


class LogsListView(LoginRequiredMixin, ListView):
    model = Createlogs
    template_name = 'admin_app/dashboard.html' 

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['logs'] = Createlogs.objects.all()
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
    fields = ['name', 'transactiontype', 'job_title','network','jabber','email','internet','Branch_Comp_Dept', 'work_order','date_created','remarks']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class LogsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Createlogs
    fields = ['name', 'transactiontype', 'job_title','network','jabber','email','internet','Branch_Comp_Dept', 'work_order','date_created','remarks']


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

def is_valid_queryparam(param):
    return param != "" and param is not None

def LogsFilterView(request):
    qs =  Createlogs.objects.all()
    transactiontype = TblTransactionType.objects.all()
    Branch_Comp_Dept = TblBranchCompDept.objects.all()
    name_contains_query = request.GET.get("name_contains")
    work_order_exact_query = request.GET.get("work_order_exact")
    name_or_doer_query = request.GET.get("name_or_doer")
    date_min = request.GET.get("date_min")
    date_max = request.GET.get("date_max")
    transaction = request.GET.get("transaction")
    company = request.GET.get("company")


    if is_valid_queryparam(name_contains_query):
        qs = qs.filter(name__icontains=name_contains_query)

    elif is_valid_queryparam(work_order_exact_query):
        qs = qs.filter(id=work_order_exact_query)

    elif is_valid_queryparam(name_or_doer_query):
        qs = qs.filter(
            Q(name__icontains=name_or_doer_query)
            | Q(created_by__username__icontains=name_or_doer_query)
        ).distinct()

    if is_valid_queryparam(date_min):
            qs = qs.filter(date_created__gte=date_min)

    if is_valid_queryparam(date_max):
        qs = qs.filter(date_created__lt=date_max)

   # if is_valid_queryparam(transaction) and transaction != "Choose..":
      #  qs = qs.filter(transactiontype__name=transaction)

  

    context = {"queryset": qs, "transactiontype": transactiontype}
    return render(request, "admin_app/logs-filter.html", context)