from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from posts.views import PostListCreateView, PostRetrieveUpdateView, PostModelViewSet, calculator, CalculatorAPIView
from accounts.views import login_view

router = routers.DefaultRouter()
router.register('posts', PostModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    
    path('login/', login_view),
    # path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    # path('posts/<int:pk>/', PostRetrieveUpdateView.as_view(), name='post-detail'),

    # path('calculator/', calculator, name='calculator-fbv'),
    path('calculator/', CalculatorAPIView.as_view(), name='calculator-cbv'),
]
