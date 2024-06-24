from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ArtdModulesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "artd_modules"
    verbose_name = _("Artd Modules")

    def ready(self):
        from artd_modules.utils import create_or_update_module_row

        create_or_update_module_row(
            slug="artd_modules",
            name="Artd Modules",
            description="Artd Modules",
            version="1.0.2",
            is_plugin=False,
        )
