from django.contrib import admin

# Register your models here.
from deep_punc.models import Paragraph


class ParagraphAdmin(admin.ModelAdmin):
    list_display = ('original_text', 'processed_text', 'processing')
    list_per_page = 25


admin.site.register(Paragraph, ParagraphAdmin)