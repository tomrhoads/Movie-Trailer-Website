import fresh_tomatoes
import media

# first Movie object constructor
empire_strikes_back = media.Movie(
    "The Empire Strikes Back",
    "1980",
    "A story of an aspiring Jedi Knight and friends",
    "https://upload.wikimedia.org/wikipedia/en/thumb/3/3c/SW_-_Empire_Strikes_Back.jpg/220px-SW_-_Empire_Strikes_Back.jpg",  # noqa
    "https://www.youtube.com/watch?v=mz_YWNhKOkM"
    )

# second Movie object constructor
saving_private_ryan = media.Movie(
    "Saving Private Ryan",
    "1998",
    "One of four brothers survive World War II",
    "https://upload.wikimedia.org/wikipedia/en/thumb/a/ac/Saving_Private_Ryan_poster.jpg/220px-Saving_Private_Ryan_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=vwAxi4A2YcY"
    )

# third Movie object constructor
the_big_lebowski = media.Movie(
    "The Big Lebowski",
    "1998",
    "The Dude needs his rug back",
    "https://upload.wikimedia.org/wikipedia/en/thumb/3/35/Biglebowskiposter.jpg/220px-Biglebowskiposter.jpg",  # noqa
    "https://www.youtube.com/watch?v=cd-go0oBF4Y"
    )

# fourth Movie object constructor
dumb_and_dumber = media.Movie(
    "Dumb and Dumber",
    "1994",
    "Two dumb guys need to return a woman her money",
    "https://upload.wikimedia.org/wikipedia/en/thumb/6/64/Dumbanddumber.jpg/198px-Dumbanddumber.jpg",  # noqa
    "https://www.youtube.com/watch?v=l13yPhimE3o"
    )

# fifth Movie object constructor
braveheart = media.Movie(
    "Braveheart",
    "1995",
    "William Wallace leads Scotland to earn their freedom",
    "https://upload.wikimedia.org/wikipedia/en/thumb/5/55/Braveheart_imp.jpg/220px-Braveheart_imp.jpg",  # noqa
    "https://www.youtube.com/watch?v=wj0I8xVTV18"
    )

# sixth Movie object constructor
gladiator = media.Movie(
    "Gladiator",
    "2000",
    "Maximus sets out to give Rome back to the people",
    "https://upload.wikimedia.org/wikipedia/en/thumb/8/8d/Gladiator_ver1.jpg/220px-Gladiator_ver1.jpg",  # noqa
    "https://www.youtube.com/watch?v=uwTKRz-WmHU"
    )

# populate movies array with Movie object variables
movies = [
    empire_strikes_back, saving_private_ryan, the_big_lebowski, dumb_and_dumber,  # noqa
    braveheart, gladiator]

# open_movies_page() function takes list of movies and generates HTML page
fresh_tomatoes.open_movies_page(movies)
