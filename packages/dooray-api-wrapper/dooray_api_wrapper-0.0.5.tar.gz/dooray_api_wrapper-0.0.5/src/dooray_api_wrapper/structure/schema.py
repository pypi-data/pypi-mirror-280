from .response_result import WikiPageResultItem, WikiPageResult
from typing import Optional, List


class WikiPage:
    page: WikiPageResultItem

    def __init__(self, *, page: WikiPageResultItem) -> None:
        self.page = page
        self.sub_pages: List[WikiPage] = []
