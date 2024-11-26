from django.contrib import admin
from .models import News, NewsAttachment, Category,Comment

# Inline-класс для добавления/редактирования вложений
class NewsAttachmentInline(admin.TabularInline):  # Можно использовать StackedInline для другого вида
    model = NewsAttachment
    extra = 1  # Количество пустых дополнительных полей для новых вложений
    fields = ['photo', 'caption']  # Поля для редактирования
    max_num = 10  # Максимальное количество вложений, если нужно ограничение

# Админ-класс для модели News
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'status', 'publish', 'updated']
    list_filter = ['status', 'created', 'publish', 'category']
    search_fields = ['title', 'text']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    inlines = [NewsAttachmentInline]  # Включаем inline редактирование вложений

# Регистрация модели Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'category_slug']
    prepopulated_fields = {'category_slug': ('category_name',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author','news','created','active']
    list_filter = ['active','created','updated']
    search_fields = ['author','body']