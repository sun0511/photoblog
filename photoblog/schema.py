import graphene
from blog.schema import Query as BlogQuery

class Query(BlogQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)