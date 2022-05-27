import sys
from urllib.parse import quote

class Login():
    def is_login(request):
        if 'member' in request.session:
            return True
        else:
            return False

    def get_login_url(request):
        if not 'member' in request.session:
            url = request.get_full_path()
            if url:
                url = quote(url, safe='')
                return '/members/login?url=' + url
            else:
                return '/members/login'
