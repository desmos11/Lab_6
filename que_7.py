#Create a class Book with attributes title and author. Overload the __str__()
#method to return a string representation of the Book object in the format
#"Title by Author". Test this method by printing a Book instance.

class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def __str__(self):
        return(f"the {self.title} is written by {self.author}")
    
print(book("harry potter","JK rowling"))