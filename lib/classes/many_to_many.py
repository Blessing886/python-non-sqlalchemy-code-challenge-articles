class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author.")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine.")
        if not isinstance(title, str) or len(title) == 0:
            raise ValueError("Title must be a non-empty string.")

        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = value

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return list({magazine.category for magazine in self.magazines()})

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Magazine name must be between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = value
    
    def articles(self):
        pass

    def contributors(self):
        return list({article.author for article in Article.all if article.magazine == self})

    def article_titles(self):
        return [article.title for article in Article.all if article.magazine == self]

    def contributing_authors(self):
        pass