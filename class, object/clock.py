import turtle
import math
import datetime as dt
import time

w = turtle.Screen()
p = turtle.Turtle()
p.speed(10)
w.tracer(0)
p.hideturtle()

class drawClock():
    def __init__(self, r):
        self.r = r
    
    def start_point(self, pen):  #Sub-func
        '''
        This func move pen to (0, -r)
        '''
        pen.penup()
        pen.goto(0, -self.r)
        pen.pendown()

    def fd_then_bw(self, pen, value, op):  #Sub-func
        '''
        This func move fd then bw with same distance
        Op = 1 mean turn pen left 90 before draw then turn back right 90 when done
        Op = 0 mean keep pen head up after done
        '''
        if op == 1:
            pen.left(90)
            pen.fd(value)
            pen.backward(value)
            pen.right(90)
        elif op == 0:
            pen.fd(value)
            pen.backward(value)

    def hand_details(self):  #Sub-func
        '''
        This func give hands length and size base on self.r
        hand_details[0] is spin degree, [1] is length, else is size
        '''
        hand_details = [[6], [6], [30]]
        standard_hand_length = self.r - self.hour_hash
        standard_hand_size = math.floor(self.r / 100)
        for i in range(0, 3):
            standard_hand_length *= 9/10
            hand_details[i].append(standard_hand_length)
        for j in range(0, 3):
            hand_details[j].append(standard_hand_size)
            standard_hand_size += 1
        return hand_details
    
    def clock_face(self):  #Main-func
        '''
        This func draw clock face and hashes
        Pen go away when func ends
        '''
        self.start_point(p)  #Go to start point
        self.hour_hash = self.r/8  #Give hour hash length
        for five_mins_block in range (12):  #Five mins block repeat 12 times
            self.fd_then_bw(p, self.hour_hash, 1)
            p.circle(self.r, 6)
            for mins_block in range(4):  #Mins block repeat 4 times
                self.fd_then_bw(p, self.hour_hash/3, 1)
                p.circle(self.r, 6)

    def clock_run(self):  #Main-func
        '''
        This func draw 3 hands based on details give by hand_details()
        All hands head up (left(90)) first, then spin to correct time
        Time will be set one func called, then all hands run automaticly
        '''
        second = int(dt.datetime.now().strftime("%S"))
        minute = int(dt.datetime.now().strftime("%M"))
        hour = int(dt.datetime.now().strftime("%H"))
        set_time = [second, minute, hour]
        s_hand = None
        m_hand = None
        h_hand = None
        all_hands = [s_hand, m_hand, h_hand]
        for index in range(0, 3):
            all_hands[index] = turtle.Turtle()
            all_hands[index].left(90)
            all_hands[index].hideturtle()
            all_hands[index].pensize(self.hand_details()[index][2])
            all_hands[index].right((self.hand_details()[index][0]) * set_time[index])
            self.fd_then_bw(all_hands[index], self.hand_details()[index][1], 0)
        if 30 <= minute < 59:  #Hour hash turn to middle of fiveminsblock when minute reachs 30
            all_hands[2].clear()
            all_hands[2].right(15)
            self.fd_then_bw(all_hands[2], self.hand_details()[2][1], 0)
        count_s = 0 + second
        count_m = 0 + minute
        while True:
            all_hands[0].clear()
            all_hands[0].right(6)
            all_hands[0].pencolor("Red")
            self.fd_then_bw(all_hands[0], self.hand_details()[0][1], 0)
            if count_s % 60 == 0:
                all_hands[1].clear()
                all_hands[1].right(6)
                self.fd_then_bw(all_hands[1], self.hand_details()[1][1], 0)
                count_m += 1
                if count_m % 30 == 0:
                    all_hands[2].clear()
                    all_hands[2].right(15)
                    self.fd_then_bw(all_hands[2], self.hand_details()[2][1], 0)
            count_s += 1
            w.update()
            time.sleep(1)

app = drawClock(1)
app.clock_face()
app.clock_run()

turtle.done()