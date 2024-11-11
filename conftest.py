from typing import Dict

import pytest
from playwright.sync_api import BrowserType, BrowserContext, Page


@pytest.fixture(scope = "session")
def context(
        browser_type: BrowserType,
        browser_type_launch_args: Dict,
        browser_context_args: Dict,
        ):
    context = browser_type.launch_persistent_context(
       "./foobar",
        **{
            **browser_type_launch_args,
            **browser_context_args,
            "locale": "de-DE",
        })
    yield context
    context.close()

    @pytest.fixture
    def page(context: BrowserContext) -> Page:
        # Create a page using the context
        return context.new_page()
