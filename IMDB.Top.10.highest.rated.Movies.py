#IMDB Top 10 highest rated Movies
#18.03.2026

movies = [
            ("The Shawshank Redemption", "Frank Darabont", 9.3),
            ("The Godfather", "Francis Ford Coppola", 9.2),
            ("The Dark Knight", "Christopher Nolan", 9.1),
            ("The Godfather Part II", "Francis Ford Coppola", 9.0),
            ("12 Angry Men", "Sidney Lumet", 9.0),
            ("The Lord of the Rings: The Return of the King", "Peter Jackson", 9.0),
            ("Schindler's List", "Steven Spielberg", 9.0),
            ("The Lord of the Rings: The Fellowship of the Ring", "Peter Jackson", 8.9),
            ("Pulp Fiction", "Quentin Tarantino", 8.8),
            ("The Good, the Bad and the Ugly", "Sergio Leone", 8.8)
]

START_INDEX = 1
for movie_index, (title, director, rating) in enumerate(movies, START_INDEX):
    print(f"- {movie_index}. {title}, {director}, {rating}")

dir()







































































































