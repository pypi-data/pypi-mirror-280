from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ArtdShopifyConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "artd_shopify"
    verbose_name = _("ArtD Shopify")

    def ready(self):
        from . import signals  # noqa: F401
