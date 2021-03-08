from tkinter import *
from tkinter import ttk
import tkinter as tk

root = Tk()
scrollbar = Scrollbar(root)
root.geometry('1100x900')
root.title("Welcome to Dr.G app")

v = IntVar()

# Main Frame

main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# Canvas

my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# scrollbar to the canvas

my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# config the Canvas

my_canvas.configure(yscrollcommand=my_scrollbar.set, background="#f8e7f0")
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

# Frame inside the Canvas

second_frame = Frame(my_canvas, background="#f8e7f0")

# Add that New frame To a Window In The Canvas

my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

label1 = Label(second_frame, text="1. Enter Player (or team) name", bg="#f8e7f0")

label2 = Label(second_frame, text="2. Chose tournament type", bg="#f8e7f0")
radio_button1 = Radiobutton(second_frame,
                            text="Round robin",
                            padx=20,
                            bg="#f8e7f0",
                            variable=v,
                            value=1)
radio_button2 = Radiobutton(second_frame,
                            text="Double round robin",
                            padx=20,
                            relief=FLAT,
                            bg="#f8e7f0",
                            borderwidth=0,
                            variable=v,
                            value=2)
label3 = Label(second_frame, text="3. Schedule locations ?", bg="#f8e7f0")
radio_button3 = Radiobutton(second_frame,
                            text="Yes",
                            padx=20,
                            bg="#f8e7f0",
                            variable=v,
                            value=3)
radio_button4 = Radiobutton(second_frame,
                            text="No",
                            padx=20,
                            relief=FLAT,
                            bg="#f8e7f0",
                            borderwidth=0,
                            variable=v,
                            value=4)
label4 = Label(second_frame, text="4. Enter tournament name", bg="#f8e7f0")
tournament_name = Entry(second_frame)
label5 = Label(second_frame, text="5. Generate Schedule", bg="#f8e7f0")

team_entry = Text(second_frame, width=50, height=20, font=14, bg="powder blue", fg="#a6a5a8")
team_entry.insert("1.0", "Enter one player/team per line...")
team_entry.configure(state=DISABLED)


def on_click(event):
    team_entry.configure(state=NORMAL, fg="black")
    team_entry.delete("1.0", END)

    # make the callback only work once
    team_entry.unbind('<Button-1>', on_click_id)


on_click_id = team_entry.bind('<Button-1>', on_click)

# auto generate players


x = IntVar()
e1 = IntVar()


def auto_gen_win():
    newwindow = Toplevel(root)
    newWindow.title("Auto Generate")
    label1 = Label(newwindow, text="Enter the number of players")
    label1.grid(row=0, column=0)
    entry1 = tk.Entry(newwindow, width=20, bg='yellow')
    button1 = Button(newwindow, text="Confirm",
                command=lambda: x.set(e1.get()))
    button = Button(newwindow, text="Generate", command=lambda: gen(x))
    button1.grid(row=1, column=0)
    button.grid(row=1, column=1)
    entry1.grid(row=0, column=1)


def gen(x):
    team_entry.configure(state=NORMAL, fg="black")
    x = x.get()
    team_entry.delete("1.0", END)

    for l in range(1, x + 1):
        team_entry.insert(f"{l}.0", f"player{l}" + '\n')


auto_gen = Button(second_frame,
                  text="Auto Generate",
                  width=10,
                  height=1,
                  command=lambda: auto_gen_win())

list1 = []
list2 = []
teams = {}


def generate():
    second_frame2 = Toplevel(root)
    second_frame2.title("Schedule")
    second_frame2.geometry('1100x900')
    second_frame2.configure(bg="#f8e7f0")
    # Main Frame

    main_frame1 = Frame(second_frame2)
    main_frame1.pack(fill=BOTH, expand=1)

    #
    my_canvas1 = Canvas(main_frame1, bg="#f8e7f0",)
    my_canvas1.pack(side=LEFT, fill=BOTH, expand=1)

    # scrollbar to the canvas

    my_scrollbar1 = ttk.Scrollbar(main_frame1, orient=VERTICAL, command=my_canvas1.yview)
    my_scrollbar1.pack(side=RIGHT, fill=Y)

    # config the Canvas

    my_canvas1.configure(yscrollcommand=my_scrollbar1.set)
    my_canvas1.bind('<Configure>', lambda e: my_canvas1.configure(scrollregion=my_canvas1.bbox("all")))

    # Frame inside the Canvas

    second_frame2 = Frame(my_canvas1)

    # Add that New frame To a Window In The Canvas

    my_canvas1.create_window((0, 0), window=second_frame2, anchor="nw")

    tournament_name_1 = Label(second_frame2, text=tournament_name.get(), bg="#f8e7f0", fg="red")
    tournament_name_1.grid(row=0, column=2, padx=10, columnspan=2)
    labels1 = Label(second_frame2, text="Round", bg="#f8e7f0", font=" arial 14", width=5)
    labels1.grid(row=1, column=0)
    labels2 = Label(second_frame2, text="Match", bg="#f8e7f0", font="arial 14", width=30)
    labels2.grid(row=1, column=1, columnspan=2)
    labels3 = Label(second_frame2, text="", bg="#f8e7f0", width=20)
    labels3.grid(row=1, column=3)
    labels4 = Label(second_frame2, text="P1", font="arial 14", bg="#f8e7f0", width=5)
    labels4.grid(row=1, column=4)
    labels5 = Label(second_frame2, text="P2", font="arial 14", bg="#f8e7f0", width=5)
    labels5.grid(row=1, column=5)
    list1 = []
    list2 = []
    number_of_players = int(team_entry.index('end-1c').split('.')[0])
    player_list = team_entry.get('1.0', 'end').split('\n')
    player_list.pop()
    player_list.pop()
    if (number_of_players - 1) % 2 == 1: player_list = player_list + ["BYE"]
    for i in range(0, len(player_list)):
        create_team_dict(second_frame2, i)
    print(teams)
    length = len(player_list)
    print(player_list)
    l2 = int(length / 2)
    print(l2)
    for i in range(0, l2):
        list1.append(player_list[i])
        list2.append(player_list[(length - 1) - i])
        pass
    k = 2
    roundd = 1
    l = 0
    color = "lavender"
    
    class sch:
        """docstring for sch"""

        def __init__(self, root, g,m):
            v = list1[g]
            d = list2[g]
            self.mat=m
            self.r = Label(root, text=roundd, font="arial 14", width=5, bg="#f8e7f0")
            self.r.grid(row=k + g, column=0, sticky=W)
            self.e = Label(root, text=v, font="arial 14", width=15, bg=color)
            self.e.grid(row=k + g, column=1, sticky=W)
            self.b = Label(root, text=d, font="arial 14", width=15, bg=color)
            self.b.grid(row=k + g, column=2, sticky=W)
            self.n = Entry(root)
            self.n.grid(row=k + g, column=3, sticky=W)
            self.p1 = Entry(root, font="arial 14", width=5, bg="yellow")
            self.p1.grid(row=k + g, column=4, sticky=W)
            self.p2 = Entry(root, font="arial 14", width=5, bg="yellow")
            self.p2.grid(row=k + g, column=5, sticky=W)
            self.update_rank = Button(second_frame2, text="up", bg="#f8e7f0", height=2, width=10,
                                      command=lambda: teamup(self.p1.get(), self.p2.get(), v, d,self.mat,self.update_rank))
            self.update_rank.grid(row=k + g, column=6)
            self.Add_rank = Button(second_frame2, text="Add", bg="#f8e7f0", height=2, width=10,
                                      command=lambda: teamadd(self.p1.get(), self.p2.get(), v, d,self.Add_rank,self.mat))
            self.Add_rank.grid(row=k + g, column=7)

    def round_robin():
        g = 0
        match=0
        for i in range(0, int(length / 2)):
            sch(second_frame2, g ,match)
            g += 1
            match +=1
        print(list1)
        print(list2)
        vfix = list1[0]
        v2 = list1[int(length / 2) - 1]
        v3 = list2[0]
        for i in range(1, int(length / 2) - 1):
            list1[int(length / 2) - i] = list1[int(length / 2) - (i + 1)]

        list1[1] = v3
        list1[0] = vfix
        for i in range(0, int(length / 2) - 1):
            list2[i] = list2[i + 1]
        list2[int(length / 2) - 1] = v2

    for i in range(1, length):
        round_robin()
        roundd += 1
        k = (k + int(length / 2))
        if l == 0:
            l = 1
            color = "#f8e7f0"
        elif l == 1:
            l = 0
            color = "lavender"
        print(l)
played_match={}
class teamadd:
    """docstring for team"""

    def __init__(self, sp1, sp2, p1, p2,bts,mat):
        super(teamadd, self).__init__()
        bts.config(state='disabled')
        self.p1_draw = 0
        self.p1_points = 0
        self.p1_wins = 0
        self.p1_loss = 0
        self.p1_for = int(sp1)
        self.p1_against = int(sp2)
        self.p2_draw = 0
        self.p2_points = 0
        self.p2_wins = 0
        self.p2_loss = 0
        self.p2_for = int(sp2)
        self.p2_against = int(sp1)
        played_match[mat]={}
        played_match[mat][p1]=sp1
        played_match[mat][p2]=sp2
        if int(sp1) > int(sp2):
            self.p1_wins = 1
            self.p2_loss = 1
            self.p1_points = 1
            self.p2_points = 0
        elif int(sp1) < int(sp2):
            self.p2_wins = 1
            self.p1_loss = 1
            self.p2_points = 1
            self.p1_points = 0
        elif int(sp1) == int(sp2):
            self.p2_wins = 0
            self.p1_loss = 0
            self.p2_points = 1
            self.p1_points = 1
            self.p1_draw = 1
            self.p2_draw = 1
        teams[p1]['played'] += 1
        teams[p2]['played'] += 1
        teams[p1]['win'] += self.p1_wins
        teams[p2]['win'] += self.p2_wins
        teams[p1]['draws'] += self.p1_draw
        teams[p2]['draws'] += self.p2_draw
        teams[p1]['loss'] += self.p1_loss
        teams[p2]['loss'] += self.p2_loss
        teams[p1]['for'] += self.p1_for
        teams[p2]['for'] += self.p2_for
        teams[p1]['agi'] += self.p1_against
        teams[p2]['agi'] += self.p2_against
        teams[p1]['point'] += self.p1_points
        teams[p2]['point'] += self.p2_points

class teamup:
    """docstring for team"""

    def __init__(self, sp1, sp2, p1, p2,mat,u):
        super(teamup, self).__init__()
        u.config(state='disabled')
        self.before_sp1=int(played_match[mat][p1])
        self.before_sp2=int(played_match[mat][p2])
        teams[p1]['for'] -= self.before_sp1
        teams[p2]['for'] -= self.before_sp2
        teams[p1]['agi'] -= self.before_sp2
        teams[p2]['agi'] -= self.before_sp1
        if self.before_sp1 > self.before_sp2:
            if teams[p1]['loss'] > 0:
                teams[p1]['win'] -= 1
            if teams[p2]['win'] > 0:
                teams[p2]['loss'] -= 1
            if teams[p2]['point'] > 0:
                teams[p1]['point'] -= 1
        elif self.before_sp1 < self.before_sp2:
            if teams[p2]['win'] > 0:
                teams[p2]['win'] -= 1
            if teams[p1]['loss'] > 0:
                teams[p1]['loss'] -= 1
            if teams[p2]['point'] > 0:
                teams[p2]['point'] -= 1
        elif self.before_sp1 == self.before_sp2:
            if teams[p1]['draws'] > 0 :
                teams[p1]['draws'] -= 1
            if teams[p2]['draws'] > 0:
                teams[p2]['draws'] -= 1
            if teams[p1]['point'] > 0:
                teams[p1]['point'] -= 1
            if teams[p2]['point'] > 0:
                teams[p2]['point'] -= 1
        self.p1_draw = 0
        self.p1_points = 0
        self.p1_wins = 0
        self.p1_loss = 0
        self.p1_for = int(sp1)
        self.p1_against = int(sp2)
        self.p2_draw = 0
        self.p2_points = 0
        self.p2_wins = 0
        self.p2_loss = 0
        self.p2_for = int(sp2)
        self.p2_against = int(sp1)
        print(played_match)
        if int(sp1) > int(sp2):
            self.p1_wins = 1
            self.p2_loss = 1
            self.p1_points = 1
            self.p2_points = 0
        elif int(sp1) < int(sp2):
            self.p2_wins = 1
            self.p1_loss = 1
            self.p2_points = 1
            self.p1_points = 0
        elif int(sp1) == int(sp2):
            self.p2_wins = 0
            self.p1_loss = 0
            self.p2_points = 1
            self.p1_points = 1
            self.p1_draw = 1
            self.p2_draw = 1
        teams[p1]['win'] += self.p1_wins
        teams[p2]['win'] += self.p2_wins
        teams[p1]['draws'] += self.p1_draw
        teams[p2]['draws'] += self.p2_draw
        teams[p1]['loss'] += self.p1_loss
        teams[p2]['loss'] += self.p2_loss
        teams[p1]['for'] += self.p1_for
        teams[p2]['for'] += self.p2_for
        teams[p1]['agi'] += self.p1_against
        teams[p2]['agi'] += self.p2_against
        teams[p1]['point'] += self.p1_points
        teams[p2]['point'] += self.p2_points


def gen_tab():
    ranking_window = Toplevel(second_frame)
    ranking_window.title(f"Ranking Table for {tournament_name.get()} Tournament")
    ranking_window.geometry("1200x900")
    # Main Frame

    main_frame1 = Frame(ranking_window)
    main_frame1.pack(fill=BOTH, expand=1)

    # Canvas

    my_canvas1 = Canvas(main_frame1)
    my_canvas1.pack(side=LEFT, fill=BOTH, expand=1)

    # scrollbar to the canvas

    my_scrollbar1 = ttk.Scrollbar(main_frame1, orient=VERTICAL, command=my_canvas1.yview)
    my_scrollbar1.pack(side=RIGHT, fill=Y)

    # config the Canvas

    my_canvas1.configure(bg="#f8e7f0", yscrollcommand=my_scrollbar1.set)
    my_canvas1.bind('<Configure>', lambda e: my_canvas1.configure(scrollregion=my_canvas1.bbox("all")))

    # Frame inside the Canvas

    second_frame1 = Frame(my_canvas1)

    # Add that New frame To a Window In The Canvas

    my_canvas1.create_window((0, 0), window=second_frame1, anchor="nw")
    ranking_window.title(f"Ranking Table for {tournament_name.get()} Tournament")
    but = Button(second_frame1, text="Refresh", bg="#f8e7f0", font="arial 14", command=lambda: ref())
    but.grid(row=0, column=4)
    label_r1 = Label(second_frame1, text="#", bg="#f8e7f0", width=10, font="arial 14")
    label_r1.grid(row=1, column=0)
    label_r2 = Label(second_frame1, text="Player", bg="#f8e7f0", width=20, font="arial 14")
    label_r2.grid(row=1, column=1)
    label_r3 = Label(second_frame1, text="Played", bg="#f8e7f0", width=10, font="arial 14")
    label_r3.grid(row=1, column=2)
    label_r4 = Label(second_frame1, text="Wins", bg="#f8e7f0", width=10, font="arial 14")
    label_r4.grid(row=1, column=3)
    label_r5 = Label(second_frame1, text="Draws", bg="#f8e7f0", width=10, font="arial 14")
    label_r5.grid(row=1, column=4)
    label_r6 = Label(second_frame1, text="Losses", bg="#f8e7f0", width=10, font="arial 14")
    label_r6.grid(row=1, column=5)
    label_r7 = Label(second_frame1, text="For", bg="#f8e7f0", width=10, font="arial 14")
    label_r7.grid(row=1, column=6)
    label_r8 = Label(second_frame1, text="Against", bg="#f8e7f0", width=10, font="arial 14")
    label_r8.grid(row=1, column=7)
    label_r9 = Label(second_frame1, text="Points", bg="#f8e7f0", width=10, font="arial 14")
    label_r9.grid(row=1, column=8)
    number_of_players = int(team_entry.index('end-1c').split('.')[0])
    player_list = team_entry.get('1.0', 'end').split('\n')
    player_list.pop()
    player_list.pop()
    if (number_of_players - 1) % 2 == 1: player_list = player_list + ["BYE"]
    for i in range(0, len(player_list)):
        ranking_table(second_frame1, i, player_list)

    def ref():
        sort_list = []
        for i in range(0, len(player_list)):
            a = teams[player_list[i]]['player']
            b = teams[player_list[i]]['point']
            c = teams[player_list[i]]['for']
            d = teams[player_list[i]]['agi']
            e = c - d
            sort_list.append((a, b, e))
        print(sort_list)

        def Sort1(sub_li):
            sub_li.sort(key=lambda x: x[2], reverse=True)
            return sub_li

        def Sort(sub_li):
            Sort1(sub_li).sort(key=lambda x: x[1], reverse=True)
            return sub_li

        print(Sort(sort_list))
        new_list = Sort(sort_list)
        for i in range(0, len(player_list)):
            update_ranking_table(second_frame1, new_list, i)

    pass


print(team_entry.get("1.0"))
generate_btn = Button(second_frame,
                      text="Generate",
                      font=14,
                      width=11,
                      height=2,
                      command=lambda: generate())

ranking_btn = Button(second_frame,
                     text="Ranking",
                     font=14,
                     width=11,
                     height=2,
                     command=lambda: gen_tab())

class create_team_dict:

    def __init__(self, root, i):
        number_of_players = int(team_entry.index('end-1c').split('.')[0])
        player_list = team_entry.get('1.0', 'end').split('\n')
        player_list.pop()
        player_list.pop()
        if (number_of_players - 1) % 2 == 1: player_list = player_list + ["BYE"]
        teams.update({player_list[i]: {"player": player_list[i], "played": 0, "win": 0, "draws": 0, "loss": 0, "for": 0,
                                       "agi": 0, "point": 0}})


class ranking_table:
    """docstring for ranking"""

    def __init__(self, root, i, player_list):
        Label(root, text=i + 1, bg="#f8e7f0", font="arial 14", width=10).grid(row=i + 2, column=0)
        Label(root, text=teams[player_list[i]]['player'], bg="#f8e7f0", font="arial 14", width=20).grid(row=i + 2, column=1)
        Label(root, text=teams[player_list[i]]['played'], bg="#f8e7f0", font="arial 14", width=10).grid(row=i + 2, column=2)
        Label(root, text=teams[player_list[i]]['win'], bg="#f8e7f0", font="arial 14", width=10).grid(row=i + 2, column=3)
        Label(root, text=teams[player_list[i]]['draws'], bg="#f8e7f0", font="arial 14", width=10).grid(row=i + 2, column=4)
        Label(root, text=teams[player_list[i]]['loss'], bg="#f8e7f0", font="arial 14", width=10).grid(row=i + 2, column=5)
        Label(root, text=teams[player_list[i]]['for'], bg="#f8e7f0", font="arial 14", width=10).grid(row=i + 2, column=6)
        Label(root, text=teams[player_list[i]]['agi'], bg="#f8e7f0", font="arial 14", width=10).grid(row=i + 2, column=7)
        Label(root, text=teams[player_list[i]]['point'], bg="#f8e7f0", font="arial 14", width=10).grid(row=i + 2, column=8)


class update_ranking_table:
    """docstring for ranking"""

    def __init__(self, root, i, a):
        Label(root, text=a + 1, bg="#f8e7f0", font="arial 14", width=10).grid(row=a + 2, column=0)
        Label(root, text=teams[i[a][0]]['player'], bg="#f8e7f0", font="arial 14", width=20).grid(row=a + 2, column=1)
        Label(root, text=teams[i[a][0]]['played'], bg="#f8e7f0", font="arial 14", width=9).grid(row=a + 2, column=2)
        Label(root, text=teams[i[a][0]]['win'], bg="#f8e7f0", font="arial 14", width=9).grid(row=a + 2, column=3)
        Label(root, text=teams[i[a][0]]['draws'], bg="#f8e7f0", font="arial 14", width=9).grid(row=a + 2, column=4)
        Label(root, text=teams[i[a][0]]['loss'], bg="#f8e7f0", font="arial 14", width=9).grid(row=a + 2, column=5)
        Label(root, text=teams[i[a][0]]['for'], bg="#f8e7f0", font="arial 14", width=9).grid(row=a + 2, column=6)
        Label(root, text=teams[i[a][0]]['agi'], bg="#f8e7f0", font="arial 14", width=9).grid(row=a + 2, column=7)
        Label(root, text=teams[i[a][0]]['point'], bg="#f8e7f0", font="arial 14", width=9).grid(row=a + 2, column=8)


label1.grid(row=0, column=0, sticky=W, padx=10, pady=10)
team_entry.grid(row=1, column=0, sticky=W, pady=2, padx=10)
label2.grid(row=3, column=0, sticky=W, pady=20, padx=10)
radio_button1.grid(row=4, sticky=W, column=0, pady=1, padx=10)
radio_button2.grid(row=4, column=0, sticky=W, pady=1, padx=170)
label4.grid(row=9, column=0, sticky=W, pady=2, padx=10)
tournament_name.grid(row=10, sticky=W, column=0, pady=2, padx=10)
label5.grid(row=11, column=0, sticky=W, pady=2, padx=10)
generate_btn.grid(row=12, sticky=W, column=0, pady=10, padx=10)
ranking_btn.grid(row=12, column=0, pady=2, padx=10)

root.mainloop()
