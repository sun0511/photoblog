import graphene
from graphene_django.types import DjangoObjectType
from .models import Blog

class BlogType(DjangoObjectType):
    class Meta:
        model = Blog

class Query(object):
    all_blogs = graphene.List(BlogType)

    def resolve_all_blogs(self, info, **kwargs):
        return Blog.objects.all()