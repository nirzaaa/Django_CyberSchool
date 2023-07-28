from django.urls import path
from . import views as main_views
from users import views as users_views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path("", main_views.home, name="main-home"),
    path("about/", main_views.about, name="main-about"),
    # path("idor/", main_views.idor, name="idor"),
    path("sqli/", main_views.sqli, name="sqli"),
    path("idor/", PostListView.as_view(), name="idor"),
    path('idor/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('idor/new/', PostCreateView.as_view(), name='post-create'),
    path('idor/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('idor/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path("calculation/", main_views.calculation, name="calculation"),
    path("show/", main_views.show, name="show"),
    path("resume/", users_views.resume, name="resume"),
    path("ssti/", main_views.ssti, name="ssti"),
    path("home_cookie/", main_views.home_cookie, name="home_cookie"),
    path("login_cookie/", main_views.login_cookie, name="login_cookie"),
    path("logout_cookie/", main_views.logout_cookie, name="logout_cookie"),
    path('visit/', main_views.count_visit, name='visit'),
    path('lfi/', main_views.lfi, name='lfi'),
    path('sqli/', main_views.sqli, name='sqli'),
    path('ssrf/', main_views.ssrf, name='ssrf'),
    path('thisissecret/', main_views.thisissecret, name='thisissecret', kwargs={'restricted': True}),
]