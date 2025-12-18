from django.shortcuts import render, redirect
from .models import Report
from .forms import ReportForm

def home(request):
    reports = Report.objects.all().order_by('-is_pinned', '-created_at')
    return render(request, 'main/home.html', {'reports': reports})

def submit_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ReportForm()

    return render(request, 'main/submit.html', {'form': form})
