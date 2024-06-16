from django.contrib import admin

# Register your models here.
from .models import Question, Choice

admin.site.site_header="Poll System Admin"
admin.site.site_title="Poll System Admin Area"
admin.site.index_title="Welcom to Poll System Admim Area"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date INformation', {'fields': ['pub_date'],'classes':['collapse']}),]
    inlines = [ChoiceInline]

# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question,QuestionAdmin  )