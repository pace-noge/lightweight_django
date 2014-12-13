from django.http import HttpResponse
from django.conf import settings
from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
import sys


settings.configure(
    DEBUG=True,
    SECRET_KEY="rahasia",
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )
)

def index(request):
    return HttpResponse("Hello world")

urlpatterns = (
    url(r'^$', index),
)


application = get_wsgi_application()


if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
