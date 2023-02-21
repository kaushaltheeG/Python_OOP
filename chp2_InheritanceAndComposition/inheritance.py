
class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price

class Peridical(Publication):
    def __init__(self, title, price, publisher, period):
        super().__init__(title, price)
        self.publisher = publisher
        self.period = period

class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title,price) #these attributes will be set within publication instance 
        # self.title = title
        self.author = author
        self.pages = pages 
        # self.price = price


class Magazines(Peridical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title,publisher, price, period)
        # self.title = title
        # self.publisher = publisher
        # self.price = price 
        # self.period = period

class Newspaper(Peridical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title,publisher, price, period)
        # self.title = title
        # self.publisher = publisher
        # self.price = price 
        # self.period = period