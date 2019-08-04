from rest_framework.pagination import LimitOffsetPagination

#clase encargada de hacer paguinacion personalizada
class MyOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 10