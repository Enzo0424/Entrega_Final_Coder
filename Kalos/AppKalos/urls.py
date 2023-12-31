from django.urls import path, re_path
from AppKalos.views_pacientes import PacientesInicio, PacientesCreateView, PacientesDeleteView, PacientesDetailView,PacientesListView,PacientesUpdateView
from AppKalos.views_profesionales import ProfesionalesInicio, ProfesionalesListView, ProfesionalesCreateView, ProfesionalesDeleteView,ProfesionalesDetailView,ProfesionalesUpdateView
from AppKalos.views import Inicio, About
from Acceso.views import login_request, register


urlpatterns=[
    path('', Inicio.as_view(), name='Inicio'),
    path('about', About.as_view(), name='About'),
]

urlpatterns += [
    path('pacientes/', PacientesInicio.as_view(), name='Pacientes'),
    path('list/', PacientesListView.as_view(), name='List'),
    path('detalle/<int:pk>/', PacientesDetailView.as_view(), name='Detail'),
    path('nuevos/', PacientesCreateView.as_view(), name= 'New'),
    path('editar/<pk>/', PacientesUpdateView.as_view(), name='Edit'),
    path('borrar/<int:pk>/', PacientesDeleteView.as_view(), name='Delete'),
    ]

#Profesionales
urlpatterns += [

    path('profesionales', ProfesionalesInicio.as_view(), name='Profesionales'),
    path('listProf/', ProfesionalesListView.as_view(), name='ListProf'),
    path('detalleProf/<int:pk>/', ProfesionalesDetailView.as_view(), name='DetailProf'),
    path('nuevosProf/', ProfesionalesCreateView.as_view(), name= 'NewProf'),
    path('editarProf/<pk>/', ProfesionalesUpdateView.as_view(), name='EditProf'),
    path('borrarProf/<int:pk>/', ProfesionalesDeleteView.as_view(), name='DeleteProf'),
    
    ]
    
urlpatterns += [
    path('login', login_request, name="Login"),
    path('register', register, name="Register"),
]