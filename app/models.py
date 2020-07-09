class Source:
    '''
    News_source class that defines source objects
    '''

    def __init__(self, id, name, url, description, category):
        '''
        initilazing application

        '''
        self.id = id
        self.name = name
        self.url = url
        self.description = description
        self.category = category


class Articles:
    '''
    Article class to define Objects

    '''

    def __init__(self, author, title, description, url, urlToImage, publishedAt):
        
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        
