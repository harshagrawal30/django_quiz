from django.contrib import admin

# Register your models here.
from .models import que,choice
class ChoiceInline(admin.StackedInline):
    model = choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
         ('Question expiry Date', {'fields': ['end_date']}),
        ('Question information(Edit Here too)', {'fields': ['Class','maths','science','biology','chemistry','physics'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(que, QuestionAdmin)