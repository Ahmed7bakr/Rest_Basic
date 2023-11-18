from django.urls import path
from .views import article_list,article_detail,ArticleAPIView,ArticleDetail,GenericAPIView


urlpatterns = [
    path('article/',article_list),
    path('articles/', ArticleAPIView.as_view()),
    path('generics/article/<int:id>/', GenericAPIView.as_view()),
    path('detail/<int:pk>/',article_detail),
    path('details/<int:id>/',ArticleDetail.as_view()),
]
