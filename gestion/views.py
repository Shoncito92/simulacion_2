from django.shortcuts import render
from django.views import generic
from .models import Usuario, Perfil
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

def principal(request):
    # Numero de visitas a esta view, como está contado en la variable de sesión.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_visits':num_visits,
    } 

    # Carga la plantilla index.html con la información adicional en la variable context.
    return render(request, 'principal.html', context=context)
#-----------------------------------------CRUD usuario------
class usuarioListView(generic.ListView): #LISTAR
    model = Usuario
    paginate_by = 5

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(usuarioListView, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['some_data'] = 'This is just some data'
        return context 

class usuarioCreate(CreateView):#CREAR
    model = Usuario
    fields = '__all__'

class usuarioUpdate(UpdateView):#ACTUALIZAR
    model = Usuario
    fields = '__all__'

class usuarioDelete(DeleteView):#ELIMINAR
    model = Usuario
    success_url = reverse_lazy('usuarios')
#-----------------------------------------DETALLES usuario------
class usuarioDetailView(generic.DetailView): #VISTADETALLADA
    model = Usuario
#-----------------------------------------DETALLES usuario------

#-----------------------------------------CRUD perfil------
class perfilListView(generic.ListView): #LISTAR
    model = Perfil
    paginate_by = 5

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(perfilListView, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['some_data'] = 'This is just some data'
        return context 

class perfilCreate(CreateView):#CREAR
    model = Perfil
    fields = '__all__'
    initial={'Rut':'183623835'}

class perfilUpdate(UpdateView):#ACTUALIZAR
    model = Perfil
    fields = '__all__'

class perfilDelete(DeleteView):#ELIMINAR
    model = Perfil
    success_url = reverse_lazy('perfiles')
#-----------------------------------------DETALLES perfil------
class perfilDetailView(generic.DetailView): #VISTADETALLADA
    model = Perfil
#-----------------------------------------DETALLES perfil------