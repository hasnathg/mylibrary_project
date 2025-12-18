from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book, BookSuggestion, BookInquiry, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import BookInquiryForm, BookSuggestionForm
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
        category = self.request.GET.get('category', '').strip()

        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) | Q(author__icontains=q)
            )
        if status == 'available':
            queryset = queryset.filter(available=True)
        elif status == 'unavailable':
            queryset = queryset.filter(available=False)

        if category:
            queryset = queryset.filter(categories__slug=category)

        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_query'] = self.request.GET.get('q', '').strip()
        context['current_status'] = self.request.GET.get('status', '').strip()
        context['categories'] = Category.objects.order_by('name')
        context['current_category'] = self.request.GET.get('category', '').strip()

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

            inquiry = form.save(commit=False)
            inquiry.book = self.object
            inquiry.save()

            context = self.get_context_data()
            context['form'] = BookInquiryForm() 
            context['success'] = True
            return self.render_to_response(context)
        
        else:
            context = self.get_context_data()
            context['form'] = form
            context['success'] = False
            return self.render_to_response(context)
        
class BookSuggestionCreateView(CreateView):
    model = BookSuggestion
    form_class = BookSuggestionForm
    template_name = 'library/suggest_book.html'
    success_url = reverse_lazy('suggest_thanks')




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
    latest_books = Book.objects.order_by('-id')[:6]
    modern_books = Book.objects.filter(published_year__gt=2000).order_by('-published_year')[:6]

    context = {
        "latest_books": latest_books,
        "modern_books": modern_books,
    }
    return render(request, 'library/index.html', context)

def suggestion_thanks_view(request):
    return render (request, 'library/suggest_thanks.html')

# def book_detail_view(request, pk):
#     book = get_object_or_404(Book, pk =pk)
#     context = {
#         'book':book
#         }
#     return render(request, 'library/book_detail.html', context)



