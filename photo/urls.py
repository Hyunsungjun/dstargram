from django.urls import path
from django.views.generic.detail import DetailView
from .views import *
from .models import Photo

app_name = 'photo'#네임스페이스로 사용된 값이다 앱네임=유알엘패턴이름 형태로 사용한다 

urlpatterns = [
    path('', photo_list, name='photo_list'),
    path('detail/<int:pk>/', DetailView.as_view(model=Photo, template_name='photo/detail.html'), name='photo_detail'), #디테일은 유알엘에서 인라인코드로 작성이 가능하다 
    path('upload/', PhotoUploadView.as_view(), name='photo_upload'),
    path('delete/<int:pk>/', PhotoDeleteView.as_view(), name='photo_delete'),
    path('update/<int:pk>/', PhotoUpdateView.as_view(), name='photo_update'),
]
