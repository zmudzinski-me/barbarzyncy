from typing import Optional
from uuid import UUID

from blog.models import BlogPost


class BlogPostRepository:
    @staticmethod
    def get_posts(limit: Optional[int] = None):
        results = (
            BlogPost.objects.filter(is_published=True)
            .order_by(f"-{BlogPost.Fields.PUBLISHED_AT}")
            .all()
        )
        if limit:
            results = results[:limit]
        return results

    @staticmethod
    def get_by_id(id: UUID) -> BlogPost:
        return BlogPost.objects.get(id=id)
