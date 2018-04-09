# The first two movies (Toy Story and Avatar) were copied from the
# Nanodegree's material
# as a model to the others
#!/usr/bin/python
#coding: utf-8
import media
import fresh_tomatoes


# media.Movie receives:
#  (self, movie_title, movie_storyline, poster_image, trailer_youtube)
toy_story = media.Movie("Toy Story", "A story of a boy and his toys "
                        "that come to life",
                        # NOQA
                        "http://br.web.img3.acsta.net/medias/nmedia/18/91/05/36/20127436.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
# media.Movie receive:
#  (self, movie_title, movie_storyline, poster_image, trailer_youtube)
avatar = media.Movie("Avatar", "A marine on an alien planet",
                    # NOQA
                    "https://www.movieposter.com/posters/archive/main/98/MPW-49246",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# media.Movie receive:
#  (self, movie_title, movie_storyline, poster_image, trailer_youtube)
spawn = media.Movie("Spawn",
            "Al Simons is resurrected as Spawn, the reluctant, demonic "
            "leader of Hell's army",
            # NOQA
            "https://images-na.ssl-images-amazon.com/images/I/51BVZn%2BLCZL._SY300_.jpg",
            "https://www.youtube.com/watch?v=WukhbpAhvrc")

# media.Movie receive:
#  (self, movie_title, movie_storyline, poster_image, trailer_youtube)
donnie_darko = media.Movie("Donnie Darko", "A troubled teenager is plagued "
                            "by visions of a man in a large rabbit suit",
                            # NOQA
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BZjZlZDlkYTktMmU1My00ZDBiLWFlNjEtYTBhNjVhOTM4ZjJjXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg)",
                            "https://www.youtube.com/watch?v=ZZyBaFYFySk")

# media.Movie receive:
#  (self, movie_title, movie_storyline, poster_image, trailer_youtube)
the_mask = media.Movie("The Mask", "Bank clerk Stanley Ipkiss is transformed "
                      "into a manic superhero",
                      # NOQA
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BOWExYjI5MzktNTRhNi00Nzg2LThkZmQtYWVkYjRlYWI2MDQ4XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SY1000_CR0,0,672,1000_AL_.jpg",
                      "https://www.youtube.com/watch?v=hOqVRwGVUkA")

# media.Movie receive:
#  (self, movie_title, movie_storyline, poster_image, trailer_youtube)
v_for_vendetta = media.Movie("V for Vendetta",
                            "In a future British tyranny, a shadowy "
                            "freedom fighter, known only by the alias of "
                            "\"V\", plots to overthrow it with the help "
                            "of a young woman",
                            # NOQA
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BYzllMjJkODAtYjMwMi00YmNhLWFhYzAtZjZjODg5YzEwOGUwXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY999_CR0,0,679,999_AL_.jpg",
                            "https://www.youtube.com/watch?v=k_13fFIrhPk")

# Create the object array that will be used in the webpage
movies = [toy_story, avatar, spawn, donnie_darko, the_mask, v_for_vendetta]

# Run the open_movies_page
# If page doesn't exist, it will be created
fresh_tomatoes.open_movies_page(movies)
