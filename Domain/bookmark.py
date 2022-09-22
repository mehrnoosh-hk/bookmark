from dataclasses import dataclass, field
from typing import Optional, NewType
from datetime import datetime
import itertools


class Tag:
    pass


class Repository:
    pass


URL = NewType('URL', str)

counter = itertools.count()


@dataclass()
class Bookmark:
    url: URL
    description: Optional[str] = None
    tags: Optional[list[Tag]] = None
    date: datetime = field(default_factory=datetime.now)
    idx: int = field(default_factory=lambda :next(counter))

    def save_bookmark(self, repository: Repository) -> bool:
        pass

    def update_bookmark(self, repository: Repository) -> bool:
        pass

    def delete_bookmark(self, repository: Repository) -> bool:
        pass

