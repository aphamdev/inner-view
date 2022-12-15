from django.forms import ModelForm
from tracker.models import Interview

class InterviewForm(ModelForm):
    class Meta:
        model = Interview
        fields = [
            "company_name",
            "industry",
            "position",
            "date",
            "time",
            "responded",
            "notes",
            "job_link",
        ]
