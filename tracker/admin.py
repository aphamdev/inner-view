from django.contrib import admin
from tracker.models import Interview, Industry

@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    list_display = [
        "company_name",
        "industry",
        "position",
        "date",
        "time",
        "notes",
        "id"
    ]

@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display =[
        "name",
        "id",
    ]
