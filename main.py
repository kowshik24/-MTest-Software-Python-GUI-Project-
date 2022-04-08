# import everything from tkinter
from tkinter import *

# and import messagebox as mb from tkinter
from tkinter import messagebox as mb

# import json to use json file for data
import json

import time


# class to define the components of the GUI
class Quiz:

    def __init__(self):

        self.q_no = 0
        self.mark = [0] * len(question)

        self.display_title()
        self.display_question()

        # opt_selected holds an integer value which is used for
        # selected option in a question.
        self.opt_selected = IntVar()

        # displaying radio button for the current question and used to
        # display options for the current question
        self.opts = self.radio_buttons()

        # display options for the current question
        self.display_options()

        # displays the button for next and exit.
        self.buttons()
        # self.prev_btn()

        self.data_size = len(question)

        self.correct = 0

        self.clock()

    def display_result(self):

        # calculates the wrong count
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"

        # calcultaes the percentage of correct answers
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"

        # Shows a message box to display the result

        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")

    def clock(self):

        hour = StringVar()
        minute = StringVar()
        second = StringVar()

        hour.set("00")
        minute.set("00")
        second.set("00")

        # Use of Entry class to take input from the user
        hourEntry = Entry(gui, width=3, font=("Arial", 18, ""),
                          textvariable=hour)
        hourEntry.place(x=80, y=20)

        minuteEntry = Entry(gui, width=3, font=("Arial", 18, ""),
                            textvariable=minute)
        minuteEntry.place(x=130, y=20)

        secondEntry = Entry(gui, width=3, font=("Arial", 18, ""),
                            textvariable=second)
        secondEntry.place(x=180, y=20)

        temp = int(len(question)) * 60

        while temp > -1:

            # divmod(firstvalue = temp//60, secondvalue = temp%60)
            mins, secs = divmod(temp, 60)

            # Converting the input entered in mins or secs to hours,
            # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
            # 50min: 0sec)
            hours = 0
            if mins > 60:
                # divmod(firstvalue = temp//60, secondvalue
                # = temp%60)
                hours, mins = divmod(mins, 60)

            # using format () method to store the value up to
            # two decimal places
            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))

            secondEntry.update()
            minuteEntry.update()
            hourEntry.update()
            # gui.update()

            time.sleep(1)

            # when temp value = 0; then a messagebox pop's up
            # with a message:"Time's up"
            if (temp == 0):
                mb.showinfo("Time Countdown", "Time's up!!!")
                self.display_result()
                gui.destroy()

            # after every one sec the value of temp will be decremented
            # by one
            temp -= 1

    # This method checks the Answer after we click on Next.
    def check_ans(self, q_no):

        select_option = self.opt_selected.get()

        if(select_option==0):
            return False

        print("Option Selected : ",select_option)
        if self.mark[self.q_no] == 1:
            mb.showinfo("You have already fill it! ")
            return False

        # print(type(q_no))
        # mark[q_no]=1

        # if mark[select_option]==1:

        # checks for if the selected option is correct
        if self.opt_selected.get() == answer[q_no]:
            self.mark[self.q_no] = 1

            # if the option is correct it return true
            return True

    # This method is used to check the answer of the
    # current question by calling the check_ans and question no.
    # if the question is correct it increases the count by 1
    # and then increase the question number by 1. If it is last
    # question then it calls display result to show the message box.
    # otherwise shows next question.
    def next_btn(self):
        self.q_no += 1

        # Check if the answer is correct
        if (self.check_ans(self.q_no) and self.q_no < self.data_size and self.mark[self.q_no] == 0):
            self.mark[self.q_no] = 1
            # if the answer is correct it increments the correct by 1
            self.correct += 1

        # Moves to next Question by incrementing the q_no counter


        # checks if the q_no size is equal to the data size
        if self.q_no == self.data_size:

            # if it is correct then it displays the score
            self.display_result()

            # destroys the GUI
            gui.destroy()
        else:
            # shows the next question
            self.display_question()
            self.display_options()

    def prev_btn(self):

        if (self.check_ans(self.q_no) and self.mark[self.q_no] == 0 and self.q_no >= 0):
            self.mark[self.q_no] = 1
            self.correct += 1

        self.q_no -= 1

        if self.q_no < 0:
            self.display_result()
            gui.destroy()
        else:
            self.display_question()
            self.display_options()

    def quit_btn(self):
        self.display_result()
        gui.destroy()

    # This method shows the two buttons on the screen.
    # The first one is the next_button which moves to next question
    # It has properties like what text it shows the functionality,
    # size, color, and property of text displayed on button. Then it
    # mentions where to place the button on the screen. The second
    # button is the exit button which is used to close the GUI without
    # completing the quiz.
    def buttons(self):

        next_button = Button(gui, text="Next", command=self.next_btn,
                             width=10, bg="blue", fg="white", font=("ariel", 16, "bold"))

        next_button.place(x=500, y=380)

        quit_button = Button(gui, text="Quit", command=self.quit_btn,
                             width=5, bg="red", fg="white", font=("ariel", 20, " bold"), height=0)

        quit_button.place(x=761, y=10)

        prev_button = Button(gui, text="Previous", command=self.prev_btn, width=10, bg='red', fg='white',
                             font=("arial", 16, "bold"))
        prev_button.place(x=130, y=380)

    # This method deselect the radio button on the screen
    # Then it is used to display the options available for the current
    # question which we obtain through the question number and Updates
    # each of the options for the current question of the radio button.
    def display_options(self):
        val = 0

        self.opt_selected.set(0)

        for option in options[self.q_no]:
            self.opts[val]['text'] = option
            val += 1

    def display_question(self):

        q_no = Label(gui, text=question[self.q_no], width=60,
                     font=('ariel', 16, 'bold'), anchor='w')

        q_no.place(x=70, y=100)

    def display_title(self):

        title = Label(gui, text="Online MCQ Test! ",
                      width=50, bg="#247291", fg="white", font=("ariel", 20, "bold"), height=2)

        title.place(x=0, y=2)

    # This method shows the radio buttons to select the Question
    # on the screen at the specified position. It also returns a
    # list of radio button which are later used to add the options to
    # them.
    def radio_buttons(self):

        # initialize the list with an empty list of options
        q_list = []

        # position of the first option
        y_pos = 150

        # adding the options to the list
        while len(q_list) < 4:
            # setting the radio button properties
            radio_btn = Radiobutton(gui, text=" ", variable=self.opt_selected,
                                    value=len(q_list) + 1, font=("ariel", 14))

            # adding the button to the list
            q_list.append(radio_btn)

            # placing the button
            radio_btn.place(x=100, y=y_pos)

            # incrementing the y-axis position by 40
            y_pos += 40

        # return the radio buttons
        return q_list


gui = Tk()

gui.geometry("880x720")
gui.configure(bg='#FFEEEE')

# set the title of the Window
gui.title("Online MCQ Test!! ")

# get the data from the json file
with open('data.json') as f:
    data = json.load(f)

# set the question, options, and answer
question = (data['question'])
options = (data['options'])
answer = (data['answer'])

# create an object of the Quiz Class.
quiz = Quiz()

# Start the GUI
gui.mainloop()

# END OF THE PROGRAM
