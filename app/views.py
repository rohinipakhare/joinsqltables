from django.shortcuts import render
from app.models import *
# Create your views here.
def equijoins(request):
    EMPOBJECTS=Emp.objects.select_related('deptno').all()

    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2024)

    EMPOBJECTS=Emp.objects.select_related('deptno').all()

    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2024,sal__gt=2000)

    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno=10)
    
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dname='SALES')

    EMPOBJECTS=Emp.objects.select_related('deptno').filter(mgr__isnull=True)

    EMPOBJECTS=Emp.objects.select_related('deptno').filter(mgr__isnull=False)

    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=True)

    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=False)

    EMPOBJECTS=Emp.objects.select_related('deptno').filter(mgr__isnull=False,deptno=10)

    EMPOBJECTS=Emp.objects.select_related('deptno').all()

    EMPOBJECTS=Emp.objects.select_related('deptno').filter(sal__lt=3000)

    EMPBJECTS=Emp.objects.select_related('deptno').all()[:5:]

    EMPOBJECTS=Emp.objects.select_related('deptno').all()[3:5]


    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equijoins.html',d)