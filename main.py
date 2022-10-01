class Movie:
    def __init__(self):
        self.name = input('enter movie name:')
        self.rate = input('enter movie rate:')
    def show_info(self):
        print(self.name, self.rate)

new_movie = Movie()
print(new_movie.name)

movies = []
movies.append(Movie())