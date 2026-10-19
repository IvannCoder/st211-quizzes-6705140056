
import pytest


@pytest.fixture(params=["chrome", "firefox", "safari"])
def browser(request):
    browser_name = request.param

    # Setup: prepare the browser for the test
    print(f"\n[setup] launching {browser_name}")

    yield browser_name

    # Teardown: clean up after the test
    print(f"[teardown] closing {browser_name}")


def test_page_loads(browser):
    print(f"Testing page load on {browser}")
    assert browser is not None


def test_button_clickable(browser):
    print(f"Testing button on {browser}")
    assert len(browser) > 0
