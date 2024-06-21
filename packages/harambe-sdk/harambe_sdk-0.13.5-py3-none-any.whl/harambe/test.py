
import asyncio
from typing import Any

from playwright.async_api import Page

from harambe import SDK


async def scrape(sdk: SDK, current_url: str, *args: Any, **kwargs: Any) -> None:
    page: Page = sdk.page
    await page.wait_for_selector("#main_code")

    rows = await page.query_selector_all("ul.code-list .title-result-item-code a")
    for row in rows:
        title = await row.inner_text()
        href = await row.get_attribute("href")
        code = href.split("/")[-1]
        document_url = f"https://www.legifrance.gouv.fr/download/file/pdf/{code}.pdf/LEGI"
        await sdk.save_data({"title": title, "document_url": document_url})

if __name__ == "__main__":
    asyncio.run(SDK.run(scrape, "https://www.legifrance.gouv.fr/liste/code?etatTexte=VIGUEUR&etatTexte=VIGUEUR_DIFF&page=1#code stage", {"title": {"type": "string", "description": "The name of the document", "primary_key": False}, "document_url": {"type": "url", "actions": {"download": True}, "description": "A link to the document", "primary_key": False}}))
