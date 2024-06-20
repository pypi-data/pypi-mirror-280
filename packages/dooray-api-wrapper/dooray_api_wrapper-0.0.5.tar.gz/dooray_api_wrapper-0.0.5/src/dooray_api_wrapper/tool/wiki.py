from typing import Optional
from dooray_api_wrapper.structure import schema
import dooray_api_wrapper.dooray.wiki as dooray_wiki


def get_wiki_with_all_subpages(
    project_wiki_id, home_wiki_id: str
) -> Optional[schema.WikiPage]:
    page = dooray_wiki.get_wiki_page(project_wiki_id, home_wiki_id)
    subpages = dooray_wiki.get_wiki_sub_pages(project_wiki_id, home_wiki_id)
    if page is None or subpages is None:
        return None
    wiki_page = schema.WikiPage(page=page)
    for item in subpages.result:
        page = get_wiki_with_all_subpages(project_wiki_id, item.id)
        if page is None:
            continue
        wiki_page.sub_pages.append(page)
    return wiki_page
