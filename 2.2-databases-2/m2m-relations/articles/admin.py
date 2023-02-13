from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_count = 0
        for form in self.forms:
            data_for_validation = form.cleaned_data
            if data_for_validation and data_for_validation['is_main']:
                is_main_count += 1
        if self.forms and is_main_count == 0:
            raise ValidationError('Укажите основной раздел (тег)')
        elif is_main_count > 1:
            raise ValidationError('Основным может быть только один раздел (тег)')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


class ScopeTagInline(ScopeInline):
    verbose_name = 'Тег статьи'
    verbose_name_plural = 'Теги статьи'
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published_at']
    list_filter = ['tags']
    inlines = [ScopeTagInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']