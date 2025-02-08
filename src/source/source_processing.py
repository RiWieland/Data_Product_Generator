"""
Input for an example table:
"""

from dataclasses import dataclass

class MetadataTable:
    catalog: str
    schema: str
    tablename: str
    schema: list[tuple]
    rows_count: int

class MetadataDelta:
    path: str
    commit_history: list[tuple]

