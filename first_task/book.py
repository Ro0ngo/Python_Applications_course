class Book:
    def __init__(self, title, author, pages, cover_filename):
        self.title = title
        self.author = author
        self.pages = pages
        self.cover_filename = cover_filename

    def get_info_string(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nPages: {self.pages}"
