class Source:
    '''
    News_source class that defines source objects
    '''

    def __init__(self, id, name, category):
        '''
        initilazing application

        '''
        self.id = id
        self.name = name


class Articles:
    '''
    Article class to define Objects

    '''

    def __init__(self, author, title, description, Url, urlToImage, publishedAt, content):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
