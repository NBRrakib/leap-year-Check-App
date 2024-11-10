from django.shortcuts import render

# Create your views here.
# leapyear/views.py
from django.shortcuts import render
from .forms import YearForm

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def leap_year_view(request):
    result = None
    if request.method == 'POST':
        form = YearForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            result = is_leap_year(year)
    else:
        form = YearForm()

    return render(request, 'leap_year.html', {'form': form, 'result': result})
