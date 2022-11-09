from django.urls import path, include
from . import views
# from .views import PostDetailView, CommentCreateView, public_profile, CommentUpdateView, CommentDeleteView, FollowerListView, PostDeleteView, PostUpdateView, likePost, SearchListView, PostListView, ExploreListView
import notifications.urls
from .views import PostListView, PostDetailView, public_profile, ProfileDetailView, ProfileEditView

# second- truncated request is sent here and a match is searched for in url patterns again
urlpatterns = [
    path('posts/', PostListView.as_view(), name='klackr-home'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # path('posts/<int:pk>/likes/', views.LikeListView.as_view(), name='likes-list'),
    # path('posts/<int:pk>/likepost/', views.LikePostView.as_view(), name='likepost'),

    path('profile/', ProfileDetailView.as_view(), name='public-profile'),
    path('profile/<int:pk>/', ProfileEditView.as_view(), name='edit-profile'),
    # path('profile/<str:username>/followers/', views.
    #      FollowerListView.as_view(), name='follower-list'),
    # path('profile/<str:username>/following/', views.
    #      FollowerListView.as_view(), name='following-list'),



    # path('about/us/', views.aboutUs, name='klackr-about-us'),
    # path('about/jobs/', views.aboutJobs, name='klackr-about-jobs'),
    # path('about/', views.redirectAboutView, name='klackr-about-us-redirect'),
    # path('explore/', ExploreListView.as_view(), name='klackr-explore'),
    # path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    # path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    # path('comment/<int:pk>/', CommentCreateView.as_view(), name='comment-form'),

    # path('search/', views.SearchListView.as_view(), name="search-list"),
    # path('likepost/', views.likePost, name='likepost'),
    # path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
]
