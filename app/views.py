from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from datetime import datetime, time, timedelta, tzinfo

from .models import Assignment, Student


class IndexView(generic.ListView):
    model = Student
    template_name = "app/index.html"
    context_object_name = "student_list"
    def get_queryset(self):
        return Student.objects.filter()

def StudentView(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    print(f"Student {student} logged in")
    assignments = Assignment.objects.filter(students=student)
    assignment_list = assignments.order_by('-pub_date')[:10]
    print(f"{student}'s assignments are: {assignments}")
    context = {'assignment_list':assignments, 'student_name':student.name}
    return render(request, 'app/student_1.html', context)

def AssignmentView(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    now = datetime.now(timezone.utc)
    diff = assignment.due_date - now
    days = diff.days
    secs = diff.seconds

    hours = secs / 3600
    if hours < 1:
        hours = 0
    else:
        secs = secs - hours * 60

    minutes = secs / 60

    if minutes < 1:
        minutes = 0
    else:
        secs = secs - minutes * 60

    if hours < 1 and minutes < 1:
        if secs < 1:
            time = f"Overdue"
        else:
            time = f"Days: {days}, Hours: {hours}, Mins: {minutes}, Secs: {secs}"
    else:
        time = f"Days: {days}, Hours: {hours}, Mins: {minutes}"
    
    # if secs < 1:
    #     print(secs)
    #     time = f"Overdue"

    # secs = old_secs - (minutes + hours)
    # minutes = diff.minute
    # secs = diff.second
    context = {'assignment':assignment, 'diff':time, 'now': datetime.now()}
    return render(request, 'app/assignment.html', context)

# class AssignmentView(generic.ListView):
#     model = Assignment
#     template_name = "app/assignment.html"
#     context_object_name = "assignment"
#     def get_queryset(self):
#         return Assignment.objects.filter(name=get_object_or_404(Assignment, pk=pk))