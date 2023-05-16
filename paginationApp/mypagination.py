from rest_framework.pagination import PageNumberPagination


class StudentpaginationNumber(PageNumberPagination):
    page_size=3
    