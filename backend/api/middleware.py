from django.conf import settings
from django.middleware.csrf import CsrfViewMiddleware

class CSRFExemptMiddleware(CsrfViewMiddleware):
    def process_view(self, request, view_func, view_args, view_kwargs):
        # Exempt specified URLs from CSRF checks
        path = request.path
        for exempt_url in settings.CSRF_EXEMPT_URLS:
            if path.endswith(exempt_url):
                return None  # Skip CSRF check
        return super().process_view(request, view_func, view_args, view_kwargs)