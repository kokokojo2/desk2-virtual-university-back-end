from django.contrib import admin
from django.urls import path, include
from courses.views import CourseViewSet,GradeViewSet,TaskViewSet,\
    ChapterViewSet,FacultyViewSet,DepartmentViewSet,CourseMemberViewSet,\
    AttachmentViewSet,StudentWorkViewSet
from rest_framework import routers

router = routers.DefaultRouter()
#router.register(r'courses', CourseViewSet)
#router.register(r'users', UserViewSet)
#router.register(r'groups', GroupViewSet)
router.register('faculties', FacultyViewSet)
router.register('departments', DepartmentViewSet)
router.register('courses', CourseViewSet)
router.register('course_members', CourseMemberViewSet)
router.register('tasks', TaskViewSet)
router.register('chapters', ChapterViewSet)
router.register('grades', GradeViewSet)
router.register('attachments', AttachmentViewSet)
router.register('student_works', StudentWorkViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
