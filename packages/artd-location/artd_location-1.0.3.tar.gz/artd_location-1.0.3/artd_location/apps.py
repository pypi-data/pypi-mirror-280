from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class ArtdLocationConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "artd_location"
    verbose_name = _("ARTD Location")

    def ready(self) -> None:
        print("Loading")
        from artd_modules.utils import create_or_update_module_row

        create_or_update_module_row(
            "artd_location",
            "ArtD Location",
            "ArtD location",
            "1.0.3",
            False,
        )
        print("Loaded")
        return super().ready()
