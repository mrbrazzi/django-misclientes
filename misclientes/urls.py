####################################################################
#                MisClientes V 0.0.1                               #
#      By: Luis Miguel Pozo González luis.pozo@nauta.cu            #
#          Dennis Quesada Cruz       dcruz@pescatun.alinet.cu      #
####################################################################


from django.urls import path,include
from misclientes.views import index, ListaClientesView, addclient, addempresa, deletemodel, AddPersonaView, ClienteDetailView, EnterpriseUpdate, ClienteUpdate, ClienteDeleteView, ClienteCreateView, printToPDF, printClientList

from django.contrib.auth import views as auth_views
from misclientes.models import Enterprise


urlpatterns = [
    path('index/', index, name='index'),
    path('clientes/', ListaClientesView.as_view(), name='listaclientes'),
    path('addclientes/', addempresa, name='addclientes'),
    path('accounts/' , include('django.contrib.auth.urls' )),
	path('', auth_views.LoginView.as_view(), name='login'),
	path('delete/<id>/', deletemodel, name='delmodel'),
	path('addpersonas/', AddPersonaView.as_view(), name='addpersonas'),
	path('clientdetail/<int:pk>/', ClienteDetailView.as_view(), name='client-detail'),
	path('addpersonas/', AddPersonaView.as_view(), name='addpersonas'),
	path('editenterprise/<int:pk>/', EnterpriseUpdate.as_view(), name='edit-enterprise'),
	path('editcliente/<int:pk>/', ClienteUpdate.as_view(), name='edit-cliente'),
	path('delperson/<int:pk>/', ClienteDeleteView.as_view(), name='del-person'),
	path('createperson/<int:pk>', ClienteCreateView.as_view(), name='create-person'),
	path('printreport/<int:pk>', printToPDF, name='imprimir-ficha' ),
	path('printclientlist', printClientList, name='imprimir-todos-clientes'),

	]
