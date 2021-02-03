# Write a function that will remember parameters passed to it and if such parameters have already been passed - will not
# waste time on their calculation in a second time. Do not use ready-made solutions, but make yours.
# As an example, you can take the following function:
# from time import sleep
# def delayed_greeting(name):
#     sleep(5)
#     return f'Hey, {name}!'
# delayed_greeting('Bob')
# delayed_greeting('Bob')


exit()



from time import sleep

def memoize(f):
    def wrapper(name):
        if not name in f.cache:
            f.cache[name] = f(name)
        return f.cache[name]
    f.cache = {}

    return wrapper

@memoize
def delayed_greeting(name):
    sleep(5)
    return f'Hey, {name}!'

print(delayed_greeting('Bob'))
print(delayed_greeting('Bobi'))
print(delayed_greeting('Bob'))
print(delayed_greeting('Beby'))
print(delayed_greeting('Bob'))


exit()

#solution1
from time import sleep
list_optimization = []

def delayed_greeting(name):
    global list_optimization
    # list_optimization = []
    print(list_optimization)
    if name not in list_optimization:
        list_optimization.append(name)
        print('-->',list_optimization)
        sleep(5)
        return f'Hey, {name}!'

print(delayed_greeting('Bob'))
print(delayed_greeting('Bob'))


exit()
#solution2
from time import sleep

class Foo:
    list_optimization = []
    def __init__(self, name):
        self.name = name

    def delayed_greeting(self):
        if self.name not in self.list_optimization:
            self.list_optimization.append(self.name)
            sleep(5)
            return f'Hey, {self.name}!'

t = Foo('Bob')
t.delayed_greeting()
p = Foo('Bob')
p.delayed_greeting()
