from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def execute_after_migrations(sender, **kwargs):
    from artd_modules.utils import create_or_update_module_row

    create_or_update_module_row(
        slug="artd_shopify",
        name="Artd Shopify",
        description="Artd Shopify",
        version="1.1.7",
        is_plugin=False,
    )
