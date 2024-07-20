from django.urls import path

from .api.article.BlogCreate.views import ArticleCreateView
from .api.category.CategoryCreate.views import CategoryCreateView
from .api.category.CategoryDestroy.views import CategoryDestroyView
from .api.category.CategoryDetail.views import CategoryRetrieveView
from .api.category.CategoryList.views import CategoryListView
from .api.category.CategoryUpdate.views import CategoryUpdateView

app_name = "article"

urlpatterns = [
    path('create/', ArticleCreateView.as_view(), name="article_create"),
    path('CategoryCreate/', CategoryCreateView.as_view(), name="category_create"),
    path('CategoryList/', CategoryListView.as_view(), name="category_list"),
    path('CategoryUpdate/<slug:slug>/', CategoryUpdateView.as_view(), name="category_edit"),
    path('CategoryDetail/<slug:slug>/', CategoryRetrieveView.as_view(), name="category_detail"),
    path('CategoryDelete/<slug:slug>/', CategoryDestroyView.as_view(), name="category_delete"),

]
