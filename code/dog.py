class Dog():
    def __init__(self, times=3):
        self.times = times

    def bark(self):
        print('woof ' * self.times)


if __name__ == '__main__':
    dog = Dog(6)
    dog.bark()
