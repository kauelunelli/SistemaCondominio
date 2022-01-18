from django.urls import path
from . import views


urlpatterns = [
    #INQUILINOS

    path('inquilinos' , views.inquilinos, name='inquilinos'),
    path('add_inquilino', views.add_inquilino, name='add_inquilino'),

    #UNIDADES

    path('unidades' , views.unidades, name='unidades'),
    path('add_unidades', views.add_unidade, name='add_unidade'),
    path('deletar_unidade/<int:id>', views.deletar_unidade, name='deletar_unidade'),

    #DESPESAS

    path('despesas' , views.despesas, name='despesas'),
    path('add_despesa', views.add_despesa, name='add_despesa'),
    path('edita_despesa/<int:id>', views.editar_despesa, name='edita_despesa'),
    path('deleta_despesa/<int:id', views.deleta_despesa, name='deleta_despesa'),






]