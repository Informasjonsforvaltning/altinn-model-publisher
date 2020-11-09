"""Module for mapping organizations from shortname."""
from dataclasses import dataclass
import json
from typing import Optional

from .shortname_orgs import shortname_orgs_json


shortname_orgs_map = json.loads(shortname_orgs_json)


@dataclass
class Organization:
    """Organization class where orgnr is the id from the norwegian registry."""

    orgnr: str
    name: str


def map_shortname_to_org(shortname: str) -> Optional[Organization]:
    """Map shortname to organization."""
    org = shortname_orgs_map.get(shortname)
    return Organization(orgnr=org["orgnr"], name=org["name"]) if org else None
