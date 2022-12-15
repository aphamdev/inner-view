from django.shortcuts import render, get_object_or_404, redirect
from tracker.models import Interview
from django.contrib.auth.decorators import login_required
from tracker.forms import InterviewForm
from datetime import date

##########################################################################


@login_required
def interview_list(request):
    interviews = Interview.objects.all()
    today_date = date.today()
    context = {
        "interviews": interviews,
        "today_date": today_date
    }
    return render(request, "tracker/interview_list.html", context)

##########################################################################


@login_required
def show_interview(request, id):
    interview = get_object_or_404(Interview, id=id)
    context = {
        "show_interview": interview,
    }
    return render(request, "tracker/detail.html", context)

##########################################################################


@login_required
def create_interview(request):
    if request.method == "POST":
        form = InterviewForm(request.POST)
        if form.is_valid():
            interview = form.save(False)
            interview.user = request.user
            interview.save()
            form.save()
            return redirect("home")
    else:
        form = InterviewForm()

    context = {
        "form": form,
    }

    return render(request, "tracker/create.html", context)

##########################################################################

@login_required
def update_interview(request, id):
    model_instance = Interview.objects.get(id=id)
    if request.method == "POST":
        form = InterviewForm(request.POST, instance=model_instance)
        if form.is_valid():
            form.save()
            return redirect("show_interview", id=id)

    else:
        form = InterviewForm(instance=model_instance)

    context = {
        "form": form,
        "post_object": model_instance,
    }

    return render(request, "tracker/edit.html", context)
