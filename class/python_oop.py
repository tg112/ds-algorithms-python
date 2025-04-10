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


class Character:
    membership = True
    # __はdunder methodsを意味する
    def __init__(self, name: str, age: int):
        # privateを表すときは慣習として_をつける
        self._name = name
        self._age = age

    def shout(self):
        print(self)

    # 第一引数に cls を取る（これはそのメソッドがどのクラスから呼ばれたかを受け取る）
    # クラスを操作したいときや、**ファクトリーメソッド（別の形でインスタンスを生成する）**を作りたいときによく使われる
    # インスタンスにアクセスできない
    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    # 第一引数に self や cls を取らない
    # クラスやインスタンスに依存しない汎用的な関数を、クラスの中に整理しておきたいときに使う
    # classやインスタンスにアクセスできない
    @staticmethod
    def adding_things2(cls, num1, num2):
        return num1 + num2

    def speak(self):
        print(f'my name is {self._name}')

character1 = Character("John", 20)
print(Character.adding_things(1,2))
character1.speak()


class User:
    def sign_in(self):
        print('logged in')

print('inheritance')
# inheritanceは親クラスを引数で受け取る
class Wizard(User):
    def __init__(self, name: str, power: int):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name: str, num_arrows: int):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows:  arrows left-{self.num_arrows}')

wizard = Wizard('Tom', 10)
archer = Archer('sam', 15)
wizard.sign_in()
wizard.attack()
archer.sign_in()
archer.attack()
print(isinstance(wizard, User))   # True
print(isinstance(wizard, Wizard)) # True
print(isinstance(wizard, object)) # True Objectはbase class

print('Polymorphism')
wizard1 = Wizard('John', 60)
archer1 = Archer('Sammy', 35)

def player_attack(char):
    return char.attack()
player_attack(wizard1)
player_attack(archer1)
