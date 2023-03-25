from django.contrib import admin
from django.urls import path
from EmployeeApp import views
from .views import SignupView, LoginView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
    path('department/',views.departmentApi),
    path('department/<int:id>',views.departmentApi),
    path('employee/',views.employeeApi),
    path('employee/<int:id>',views.employeeApi),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    # path(r'^/department/([0-9]+)$',views.departmentApi),

    # path(r'^/employee$',views.employeeApi),
    # path(r'^/employee/([0-9]+)$',views.employeeApi),

    # path(r'^/employee/savefile',views.SaveFile)
]
# +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)