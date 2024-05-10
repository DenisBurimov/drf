from django.core.management.base import BaseCommand
from django.urls import URLPattern, URLResolver


def print_urls(urlpatterns, prefix=""):
    for pattern in urlpatterns:
        if isinstance(pattern, URLPattern):
            print(
                f"{prefix}{pattern.pattern} - {pattern.callback.__module__}.{pattern.callback.__name__}"
            )
        elif isinstance(pattern, URLResolver):
            print_urls(
                pattern.url_patterns, prefix=prefix + pattern.pattern.regex.pattern
            )


class Command(BaseCommand):
    help = "Display all URL patterns and their corresponding views"

    def handle(self, *args, **options):
        from django.urls import get_resolver

        resolver = get_resolver()
        print_urls(resolver.url_patterns)
