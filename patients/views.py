from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Patient
from .forms import PatientForm


class PatientList(ListView):
    model = Patient
    context_object_name = 'patient_list'
    ordering = ['-update_date']
    paginate_by = '15'

    def get_queryset(self):
        search = self.request.GET.get('search')
        patients = Patient.objects.all().order_by('-update_date')
        if search:
            patients = Patient.objects.filter(id__icontains=search).order_by('-update_date')
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
    success_message = 'Paciente excluído com sucesso.'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PatientDelete, self).delete(request, *args, **kwargs)
