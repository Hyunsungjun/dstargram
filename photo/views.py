from django.shortcuts import render, redirect
from .models import Photo
from django.views.generic.edit import CreateView, DeleteView, UpdateView



def photo_list(request):#함수형 뷰는 기본 매개변수로 request를 설정한다. 클래스형뷰와 다르게 직접 모든기능을 처리해야된다.  
    photos = Photo.objects.all()# 목록으로 출력할 사진 객체를 불러오기 위해 Photo모델의 기본메니저인 objects를 이용해 올메소드를 호출한다 
    return render(request, 'photo/list.html', {'photos':photos}) #렌더함수로 html을 렌더하고 포토라는 템플릿 변수를 같이 전달해준다 

class PhotoUploadView(CreateView):
    model = Photo
    fields = ['photo','text']
    template_name = 'photo/upload.html'

    def form_valid(self, form): #업로드를 끝낸후 이동할 페이지를 호출
        form.instance.author_id = self.request.user.id #이 메서드를 오버라이드해서 작성자를 설정하는 기능
        if form.is_valid(): #작성자를 설정하고나면 is_valid를 이용해서 입력된 값들을 검증 이상이 없으면 저장하고 
            form.instance.save()
            return redirect('/') #이걸로 메인 페이지로 이동함 
        else:
            return self.render_to_response({'form':form}) #이상이 있으면 그대로 작성페이지에 표시 

class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = '/'#사이트 메인을 의미 
    template_name = 'photo/delete.html'

class PhotoUpdateView(UpdateView):
    model = Photo
    fields = ['photo','text']
    template_name = 'photo/update.html'

#view를 만들지 않은 이유는 다른방법을 이용할 예정이기 때문이다 