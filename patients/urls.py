from django.urls import path
from .views import PatientList, PatientCreate, PatientDetail, PatientUpdate, PatientDelete
# from django.contrib.auth import views as auth_views
# from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', PatientList.as_view(), name='patient-list'),
    path('<int:pk>/', PatientDetail.as_view(), name='patient-detail'),
    path('atualizar/<int:pk>/', PatientUpdate.as_view(), name='patient-update'),
    path('excluir/<int:pk>/', PatientDelete.as_view(), name='patient-delete'),
    path('novo-paciente/', PatientCreate.as_view(), name='patient-create'),

    # path('login/', auth_views.LoginView.as_view(
    #     template_name='pisciculturadb/login.html'), name='url-login'),
    # path('logout/', auth_views.LogoutView.as_view(
    #     template_name='pisciculturadb/logout.html'), name='url-logout'),
    # path('perfil/', login_required(views.PerfilUsuarioView),
    #     name='url-profile'),
    # path('nova-propriedade/', login_required(
    #     views.PropriedadeAmostraCreate.as_view()), name='url-add'),
    # path('alterar-formulario/', login_required(views.PropriedadeEdit),
    #     name='url-edit'),
    # path('alterar-formulario/propriedade/<int:pk>/', login_required(
    #     views.PropriedadeAmostraUpdate.as_view()), name='url-update'),
    # path('delete/propriedade/<int:pk>/', login_required(
    #     views.PropriedadeDelete), name='url-delete'),
    # path('propriedades-cadastradas/', login_required(
    #     views.PropriedadeList.as_view()), name='url-list'),
    # path('ajax/get-geocode/', views.get_geocode, name='ajax_get_geocode'),
]