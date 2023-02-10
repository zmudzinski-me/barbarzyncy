from typing import Optional

from banner.models import Banner


class BannerRepository:
    @staticmethod
    def get_banner() -> Optional[Banner]:
        return Banner.objects.filter(is_active=True).first()
