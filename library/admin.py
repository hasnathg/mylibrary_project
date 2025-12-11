from django.contrib import admin
from .models import Book, BookSuggestion, BookInquiry

# Register your models here.
# admin.site.register(Book)

class BookInquiryInline(admin.TabularInline):
    model = BookInquiry
    extra = 0
    readonly_fields = ('name', 'email', 'inquiry_type', 'message', 'created_at') 
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_year', 'price','available')
    list_filter = ('available', 'published_year')
    search_fields = ('title', 'author', 'description')
    inlines = [BookInquiryInline]


@admin.register(BookSuggestion)
class BookSuggestionAdmin(admin.ModelAdmin):
    list_display = ('suggested_title', 'suggested_author', 'name', 'email')
    list_filter = ('status', 'created_at')
    search_fields = ('suggested_title', 'suggested_author', 'name', 'email')

@admin.register(BookInquiry)
class BookInquiryAdmin(admin.ModelAdmin):
    list_display = ('book', 'name', 'email', 'inquiry_type', 'created_at')
    list_filter = ('inquiry_type', 'created_at', 'book')
    search_fields = ('book_title', 'name', 'email')



