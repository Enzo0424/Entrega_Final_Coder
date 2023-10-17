from django.urls import path, re_path
from AppKalos.views_pacientes import Inicio, PacientesInicio, PacientesCreateView, PacientesDeleteView, PacientesDetailView,PacientesListView,PacientesUpdateView
from AppKalos.views_profesionales import ProfesionalesInicio, ProfesionalesListView, ProfesionalesCreateView, ProfesionalesDeleteView,ProfesionalesDetailView,ProfesionalesUpdateView
from Acceso.views import login_request, register

urlpatterns = [

    path('', Inicio.as_view(), name='Inicio'),
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
         #CLASE 22 - Grabación en 1:17:44
         
         #(?P<...)le dice que van a pasar un primary key. SON Expresiones regulares.
         
         # <int:pk> --> se usa para indicar que el valor es el id o primary key. más simple que las expresiones regulares