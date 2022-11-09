from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        nl = self.get_next_link()
        pl = self.get_previous_link()
        return Response({
            'links': {
                'next': nl[nl.find("/api"):] if nl is not None else None,
                'previous': pl[pl.find("/api"):] if pl is not None else None
            },
            'count': self.page.paginator.count,
            'results': data
        })
