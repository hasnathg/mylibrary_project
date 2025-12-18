from django.contrib import admin
from .models import Book, BookSuggestion, BookInquiry, Category

# Register your models here.
# admin.site.register(Book)

class BookInquiryInline(admin.TabularInline):
    model = BookInquiry
    extra = 0
    readonly_fields = ('name', 'email', 'inquiry_type', 'message', 'created_at') 


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_year', 'price','available', 'categories_list')
    list_filter = ('available', 'published_year', 'categories')
    search_fields = ('title', 'author', 'description')
    filter_horizontal = ('categories',)
    inlines = [BookInquiryInline]


    def categories_list(self, obj):
        return ",".join(obj.categories.values_list("name", flat=True))
    categories_list.short_description = "Categories"


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


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields= ('name', 'slug')
    prepopulated_fields= {'slug': ('name',)}





