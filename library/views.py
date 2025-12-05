from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView
from .forms import BookInquiryForm
from django.db.models import Q

# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'library/book_list.html'
    paginate_by = 6
    ordering = 'title'

    def get_queryset(self):
        
        queryset = super().get_queryset()
        q = self.request.GET.get('q', '').strip()
        status = self.request.GET.get('status', '').strip() 

        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) | Q(author__icontains=q)
            )
        if status == 'available':
            queryset = queryset.filter(available=True)
        elif status == 'unavailable':
            queryset = queryset.filter(available=False)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_query'] = self.request.GET.get('q', '').strip()
        context['current_status'] = self.request.GET.get('status', '').strip()
        return context

class BookDetailView(DetailView):    
    model = Book
    template_name = 'library/book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = BookInquiryForm()

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = BookInquiryForm(request.POST)

        if form.is_valid():

            context = self.get_context_data()
            context['form'] = BookInquiryForm() 
            context['success'] = True
            context['submitted_data'] = form.cleaned_data 

            return self.render_to_response(context)
        
        else:
            context = self.get_context_data()
            context['form'] = form
            context['success'] = False
            return self.render_to_response(context)



# def book_list_view(request):
#     books = Book.objects.all().order_by('title')
#     paginator = Paginator(books,6)
#     page_number = request.GET.get('page')
#     try:
#         page_obj = paginator.page(page_number)
#     except PageNotAnInteger:
#         page_obj = paginator.page(1)
#     except EmptyPage:
#         page_obj = paginator.page(paginator.num_pages)

#     context ={
#         'page_obj': page_obj,
#     }
#     return render(request, 'library/book_list.html', context)

def about_view(request):
    return render(request, 'library/about.html')

def home_view(request):
    return render(request, 'library/index.html')

# def book_detail_view(request, pk):
#     book = get_object_or_404(Book, pk =pk)
#     context = {
#         'book':book
#         }
#     return render(request, 'library/book_detail.html', context)



