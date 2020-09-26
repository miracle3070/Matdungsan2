from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from taggit.managers import TaggableManager

# Create your models here.
class Board(models.Model): #일반 게시물 - 내용, 해시태그, 이미지
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to = 'images/', blank=True)
    tags= TaggableManager(blank= True)

    def __str__(self):
        return self.content[:15]

# 게시물 작성할때 들어갈 내용 : 제목, 내용, 위도, 경도, 이미지, 공개유무
class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20) # 식당이름
    rating = models.FloatField() # 평점
    pub_date = models.DateTimeField('date published') # 작성 시간
    content = models.TextField() # 한줄평
    image = models.ImageField(upload_to='images/', blank=True) # 사진
    latitude = models.FloatField() # 위도
    longtitude = models.FloatField() # 경도
    like = models.ManyToManyField(User, related_name='likes', blank=True)
    tags = TaggableManager(blank=True)
    
    def __str__(self):
        return self.title
        
    def summary(self):
        return self.content[:30]

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.TextField(blank = True)
    created_at = models.DateTimeField('date published')

    def __str__(self):
        return self.content

class Profile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE) #유저랑 1:1관계
    name=models.CharField(max_length=10) #이름
    nickname=models.CharField(max_length=10) #닉네임
    gender = models.CharField(max_length=5) #성별
    age_group = models.CharField(max_length=5, blank=True) #연령대
    grade = models.CharField(max_length=15, blank=True) #등급
    image = models.ImageField(upload_to='images/',null=True, blank=True) #프로필 사진첨부
    #complete_count = models.IntegerField(default=0) 
    # 등반 완료 횟수#####################완등횟수 다음에 지울것 -> Mountain모델로 조회가능#####################
    def __str__(self):
        n_user=str(self.user)
        return n_user
 


@receiver(post_save, sender=User) #자동으로 생성
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class FollowRelation(models.Model):
    follower = models.OneToOneField(User, related_name='follower', on_delete=models.CASCADE)
    followee = models.ManyToManyField(User, related_name='followee')
    
    def __str__(self):
        return self.follower