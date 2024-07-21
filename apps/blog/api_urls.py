from django.urls import path

from .api.article.BlogCreate.views import ArticleCreateView
from .api.article.BlogList.views import ArticleListView
from .api.article.BlogRUD.views import ArticleRUDView

from .api.category.CategoryCreate.views import CategoryCreateView
from .api.category.CategoryDestroy.views import CategoryDestroyView
from .api.category.CategoryDetail.views import CategoryRetrieveView
from .api.category.CategoryList.views import CategoryListView
from .api.category.CategoryUpdate.views import CategoryUpdateView

from .api.tag.TagCreate.views import TagCreateView
from .api.tag.TagList.views import TagListView
from .api.tag.TagRUD.views import TagRUDView

app_name = "article"

urlpatterns = [
    path('create/', ArticleCreateView.as_view(), name="article_create"),
    path('list/', ArticleListView.as_view(), name="article_list"),
    path('rud/<slug:slug>/', ArticleRUDView.as_view(), name="article_list"),

    path('CategoryCreate/', CategoryCreateView.as_view(), name="category_create"),
    path('CategoryList/', CategoryListView.as_view(), name="category_list"),
    path('CategoryUpdate/<slug:slug>/', CategoryUpdateView.as_view(), name="category_edit"),
    path('CategoryDetail/<slug:slug>/', CategoryRetrieveView.as_view(), name="category_detail"),
    path('CategoryDelete/<slug:slug>/', CategoryDestroyView.as_view(), name="category_delete"),

    path('TagCreate/', TagCreateView.as_view(), name="tag_create"),
    path('TagList/', TagListView.as_view(), name="tag_create"),
    path('TagRUD/<slug:slug>/', TagRUDView.as_view(), name="tag_rud"),

]
