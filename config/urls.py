from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('photo.urls')), #''을 하면 메인페이지가 됨 
]
from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#static을 사용해서 미디어_유알엘에 해당하는 주소를 가진 요청에 대해서는 미디어_루트에서 찾아서 응답하도록 하는 구문이다 디버그모드가 트루일때만 동작합니다
