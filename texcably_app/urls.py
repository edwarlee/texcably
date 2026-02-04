from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('accounts/create-account', views.CreateAccountView.as_view(), name='create_account'),
    path('accounts/login', views.UserLoginView.as_view(), name='login'),
    path('app', views.AppIndexView.as_view(), name='app_index'),
    path('accounts/logout', views.UserLogOutView.as_view(), name='logout'),
    path('app/add/article', views.ArticleCreateView.as_view(), name='add_article'),
    path('app/add/word', views.WordCreateView.as_view(), name='add_word'),
    path('app/dictionary', views.DictionaryView.as_view(), name='dictionary'),
    path('app/articles', views.ArticleListView.as_view(), name='article_list'),
]