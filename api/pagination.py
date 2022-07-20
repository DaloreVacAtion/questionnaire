from rest_framework.pagination import PageNumberPagination
from rest_framework.views import Response


class DefaultPaginationResult(PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'pages': self.page.paginator.num_pages,
            'data': data
        })