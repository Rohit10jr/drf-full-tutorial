from rest_framework.authentication import TokenAuthentication as BaseTokenauth
from rest_framework.authtoken.models import Token
class TokenAuthentication(BaseTokenauth):
    keyword = 'Bearer'