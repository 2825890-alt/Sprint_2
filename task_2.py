class Movies:
    def __init__(self):
        self.movies = []
    def add_movie(self, movie):
        self.movies.append(movie)
       

class Comedy (Movies):
    def __init__(self):
        super().__init__()
    def add_movie(self, movie):
        super().add_movie(movie)
        return f'Комедии: {self.movies}'


          

class Drama (Movies):
    def __init__(self):
        super().__init__()
    def add_movie(self, movie):
        super().add_movie(movie)
        return f'Драмы: {self.movies}'   
       
comedy1 = Comedy()
print(comedy1.add_movie('Большой куш'))

drama1 = Drama()
print(drama1.add_movie('Оржейный барон'))