
from state import curr,switch,stateful,State,behavior


@stateful
class People(object): 
    class Workday(State):
        default = True
        @behavior
        def day(self):
            print('work hard')
    
    class Weekend(State):
        @behavior
        def day(self):
            print('play hard')

people = People()

while True:
    for i in range(1,8):
        if i == 6:
            switch(people,People.Weekend)
        if i == 1:
            switch(people,People.Workday)
#    people.day()

# 是python 2  中的方法。python3 不适用，可以理解思想