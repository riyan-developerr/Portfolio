# Magic methods = Dunder methods __init__, __getitem__ etc
# they are automatically called behind the scenes as built-in 
# they help programmers to customize the objects

# NOTE : Just like operator overloading in c++
class Books:
    count = 0
    def __init__(self , title , author , pages):
        self.title = title
        self.author = author
        self.pages = pages
        Books.count += 1
        
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __eq__(self , other):
        return self.title == other.title and self.author == other.author
    # __ls__ less than
    # __gt__ greater than
    
    def __contains__(self, item):
        if item in self.title:
            return True
    
    def __getitem__(self, key):
        if key == 'title':
            return self.title
        elif key == 'author':
            return self.author
        elif key == 'pages':
            return self.pages
        else:
            return f"key '{key}' is not found"
    
    @classmethod
    def get_count(cls):
        print(f"Total Books: {cls.count}")
        
Book1 = Books("Millionaire", "someone",223)
Book2 = Books("Millionaire fastlane", "someone",112)
        
# Books.get_count()
print(Book1)
print(Book1 == Book2)
# print("Millionaire no" in Book2)
print(Book2['location'])
    