from django.shortcuts import render,redirect
from  .models import studentdata

def home(request):
    students=studentdata.objects.all()
    context={'students': students}
    return render(request,'students/home.html',context)


def add_student(request):
    return render(request,'students/add_students.html')


def save_data(request):
    sname=request.POST.get('sname')
    cls=request.POST.get('cls')
    section=request.POST.get('section')
    school=request.POST.get('school')
    email=request.POST.get('email')
    mobile=request.POST.get('mobile')
    odia=request.POST.get('odia')
    hindi=request.POST.get('hindi')
    english=request.POST.get('english')
    maths=request.POST.get('maths')
    science=request.POST.get('science')
    social=request.POST.get('social')

    data=studentdata(
        student_name=sname,
        class_name=cls,
        section=section,
        school_name=school,
        email=email,
        mobile=mobile,
        odia_mark=odia,
        hindi_mark=hindi,
        english_mark=english,
        math_mark=maths,
        science_mark=science,
        social_mark=social
    )
    data.save()
    return redirect('/')


def update_data(request, pk):
    student=studentdata.objects.get(id=pk)
    context={'student': student}
    return render(request,'students/update_data.html',context)


def save_update_data(request,pk):
    student=studentdata.objects.get(id=pk)
    student.student_name=request.POST.get('sname')
    student.class_name=request.POST.get('cls')
    student.section=request.POST.get('section')
    student.school_name=request.POST.get('school')
    student.email=request.POST.get('email')
    student.mobile=request.POST.get('mobile')
    student.odia_mark=request.POST.get('odia')
    student.hindi_mark=request.POST.get('hindi')
    student.english_mark=request.POST.get('english')
    student.math_mark=request.POST.get('maths')
    student.science_mark=request.POST.get('science')
    student.social_mark=request.POST.get('social')
    student.save()
    return redirect('/')


def delete_data(request,pk):
    student=studentdata.objects.get(id=pk)
    student.delete()
    return redirect('/')