import media
import fresh_tomatoes


toy_story_synopsis = "Woody (Tom Hanks), a good-hearted cowboy doll who belongs to a young boy named Andy (John Morris), sees his position as Andy's favorite toy jeopardized when his parents buy him a Buzz Lightyear (Tim Allen) action figure. Even worse, the arrogant Buzz thinks he's a real spaceman on a mission to return to his home planet. When Andy's family moves to a new house, Woody and Buzz must escape the clutches of maladjusted neighbor Sid Phillips (Erik von Detten) and reunite with their boy."
toy_story_cast = {'Director': 'John Lasseter', 'Stars': [
    'Joss Whedon', 'Andrew Stanton', 'Joel Cohen', 'Alec Sokolow']}
toy_story = media.Movie("Toy Story",
                        "Story of a boy whose toys turn into life.",
                        "http://www.impawards.com/1995/posters/toy_story_ver1.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        toy_story_synopsis,
                        "1h 21m",
                        toy_story_cast,
                        "1995")

shawshank_redemption_synopsis = "Andy Dufresne (Tim Robbins) is sentenced to two consecutive life terms in prison for the murders of his wife and her lover and is sentenced to a tough prison. However, only Andy knows he didn't commit the crimes. While there, he forms a friendship with Red (Morgan Freeman), experiences brutality of prison life, adapts, helps the warden, etc., all in 19 years."
shawshank_redemption_cast = {'Director':'Stephen King', 'Stars': ['Morgan Freeman', 'Tim Robbins', 'Bob Gunton']}
shawshank_redemption = media.Movie("Shawshank Redemption",
                                   "Story of an innocent who is put into prison",
                                   "http://www.impawards.com/1994/posters/shawshank_redemption_ver1.jpg",
                                   "https://www.youtube.com/watch?v=6hB3S9bIaco",
                                   shawshank_redemption_synopsis,
                                   "2h 22m",
                                   shawshank_redemption_cast,
                                   "1994")

silence_of_the_lamb_synopsis = "Jodie Foster stars as Clarice Starling, a top student at the FBI's training academy. Jack Crawford (Scott Glenn) wants Clarice to interview Dr. Hannibal Lecter (Anthony Hopkins), a brilliant psychiatrist who is also a violent psychopath, serving life behind bars for various acts of murder and cannibalism. Crawford believes that Lecter may have insight into a case and that Starling, as an attractive young woman, may be just the bait to draw him out."
silence_of_the_lamb_cast = {'Director':'Jonathan Demme', 'Stars': ['Anthoy Robbins', 'Jodie Foster']}
silence_of_the_lamb = media.Movie("Silence of the lamb",
                                  "High functioning Serial Killer and a journalist",
                                  "https://i.stack.imgur.com/KYuPU.jpg",
                                  "https://www.youtube.com/watch?v=RuX2MQeb8UM",
                                  silence_of_the_lamb_synopsis,
                                  "2h 18m",
                                  silence_of_the_lamb_cast,
                                  "1991")

shutter_island = media.Movie("Shutter Island",
                             "I have still not figured out the story",
                             "http://www.impawards.com/2010/posters/shutter_island.jpg",
                             "https://www.youtube.com/watch?v=5iaYLCiq5RM",
                             silence_of_the_lamb_synopsis,
                             "2h 18m",
                             silence_of_the_lamb_cast,
                             "1991")

bahubali_2 = media.Movie("Bahubali 2",
                         "Story of a South Indian King who is almost like a superman except he can't fly and is mortal",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BYmE1MTg0MDMtZmFlMC00ZGM3LTlkYWItNzEzOWRmODlhNDQ2XkEyXkFqcGdeQXVyNzMxMzYyOTI@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
                         "https://www.youtube.com/watch?v=G62HrubdD6o",
                         silence_of_the_lamb_synopsis,
                         "2h 18m",
                         silence_of_the_lamb_cast,
                         "1991")

lion = media.Movie("Lion",
                   "Story of a lost adopted Indian Boy in Australia who reunites with his family using Google maps and scattered memory",
                   "http://www.impawards.com/2016/posters/lion_ver9_xlg.jpg",
                   "https://www.youtube.com/watch?v=-RNI9o06vqo",
                   silence_of_the_lamb_synopsis,
                   "2h 18m",
                   silence_of_the_lamb_cast,
                   "1991")

movies = [toy_story, shawshank_redemption,
          silence_of_the_lamb, shutter_island, bahubali_2, lion]
fresh_tomatoes.open_movies_page(movies)
