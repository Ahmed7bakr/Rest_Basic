from django.urls import path,include
from .views import article_list,article_detail,ArticleAPIView,ArticleDetail,GenericAPIView,ArticleViewSet
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('article',ArticleViewSet,basename='article')

urlpatterns = [

    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('article/',article_list),
    path('articles/', ArticleAPIView.as_view()),
    path('generics/article/<int:id>/', GenericAPIView.as_view()),
    path('detail/<int:pk>/',article_detail),
    path('details/<int:id>/',ArticleDetail.as_view()),
]
