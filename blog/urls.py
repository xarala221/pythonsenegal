from django.urls import path
from .views import PostIndex, PostDetail

urlpatterns = [
	path('', PostIndex.as_view(), name='post'),
	path('<slug>/', PostDetail.as_view(), name='post-detail')
]