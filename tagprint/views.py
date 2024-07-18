from django.views.generic import ListView, CreateView 
from django.shortcuts import  get_object_or_404, redirect
from .models import NFe, Tag


class NFeListView(ListView):
    model = NFe
    template_name = 'nfe_list.html' 
    context_object_name = 'nfes'  


class GenerateTagView(CreateView):
    model = Tag
    fields = ['sequence']  
    template_name = 'generate_tag.html'  

    def form_valid(self, form):
        nfe_number = self.kwargs['nfe_number']
        nfe = get_object_or_404(NFe, number=nfe_number)
        
        quantity = form.cleaned_data['sequence']   
        
        for i in range(1, quantity + 1):
            tag = Tag(number_nfe=nfe, sequence=i)
            tag.save()

        return redirect('nfe_list')
    
class PrintTagView(ListView):
    model = Tag
    template_name = 'print_tag.html'
    context_object_name = 'tags'
    
    def get_queryset(self):
        nfe_number = self.kwargs['nfe_number']
        return Tag.objects.filter(number_nfe__number=nfe_number)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        nfe_number = self.kwargs['nfe_number']
        nfe = get_object_or_404(NFe, number=nfe_number)
        tags = Tag.objects.filter(number_nfe=nfe)
        total_tags = tags.count() 
        context['nfe'] = nfe
        context['total_tags'] = total_tags
        return context