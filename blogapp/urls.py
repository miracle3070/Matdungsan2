from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('tag_search/', views.tag_search, name='tag_search'),
    path('create/', views.create, name='create'), #경로공유 등록(위도/경도 있는 모델)
    path('board_create/', views.board_create, name='board_create'), #일반 게시물
    path('profile/<str:user>',views.profile, name='profile'), #메인에서 프로필화면 가기
    path('detail/<int:post_id>',views.detail,name='detail'), # 게시글 읽기
    path('update_profile/<str:user>', views.update_profile, name="update_profile"),
    path('create_comment/<int:post_id>', views.create_comment, name="create_comment"), #댓글생성
    path('delete_comment/<int:post_id>/<int:comment_id>', views.delete_comment, name="delete_comment"),
    path('likes/', views.likes, name="likes"),
    path('follow/', views.follow, name="follow"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 