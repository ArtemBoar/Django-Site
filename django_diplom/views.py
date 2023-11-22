from django.shortcuts import render, redirect
from datetime import datetime
from django.views import View
from .models import Worker, Manager, Company
from .forms import AddWorkerForm, AddManagerForm, AddCompanyForm
from django import views
from .interfaces import WeatherAPI




# Register Form
class AddRegister(View):
    template_name = 'register_form.html'

    def get(self, request):
        form = AddCompanyForm()
        current_time = datetime.now()
        return render(request, self.template_name, {'form': form, 'current_time': current_time})

    def post(self, request):
        form = AddCompanyForm(request.POST)
        context = {'form': form}

        if form.is_valid():
            new_company = Company.objects.create(
                name=form.cleaned_data.get('name'),
                balance=form.cleaned_data.get('balance'),
            )
            return redirect('admin:django_diplom')

        else:
            context['errors'] = form.errors
            return render(request, self.template_name, context=context)




# BASECLASS
class BaseClass(View):
    @staticmethod
    def get_age_filter(request):
        age_from = request.GET.get('age_from')
        age_to = request.GET.get('age_to')
        language = request.GET.get('language')
        specialist = request.GET.get('specialist')
        filters = {}

        if age_from:
            filters['age__gte'] = age_from
        if age_to:
            filters['age__lte'] = age_to
        if language:
            filters['language'] = language
        if specialist:
            filters['specialist'] = specialist

        return filters



# MENU
class MainMenu(View):
 def get(self, request):
     current_time = datetime.now()
     temperature = WeatherAPI.get_weather_info()
     return render(request, 'menu.html', context={'current_time': current_time, 'temperature': temperature})




# WORKER
class WorkersDetail(View):
    def get(self, request, worker_id):
        worker = Worker.objects.get(id=worker_id)
        current_time = datetime.now()
        return render(request, 'worker_detail.html', context={'worker': worker, 'current_time': current_time})

class WorkersList(BaseClass):
    def get(self, request):
        workers = Worker.objects.all()
        current_time = datetime.now()
        age_filter = self.get_age_filter(request)
        workers = workers.filter(**age_filter)
        return render(request, 'workers_list.html', context={'workers': workers, 'current_time': current_time})


class AddWorker(View):
    template_name = 'worker_form.html'

    def get(self, request):
        form = AddWorkerForm()
        current_time = datetime.now()
        return render(request, self.template_name, {'form': form, 'current_time': current_time})

    def post(self, request):
        form = AddWorkerForm(request.POST)
        context = {'form': form}

        if form.is_valid():
            new_worker = Worker.objects.create(
                name=form.cleaned_data.get('name'),
                surname=form.cleaned_data.get('surname'),
                age=form.cleaned_data.get('age'),
                specialist=form.cleaned_data.get('specialist'),
                language=form.cleaned_data.get('language')
            )
            return redirect('admin:your_app_name_worker_changelist')

        else:
            context['errors'] = form.errors
            return render(request, self.template_name, context=context)







# MANAGER

class ManagerDetail(View):
    def get(self, request, manager_id):
        manager = Manager.objects.get(id=manager_id)
        current_time = datetime.now()
        return render(request, 'manager_detail.html', context={'manager': manager, 'current_time': current_time})

class ManagerList(BaseClass):
    def get(self, request):
        managers = Manager.objects.all()
        current_time = datetime.now()
        age_filter = self.get_age_filter(request)
        managers = managers.filter(**age_filter)
        return render(request, 'manager_list.html', context={'managers': managers, 'current_time': current_time})

class AddManager(View):
    template_name = 'manager_form.html'

    def get(self, request):
        form = AddManagerForm()
        current_time = datetime.now()
        return render(request, self.template_name, {'form': form, 'current_time': current_time})

    def post(self, request):
        form = AddManagerForm(request.POST)
        context = {'form': form}

        if form.is_valid():
            new_manager = Manager.objects.create(
                name=form.cleaned_data.get('name'),
                surname=form.cleaned_data.get('surname'),
                age=form.cleaned_data.get('age'),
            )
            return redirect('admin:your_app_name_manager_changelist')

        else:
            context['errors'] = form.errors
            return render(request, self.template_name, context=context)
















