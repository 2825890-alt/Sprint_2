class Movies:
    def __init__(self):
        self.movies = []
    def add_movie(self, movie):
        self.movies.append(movie)
    def get_movies(self):
         return self.movies    

class Comedy (Movies):
    def add_movie(self, movie):
            super().add_movie(movie)
    def get_comedies_report(self):
        return f'Комедии: {self.movies}'
comedy1 = Comedy()
comedy1.add_movie('Большой куш')

          

class Drama (Movies):
    def add_movie(self, movie):
            super().add_movie(movie)
    def get_dramas_report(self):
        return f'Драмы: {self.movies}'   
drama1 = Drama()  
drama1.add_movie('Оружейный барон')        

print(comedy1.get_comedies_report())
print(drama1.get_dramas_report()) 