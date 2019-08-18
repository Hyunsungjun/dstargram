from django.shortcuts import render
from .models import Photo

def photo_list(request):#함수형 뷰는 기본 매개변수로 request를 설정한다. 클래스형뷰와 다르게 직접 모든기능을 처리해야된다.  
    photos = Photo.objects.all()# 목록으로 출력할 사진 객체를 불러오기 위해 Photo모델의 기본메니저인 objects를 이용해 올메소드를 호출한다 
    return render(request,'photo/list.html', {'photos':photos})#렌더함수로 html을 렌더하고 포토라는 템플릿 변수를 같이 전달해준다 
    