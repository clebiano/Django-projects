from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import Patient
from .forms import PatientForm


class PatientList(ListView):
    model = Patient
    paginate_by = '10'

    def get_queryset(self):
        search = self.request.GET.get('search')
        if search:
            patients = Patient.objects.filter(id__icontains=search)
        else:
            patients = Patient.objects.all()
        return patients


class PatientDetail(DetailView):
    model = Patient


class PatientCreate(CreateView):
    model = Patient
    form_class = PatientForm
    success_url = reverse_lazy('patient-create')


class PatientUpdate(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patients/patient_update_form.html'
    success_url = reverse_lazy('patient-list')


class PatientDelete(DeleteView):
    model = Patient
    success_url = reverse_lazy('patient-list')
