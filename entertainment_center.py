import fresh_tomatoes
import media

# Creates Movie instances
back_to_the_future = media.Movie("Back to the Future",
                                 "Contemporary high schooler Marty McFly (Michael J. Fox) \
                                 doesn't have the most pleasant of lives. Browbeaten by his \
                                 principal at school, Marty must also endure the acrimonious \
                                 relationship between his nerdy father (Crispin Glover)  \
                                 and his lovely mother (Lea Thompson), who in turn suffer \
                                 the bullying of middle-aged jerk Biff (Thomas F. Wilson), \
                                 Marty's dad's supervisor. The one balm in Marty's life is \
                                 his friendship with eccentric scientist Doc (Christopher \
                                 Lloyd), who at present is working on a time machine. \
                                 Accidentally zapped back into the 1950s, Marty  \
                                 inadvertently interferes with the budding  \
                                 romance of his now-teenaged parents. Our hero must \
                                 now reunite his parents-to-be, lest he cease to exist \
                                 in the 1980s. It won't be easy, especially with the loutish \
                                 Biff, now also a teenager, complicating matters. Beyond \
                                 its dazzling special effects, the best element of Back \
                                 to the Future is the performance of Michael J. Fox, \
                                 who finds himself in the quagmire of surviving the  \
                                 white-bread 1950s with a hip 1980s mindset.",
                         "http://resizing.flixster.com/por4iOTnpL-nsH4QNjvWqwBF-DA=/180x270/dkpu1ddg7pbsk.cloudfront.net/movie/11/17/38/11173852_ori.jpg",
# noqa
                                 "https://www.youtube.com/watch?v=qvsgGtivCgs",
                                 "5 out of 5!",
                                 "Robert Zemeckis")
days_of_future_past = media.Movie("X-MEN: DAYS OF FUTURE PAST",
                                  'The ultimate X-Men ensemble fights a war for \
                                   the survival of the species across two time periods \
                                   in X-MEN: DAYS OF FUTURE PAST. The beloved characters \
                                   from the original "X-Men" film trilogy join forces with \
                                   their younger selves from the past, "X-Men: First Class," \
                                   in order to change a major historical event and fight in \
                                   an epic battle that could save our future. (c) Fox',
                                  "http://resizing.flixster.com/Oi1KcdBv_gG5Xqk84faEkayyX9E=/180x270/dkpu1ddg7pbsk.cloudfront.net/movie/11/18/08/11180875_ori.jpg",
# noqa
                                  "https://www.youtube.com/watch?v=pK2zYHWDZKo",
                                  "5 out of 5!",
                                  "Bryan Singer")

big_hero_six = media.Movie("Big Hero 6",
                            "With all the heart and humor audiences expect from Walt Disney \
                            Animation Studios, \"Big Hero 6\" is an action-packed \
                            comedy-adventure about robotics prodigy Hiro Hamada, \
                            who learns to harness his genius-thanks to his brilliant \
                            brother Tadashi and their like-minded friends: adrenaline \
                            junkie Go Go Tamago, neatnik Wasabi, chemistry whiz Honey \
                            Lemon and fanboy Fred. When a devastating turn of events \
                            catapults them into the midst of a dangerous plot unfolding \
                            in the streets of San Fransokyo, Hiro turns to his closest \
                            companion-a robot named Baymax-and transforms the group into \
                            a band of high-tech heroes determined to solve the mystery. (C) \
                            Disney",
                            "http://resizing.flixster.com/-cq7-XOjuDRCHC6Wqc76NzEPx20=/180x257/dkpu1ddg7pbsk.cloudfront.net/movie/11/17/85/11178581_ori.jpg",
# noqa
                            "https://www.youtube.com/watch?v=z3biFxZIJOQ",
                            "5 out of 5!",
                            "Christ Williams"
                            )
last_five_years = media.Movie("The Last 5 Years",
                              "In this adaptation of the hit musical, The Last Five Years \
                              is a musical deconstruction of a love affair and a marriage \
                              taking place over a five year period. Jamie (Jordan), a young, \
                              talented up-and-coming Jewish novelist falls in love with \
                              Cathy (Kendrick), a Shiksa Goddess and struggling actress. \
                              Their story is told almost entirely through song. All of \
                              Cathy's songs begin at the end of their marriage and move \
                              backwards in time to the beginning of their love affair, \
                              while Jamie's songs start at the beginning of their affair \
                              and move forward to the end of their marriage. They meet \
                              in the center when Jamie proposes. (C) TWC",
                              "http://resizing.flixster.com/MjdyS6fmbAyQukXYwqtoGvs3ntw=/180x267/dkpu1ddg7pbsk.cloudfront.net/movie/11/18/90/11189084_ori.jpg",
# noqa
                              "https://www.youtube.com/watch?v=1dT0mrKzObw",
                              "5 out of 5!",
                              "Richard LaGravenese")

avenger = media.Movie("Age of Ultron",
                      "Superheroes fight together once again!",
                      "https://upload.wikimedia.org/wikipedia/en/1/1b/Avengers_Age_of_Ultron.jpg",
                      "https://www.youtube.com/watch?v=JAUoeqvedMo",
                      "5 out of 5!",
                      "Joss Whedon")


# put all the movies object into a list
movies = [back_to_the_future, 
              days_of_future_past,
              big_hero_six,
              last_five_years,
              avenger]

# run the movies page to redner the HTML      
fresh_tomatoes.open_movies_page(movies)