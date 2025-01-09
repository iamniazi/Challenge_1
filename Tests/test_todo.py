import pytest
from pages.todo_page import TodoPage
from datetime import date, timedelta
from playwright.sync_api import sync_playwright


current_date = date.today().strftime("%Y-%m-%d")
current_date_item = f"TODO 1 - {current_date}"
url="https://todomvc.com/examples/react/dist/#/active"

tomorrow_date = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")
next_date_item = f"TODO 2 - {tomorrow_date}"

@pytest.fixture(scope="module")
def page_context():
  
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  
        context = browser.new_context(
    record_video_dir="test_execution_recording/",
    record_video_size={"width": 640, "height": 480}
)
        page = context.new_page()
        yield page
        browser.close()


@pytest.fixture(scope="module")
def todo_page(page_context):
    todo_page = TodoPage(page_context)
    todo_page.navigation(url)
    return todo_page


def test_url(todo_page):
    assert todo_page.page.url == url
    todo_page.take_snapshots("after_url_check")


def test_item_creation(todo_page):
    todo_page.take_snapshots("before_adding_items")
    todo_page.add_todo_listItems(current_date_item)
    assert todo_page.get_todo_text(0) == current_date_item
    
    todo_page.add_todo_listItems(next_date_item)
    todo_page.take_snapshots("after_adding_items")
    assert todo_page.get_todo_text(1) == next_date_item

def test_current_date_item_completed(todo_page):

    todo_page.take_snapshots("before_completing_item")
    todo_page.mark_todo_as_completed(current_date_item)
    assert todo_page.check_completed_item(current_date_item) is True
    todo_page.take_snapshots("after_completing_item")

def test_seconditem_deletion(todo_page):
    todo_page.take_snapshots("before_deleting_item")
    todo_page.delete_todolist_Items(0)
    todo_page.take_snapshots("after_deleting_item")
    assert todo_page.get_items_count() == 0
    updatedlist=todo_page.get_todo_list_text()
    assert next_date_item not in updatedlist


