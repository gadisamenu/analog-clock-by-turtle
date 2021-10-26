import datetime as dt
import turtle
import time as t

# Taking time from the system to continue counting from it
systems_time = dt.datetime.now().time()
systems_hour = systems_time.hour
systems_minute = systems_time.minute
systems_second = systems_time.second

# Ceating turtle objects
seconds = turtle.Turtle()
minutes = turtle.Turtle()
hours = turtle.Turtle()
watch = turtle.Turtle()

# Making the animation off
watch.speed(0)
seconds.speed(0)
minutes.speed(0)
hours.speed(0)

# Making the physical part of the watch
watch.ht()
watch.up()
watch.goto(0,-150)
watch.down()
watch.pensize(10)
watch.pencolor('orange')
watch.circle(150)



watch.pencolor('black')
watch.pensize(5)
watch.pu()
watch.goto(-10,128)
watch.lt(20)
watch.write(12,font=("Arial", 12, "normal"))
watch.goto(135,-6)
watch.write(3,font=("Arial", 12, "normal"))
watch.goto(-3,-145)
watch.rt(20)
watch.write(6,font=("Arial", 12, "normal"))
watch.goto(-138,-6)
watch.write(9,font=("Arial", 12, "normal"))
watch.pd()

def dot_maker(x,y,Angle):
    watch.pu()
    watch.goto(x,y)
    watch.lt(Angle)
    watch.pd()
    watch.forward(5)
dot_maker(127,71,30)
dot_maker(-71,126,100)
dot_maker(71,127,100)
dot_maker(127,-71,100)
dot_maker(71,-127,-20)
dot_maker(-127,71,30)
dot_maker(-127,-71,60)
dot_maker(-71,-127,30)




# The physical make up of the counters
seconds.shape('turtle')
seconds.shapesize(0.40,0.40)
minutes.shape('turtle')
minutes.shapesize(0.5,0.5)
minutes.pensize(1.75)
hours.shape('turtle')
hours.shapesize(0.55,0.55)
hours.pensize(2.5)


# Setting the time to starting point
hours.lt(90)
minutes.lt(90)
seconds.lt(90)


if systems_hour > 12:
    systems_hour-= 12
compileDelaySecond = 2 # we need to add the time it takes to start counting after it grabs system time



# Adjusting the logic with improted system time
minutes.rt(6*systems_minute)
seconds.rt(6*(systems_second + compileDelaySecond ))

# to compenset compileDelaySecond we added on startup we need to reduce the first interation by 2 we added three seconds
systems_second += 2


if systems_minute < 12:
    pass
elif systems_minute < 24:
    systems_minute -= 12
    fraction_hour = 0.2
elif systems_minute < 36:
    systems_minute -= 24
    fraction_hour = 0.4
elif systems_minute < 48:
    systems_minute -= 36
    fraction_hour = 0.6
else:
    systems_minute -= 48
    fraction_hour = 0.8
    
hours.rt(30*( systems_hour + fraction_hour))
    
  
# The watchs infinite loop to count    
while True:
    hours.fd(60)
    for minute in range(systems_minute,12):
        minutes.fd(90)
        minutes.st
        for second in range(systems_second,60):
            seconds.fd(110)
            seconds.st()
            t.sleep(0.9) #the reason the sleep time reduced from 1 sec is, the time spent by the machine workin on the steps
            seconds.undo()
            seconds.undo()
            seconds.ht()
            seconds.rt(6)
            if second == 59:
                systems_second = 0
        minutes.ht
        minutes.undo()
        minutes.rt(6)
        if minute == 11:
            systems_minute = 0
    hours.undo()
    hours.rt(6)