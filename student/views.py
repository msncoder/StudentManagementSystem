from django.shortcuts import render,HttpResponse
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q,Sum

# Create your views here.

def get_student(request):
    queryset = Student.objects.all()

    

    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(
            Q(student_name__icontains = search) |
            Q(department__department__icontains = search)|
            Q(student_id__student_id__icontains = search)|
            Q(student_age__icontains = search)
                                   )

    paginator = Paginator(queryset, 10)  # Show 25 contacts per page.
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    
    return render(request,'student/students.html',{"queryset":page_obj})


def see_marks(request,student_id):
    # generate_report_card()
    queryset = SubjectMarks.objects.filter(student__student_id__student_id = student_id)
   
   
    total_marks = queryset.aggregate(total_marks = Sum('marks'))
    # current_rank = -1

    # ranks = Student.objects.annotate(marks = Sum("StudentMarks__marks")).order_by('-marks','-student_age')
    
    # i = 1
    # for rank in ranks:
    #     if student_id == rank.student_id.student_id:
    #         current_rank = i
    #         break

    #     i = i + 1
    
    return render(request,'student/see_marks.html',{'queryset':queryset,'total_marks':total_marks})