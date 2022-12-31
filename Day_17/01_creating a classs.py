class User:
    def __init__(self,user_id,username):
        #constructor
        print("user is created")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self,user):
        #method
        #method always needs self as first parameter
        user.followers += 1
        self.following += 1


user_1 = User("001","angela")
user_2 = User("002","jack")
print(user_1.username)
print(user_1.id)


user_1.follow(user_2)                 #user_1 follows user_2
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

