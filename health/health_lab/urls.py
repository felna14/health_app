

from django.urls import path

from health_lab import views

urlpatterns=[
              path('',views.DeptDetail,name='DeptDetail'),
              path('<slug:c_slug>/',views.DeptDetail,name='Dept_Details'),
               path('<slug:c_slug>/<slug:doctor_slug>/',views.DocDetail,name='DocDetail')
]

