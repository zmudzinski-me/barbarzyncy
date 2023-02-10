from typing import Any, Dict

from django.template.defaulttags import register


@register.filter
def lookup(value: Dict[str, Any], arg: str) -> Any:
    return value.get(arg) or ""
