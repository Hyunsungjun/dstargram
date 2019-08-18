from django.contrib import admin
from .models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id','author','created','updated']#목록에 보일 필드 
    raw_id_fields = ['author'] #ForeignKey필드의 경우 연결된 모델의 객체 목록을 출력하고 서낵하는데 목록이 길면 불편하므로 이값을 넣으면 써넣는 혀태로 바뀌고 검색기능을 사용해서 선택 가능 
    list_filter = ['created','updated','author']# 검색기능을 통해 필드를 선택 ForeignKey는 설정할수 없다
    search_fields = ['text','created']# 모델의 기본 정렬값이 아닌 관리자 사이트에서 기본으로 사용할 정렬값을 설정한다
    ordering = ['-updated','-created']

admin.site.register(Photo, PhotoAdmin)