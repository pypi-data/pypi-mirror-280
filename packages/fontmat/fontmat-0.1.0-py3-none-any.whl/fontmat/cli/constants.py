from typing import TypedDict


class Metadatum(TypedDict):
    name_id: int
    label: str


METADATA: tuple[Metadatum, ...] = (
    {"name_id": 4, "label": "Full name"},
    {"name_id": 6, "label": "PostScript name"},
    {"name_id": 16, "label": "Typographic/Preferred family name"},
    {"name_id": 5, "label": "Version"},
)
