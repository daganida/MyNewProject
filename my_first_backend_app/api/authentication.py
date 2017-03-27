from rest_framework.authentication import BaseAuthentication


class BasicAuthentication(BaseAuthentication):

    def authenticate(self, request):
        return (True, None)
