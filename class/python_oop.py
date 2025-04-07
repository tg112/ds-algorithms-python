# classはpascal case
print("Cookie class")
class Cookie:
    # global variables
    milk = 0.5
    # Initializer (__init__)
    def __init__(self, color: str, weight: int):
        # initialize attributes
        self.color = color
        self.weight = weight

star_cookie = Cookie('red', 10)
star_cookie1 = Cookie('red', 10)
print(star_cookie.color)
print(star_cookie.weight)
print(star_cookie.milk, star_cookie1.milk, Cookie.milk)
print(star_cookie1.__dict__) # {'color': 'red', 'weight': 10}
print(Cookie.__dict__) # {'__module__': '__main__', 'milk': 0.5, '__init__': <function Cookie.__init__ at 0x10258a830>, '__dict__': <attribute '__dict__' of 'Cookie' objects>, '__weakref__': <attribute '__weakref__' of 'Cookie' objects>, '__doc__': None}

print("Youtube class")
class Youtube:
    def __init__(self, username: str, subscribers=0, subscriptions=0):
        self.username = username
        self.subscribers = subscribers
        self.subscriptions = subscriptions

    def subscribe(self, user):
        user.subscribers += 1
        self.subscriptions += 1


user1 = Youtube("Tom")
user2 = Youtube("Bob")
print(user1.username)
user1.subscribe(user2)
print(f"User 1 subscribers: {user1.subscribers})")
print(f"User 1 subscriptions: {user1.subscriptions})")
print(f"User 2 subscribers: {user2.subscribers})")
print(f"User 2 subscriptions: {user2.subscriptions})")


