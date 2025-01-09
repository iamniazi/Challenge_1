from pages.base_page import BasePage

class TodoPage(BasePage):
   
    def __init__(self, page):
        super().__init__(page)
        self.todoitem_inputfield = ".new-todo" 
        self.todo_item_list = ".todo-list li"
        self.completed_items_filter= 'ul.filters li a[href="#/completed"]'
        self.active_items_filter = 'a[href="#/active"]'
        self.checkbox = ".toggle" 
        self.completed_items_identifier = "completed" 
        self.delete_button = ".destroy" 
        

    def add_todo_listItems(self, text: str):
        self.page.fill(self.todoitem_inputfield, text)
        self.page.press(self.todoitem_inputfield, "Enter")

    def get_todo_list_text(self):
        list_text=self.page.locator(self.todo_item_list)
        return list_text.all_inner_texts()

    def get_todo_text(self, index: int) -> str:

        return self.page.locator(self.todo_item_list).nth(index).locator("label").text_content()

    def mark_todo_as_completed(self, text: str):
        
        index = self.get_item_index_by_text(text)  # Find the index of the item
        todo_item = self.page.locator(self.todo_item_list).nth(index)  # Get the specific item
        checkbox = todo_item.locator(self.checkbox)  # Find the checkbox within the item
        checkbox.click()

    def check_completed_item(self, text: str) -> bool:
        self.page.locator(self.completed_items_filter).click()
        index = self.get_item_index_by_text(text)  # Find the index of the item
        todo_item = self.page.locator(self.todo_item_list).nth(index)  # Get the specific item
        class_attribute = todo_item.get_attribute("class")  # Get the class attribute of the item
        return self.completed_items_identifier in (class_attribute or "")

    def delete_todolist_Items(self, index: int):
        self.page.locator(self.active_items_filter).click()
        todo_item = self.page.locator(self.todo_item_list).nth(index)
        todo_item.hover() 
        delete_button = todo_item.locator(self.delete_button)
        delete_button.click()

    def get_items_count(self) -> int:
     
        return self.page.locator(self.todo_item_list).count()

    def get_item_index_by_text(self, text: str) -> int:
     
        todo_items = self.page.locator(self.todo_item_list) 
        for index in range(todo_items.count()): 
            label = todo_items.nth(index).locator('[data-testid="todo-item-label"]').text_content()
            if label.strip() == text:
             return index
        
