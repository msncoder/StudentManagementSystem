
from django.urls import path
from .views import *
urlpatterns = [
        path('',get_student),
        path('see_marks/<student_id>/',see_marks,name="see_marks")
]
