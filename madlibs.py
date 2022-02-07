# string concatenation (aka how to put strings together)
# suppose we want to create a string that says "subscribe to _____"

# youtuber = "Abu Horraira"   # some string variable
#
# # a few ways to do this
# print("Subscribe to " + youtuber)
# print("Subscribe to {}".format(youtuber))
#
# # most preferable
# print(f"Subscribe to {youtuber}")

# ---------  madlib  --------------

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)
