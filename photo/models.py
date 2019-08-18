from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Photo(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_photos') #foreignkey를 활용해서 유저 값을 받아옴 케스케이드 밑에 인자값 정리 해놨음 _name은 연결된 객체에서 하위 객체를 불러올때 사용함
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')#upload_to 사진이 업로드될 경로 사진이 업로드가 되지않으면 디폴트값으로 대체
    text = models.TextField()#문자열 길이제한 없는 박스 
    created = models.DateTimeField(auto_now_add=True)#날짜시간 
    updated = models.DateTimeField(auto_now=True)
    #CASCADE : 연결된 객체가 지워지면 해당 하위 객체도 같이 삭제된다.
    #PROTECT : 하위 객체가 남아 있다면 연결된 객체가 지워지지 않음
    # SET_NULL : 연결된 객체만 삭제하고 필드 값을 null로 설정
    #SET_DEFAULT : 연결된 객체만 삭제하고 필드 값을 설정된 기본 값으로 변경
    #set() : 연결된 객체만 삭제하고 지정한 값으로 변경
    #DO_NOTHING : 아무일도 하지 않음
    
    class Meta:
        ordering = ['-updated']#-이므로 내림차순정렬 해당 모델의 객체들을 어떤 기준으로 정렬할지(오더링)
    
    def __str__(self):
        return self.author.username + " " + self.created.strftime("%y-%m-%d-%h:%m:%s")

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[str(self.id)])
        #겟_앱솔루트_유알엘은 상세 페이지 주소를 반환하는 메서드이다. 이런주소를 만들기 위해서 리버스를 이용하는데 URL패턴 이름을 가지고 주소를 만들어주는 함수이다 상세화면 패턴을
        # 포토 디테일로 했는데 호출전까지 오류가 발생하지 않아 미리 넣어놔도 괜찮다. 마지막 아규스는 여러값을 리스트로 전달되는데 URL을 만드는 PK값을 넣음
