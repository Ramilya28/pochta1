# from django.shortcuts import render, redirect
# from django.views import View
# from .models import Client

# class ClientListView(View):
#     def get(self, request):
#         clients = Client.objects.all()
#         return render(request, 'client_list.html', {'clients': clients})

# class ClientDetailView(View):
#     def get(self, request, pk):
#         client = Client.objects.get(pk=pk)
#         return render(request, 'client_detail.html', {'client': client})

# class ClientCreateView(View):
#     def get(self, request):
#         return render(request, 'client_create_form.html')

#     def post(self, request):
#         # Обработка данных формы для создания клиента
#         return redirect('client_list')

# class ClientUpdateView(View):
#     def get(self, request, pk):
#         client = Client.objects.get(pk=pk)
#         return render(request, 'client_update_form.html', {'client': client})

#     def post(self, request, pk):
#         # Обработка данных формы для обновления клиента
#         return redirect('client_list')

# class ClientDeleteView(View):
#     def get(self, request, pk):
#         client = Client.objects.get(pk=pk)
#         return render(request, 'client_delete_confirm.html', {'client': client})

#     def post(self, request, pk):
#         client = Client.objects.get(pk=pk)
#         client.delete()
#         return redirect('client_list')

from django.views.generic import ListView
from .models import Client  # Предположим, что у вас есть модель Client

class ClientListView(ListView):
    model = Client
    template_name = 'client/client_list.html'
    context_object_name = 'clients'
