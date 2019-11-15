from django.contrib import admin
from django.urls import  re_path, path, include
from graphene_django.views import GraphQLView
from photoblog.schema import schema
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
