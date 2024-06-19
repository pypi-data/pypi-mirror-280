from typing import List

from django.conf import settings
from pydantic import ValidationError

from nwon_django_seeding.typings import (
    ModelFolderMapping,
    NWONDjangoSeedingSettings,
    SeedDirectories,
)


def dummy(environment: str) -> SeedDirectories:
    return SeedDirectories(default_directory="", environment_directory="")


def dummy_files(environment: str) -> List[ModelFolderMapping]:
    return []


def set_settings() -> NWONDjangoSeedingSettings:
    """
    Parse Settings from Django settings
    """

    if not hasattr(settings, "NWON_DJANGO_SEEDING"):
        return NWONDjangoSeedingSettings(
            disable_signals_before_seeding_model=[],
            custom_seed_map={},
            directories_for_environment=dummy,
            file_directories_for_environment=dummy_files,
            default_app_name="nwon",
        )

    if isinstance(settings.NWON_DJANGO, NWONDjangoSeedingSettings):
        return settings.NWON_DJANGO

    if not isinstance(settings.NWON_DJANGO, dict):
        raise Exception(
            "The NWON_DJANGO_SEEDING settings need to be of type dict or NWONDjangoSeedingSettings"
        )

    try:
        return NWONDjangoSeedingSettings.model_validate(settings.NWON_DJANGO)
    except ValidationError as exception:
        raise Exception(
            f"Could not parse the NWON_DJANGO settings: {str(exception)}"
        ) from exception


NWON_DJANGO_SEED_SETTINGS = set_settings()
"""
Settings used withing the NWON-django-seeding package
"""

__all__ = ["NWON_DJANGO_SEED_SETTINGS"]
