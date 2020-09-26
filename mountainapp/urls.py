from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # path('create/', views.create, name='create'),
    # path('profile/<str:user>',views.profile, name='profile'), #메인에서 프로필화면 가기
    # path('detail/<int:post_id>',views.detail,name='detail'), # 게시글 읽기
    # path('update_profile/<str:user>', views.update_profile, name="update_profile"),
    path("add_mountain/", views.add_mountain, name="add_mountain"),
    path('complete_climbing/<str:user>',views.complete_climbing, name='complete_climbing'), #메인에서 완등하러가기 화면
    path('search_mountain/',views.search_mountain, name='search_mountain'), #메인에서 완등하러가기 화면
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 