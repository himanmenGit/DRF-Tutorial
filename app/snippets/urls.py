from django.conf.urls import url, include
from snippets import views
from rest_framework.routers import DefaultRouter

# 라우터를 생성하고 뷰셋을 등록 합니다
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# 이제 API URL을 라우터가 자동으로 인식합니다.
# 추가로 탐색 가능한 API를 구현하기 위해 로그인에 사용할 URL은 직접 설정을 했습니다.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls'), name='rest_framework'),
]
