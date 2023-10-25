#!/usr/bin/env python3

class Book:
    def __init__(self,title,page_count):
        self._title = title
        if(type(page_count) != int):
            print("page_count must be an integer")
        else:
            self._page_count = page_count

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,title):
        if(type(title) != str):
            print("title must be a string")
        else:
            self._title = title

    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self,page_count):
        if(type(page_count) != int):
            print("page_count must be an integer")
        else:
            self._page_count = page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        
book = Book("The Great Gatsby", 300)
print(book)