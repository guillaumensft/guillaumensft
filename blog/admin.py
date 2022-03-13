from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.

from .models import Article, Category, UserProfile

class ArticleInline(admin.TabularInline):
    model = Article

class CategoryAdmin(admin.ModelAdmin):
    inlines = [ArticleInline]

class ArticleAdmin(ImportExportModelAdmin):
    list_display = ['id', 'titre', 'content',
                    'published', 'author']

admin.site.register(UserProfile)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)

