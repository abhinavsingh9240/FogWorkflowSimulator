from tkinter import Tk
from tkinter.ttk import Frame, LabelFrame, Label, Entry, Spinbox, Button, Combobox

if __name__ == "__main__":
    root = Tk()

    root.title("Fog Workflow Simulator")

    root_frame = Frame(root, padding="20")
    root_frame.pack()

    frame_1 = LabelFrame(root_frame, text="VMs")
    frame_1.grid(sticky="N", row=1, column=1)

    lbl_cloud = Label(frame_1, text="Clouds : ")
    entry_cloud = Spinbox(frame_1, from_=0, to=5000, width=10)
    lbl_cloud.grid(sticky="W", row=1, column=1)
    entry_cloud.grid(sticky="W", row=1, column=2)

    lbl_fog = Label(frame_1, text="Fogs : ")
    entry_fog = Spinbox(frame_1, from_=0, to=5000, width=10)
    lbl_fog.grid(sticky="W", row=2, column=1)
    entry_fog.grid(sticky="W", row=2, column=2)

    lbl_mobile = Label(frame_1, text="Mobiles : ")
    entry_mobile = Spinbox(frame_1, from_=0, to=5000, width=10)
    lbl_mobile.grid(sticky="W", row=3, column=1)
    entry_mobile.grid(sticky="W", row=3, column=2)

    button_vms = Button(frame_1, text="Details")
    button_vms.grid(sticky="E", row=4, column=2)

    # frame2 - Algorithms

    frame_2 = LabelFrame(root_frame, text="Algorithms")
    frame_2.grid(sticky="N", row=1, column=2)

    lbl_Scheduling = Label(frame_2, text="Scheduling : ")
    entry_Scheduling = Combobox(frame_2, values=[])
    button_Scheduling = Button(frame_2, text="...", width=5)
    button_Scheduling.grid(sticky="E", row=1, column=3)
    lbl_Scheduling.grid(sticky="W", row=1, column=1)
    entry_Scheduling.grid(sticky="W", row=1, column=2)

    lbl_LBalancing = Label(frame_2, text="LBalancing : ")
    entry_LBalancing = Combobox(frame_2, values=[])
    button_LBalancing = Button(frame_2, text="...", width=5)
    button_LBalancing.grid(sticky="E", row=2, column=3)
    lbl_LBalancing.grid(sticky="W", row=2, column=1)
    entry_LBalancing.grid(sticky="W", row=2, column=2)

    lbl_Migration = Label(frame_2, text="Migration : ")
    entry_Migration = Combobox(frame_2, values=[])
    button_Migration = Button(frame_2, text="...", width=5)
    button_Migration.grid(sticky="E", row=3, column=3)
    lbl_Migration.grid(sticky="W", row=3, column=1)
    entry_Migration.grid(sticky="W", row=3, column=2)

    lbl_Objective = Label(frame_2, text="Objective : ")
    entry_Objective = Combobox(frame_2, values=["Cost", "Time", "Energy"])

    lbl_Objective.grid(sticky="W", row=4, column=1)
    entry_Objective.grid(sticky="W", row=4, column=2)

    #frame 3

    frame_3 = LabelFrame(root_frame, text="Workflow")
    frame_3.grid(sticky="N", row=2, column=1)

    lbl_type = Label(frame_3, text="Type : ")
    entry_type = Combobox(frame_3, values=["Montage", "second", "Third"])
    lbl_type.grid(sticky="W", row=1, column=1)
    entry_type.grid(sticky="W", row=1, column=2)

    lbl_amount = Label(frame_3, text="Amount : ")
    entry_amount = Combobox(frame_3, values=["10", "20", "30"])
    lbl_amount.grid(sticky="W", row=2, column=1)
    entry_amount.grid(sticky="W", row=2, column=2)

    lbl_deadline = Label(frame_3, text="Deadline : ")
    entry_deadline = Entry(frame_3)
    lbl_deadline.grid(sticky="W", row=3, column=1)
    entry_deadline.grid(sticky="W", row=3, column=2)

    button_start = Button(root_frame,text= "Start")
    button_start.grid(row=2,column=2
                      )
    root.mainloop()
