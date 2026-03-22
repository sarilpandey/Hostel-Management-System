from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
import database
import csv

database.create_database_files()

def date():
    from datetime import datetime
    now = datetime.now()
    t = now.strftime("%H:%M")
    s1 = now.strftime("%H:%M,%Y-%m-%d")
    s1 = str(s1)
    return s1

base = Tk()
base.title("HOSTEL MANAGEMENT SYSTEM")
base.geometry(f'{1535}x{790}+{0}+{0}')
heading = Label(base, text="HOSTEL MANAGEMENT SYSTEM", font=("Arial 30 bold"), bg="lightseagreen", fg="white", padx=490, pady=20)
heading.pack()

canvas = Canvas(base, bg='silver', height=575, width=800)
canvas.place(x=330, y=130)

G = 1
def main():
    global G
    canvas = Canvas(base, bg='lightseagreen', height=675, width=310)
    canvas.place(x=-1, y=100)
    can = Canvas(base, bg='silver', height=675, width=1500)
    can.place(x=320, y=105)

    def add_stud():
        canvas = Canvas(base, bg='silver', height=675, width=1210)
        canvas.place(x=320, y=105)
        
        first_name = Label(base, text="First Name", font=("Arial 15 bold"), bg='silver', fg="black")
        first_name.place(x=400, y=150)
        fir_name_entry = Entry(base, width=15, font=("Arial 15"))
        fir_name_entry.place(x=400, y=180)
        fir_name_entry.focus()

        last_name = Label(base, text="Last Name", font=("Arial 15 bold"), bg="silver", fg="black")
        last_name.place(x=610, y=150)
        last_name_entry = Entry(base, width=15, font=("Arial 15"))
        last_name_entry.place(x=610, y=180)

        father_name = Label(base, text="Father Name", font=("Arial 15 bold"), bg="silver", fg="black")
        father_name.place(x=400, y=220)
        fathr_name_entry = Entry(base, width=15, font=("Arial 15"))
        fathr_name_entry.place(x=400, y=250)

        mother_name = Label(base, text="Mother Name", font=("Arial 15 bold"), bg="silver", fg="black")
        mother_name.place(x=610, y=220)
        mther_name_entry = Entry(base, width=15, font=("Arial 15"))
        mther_name_entry.place(x=610, y=250)

        dob = Label(base, text="DOB", font=("Arial 15 bold"), bg="silver", fg="black")
        dob.place(x=400, y=300)
        dob_entry = Entry(base, width=15, font=("Arial 15 bold"))
        dob_entry.place(x=400, y=330)
        m1 = Label(base, text="(Y-M-D)", font=("Arial 12 bold"), bg="silver", fg="black")
        m1.place(x=450, y=300)

        contact = Label(base, text="Contact", font=("Arial 15 bold"), bg="silver", fg="black")
        contact.place(x=610, y=300)
        cont_entry = Entry(base, width=15, font=("Arial 15 bold"))
        cont_entry.place(x=610, y=330)

        message = Label(base, text="(Contact No. will be your Hostel ID)", font=("Arial 10 bold"), bg="silver", fg="black")
        message.place(x=690, y=300)

        email = Label(base, text="Email", font=("Arial 15 bold"), bg="silver", fg="black")
        email.place(x=400, y=370)
        email_entry = Entry(base, width=15, font=("Arial 15 bold"))
        email_entry.place(x=400, y=410)

        address = Label(base, text="Address", font=("Arial 15 bold"), bg="silver", fg="black")
        address.place(x=610, y=370)
        addrs_entry = Entry(base, width=15, font=("Arial 15 bold"))
        addrs_entry.place(x=610, y=410)

        vehicle = Label(base, text="Vehicle No.", font=("Arial 15 bold"), bg="silver", fg="black")
        vehicle.place(x=400, y=450)
        vehicle_entry = Entry(base, width="15", font=("Arial 15 bold"))
        vehicle_entry.place(x=400, y=490)
        m2 = Label(base, text="(MH20EU9295)", font=("Arial 11 bold"), bg="silver", fg="black")
        m2.place(x=470, y=450)

        work_place = Label(base, text="Work Place/College", font=("Arial 15 bold"), bg="silver", fg="black")
        work_place.place(x=610, y=450)
        place_entry = Entry(base, width="15", font=("Arial 15 bold"))
        place_entry.place(x=610, y=490)

        gender = Label(base, text="Gender", font=("Arial 15 bold"), bg="silver", fg="black")
        gender.place(x=400, y=580)
        G = 1
        def selected():
            global G
            if c1.get() == 1: G = 1
            elif c1.get() == 2: G = 2
            else: G = 0

        c1 = IntVar()
        a = Radiobutton(base, text="Male", bg="silver", fg="black", font=("Arial 15 bold"), variable=c1, value=1, command=selected)
        b = Radiobutton(base, text="Female", bg="silver", fg="black", font=("Arial 15 bold"), variable=c1, value=2, command=selected)
        c = Radiobutton(base, text="Other", bg="silver", fg="black", font=("Arial 15 bold"), variable=c1, value=0, command=selected)
        a.place(x=490, y=580)
        b.place(x=580, y=580)
        c.place(x=680, y=580)

        def available_roome():
            rooms_availble = Label(base, text="Rooms Available", font=("Arial 20 bold"), bg="lightseagreen", fg="white", padx=140)
            rooms_availble.place(x=1005, y=110)
            x = "    Room No.                       |                                 Beds"
            room = Label(base, text=x, font=("Arial 15 bold"), bg="dark slate grey", fg="white")
            room.place(x=1005, y=150)
            global G
            bed1 = bed2 = bed3 = None
            if G == 1:
                f1 = open("room_info_boys.txt","r")
                bed1, bed2, bed3 = "B1", "B2", "B3"
            elif G==2:
                f1 = open("room_info_girls.txt","r")
                bed1, bed2, bed3 = "G1", "G2", "G3"
            else:
                f1 = open("room_info_others.txt","r")
                bed1, bed2, bed3 = "O1", "O2", "O3"
                
            all_lines = f1.readlines()
            count = 1
            rooms = []
            for i in all_lines:
                temp1 = str(i)
                one_line = temp1.split(',')
                if one_line[1] == bed1 and one_line[2] == bed2 and one_line[3] == bed3:
                    rooms.append([one_line[0], bed1, bed2, bed3])
                    count = 2
                elif one_line[1] != bed1 and one_line[2] == bed2 and one_line[3] == bed3:
                    rooms.append([one_line[0], "NA", bed2, bed3])
                    count = 2
                elif one_line[1] == bed1 and one_line[2] != bed2 and one_line[3] == bed3:
                    rooms.append([one_line[0], bed1, "NA", bed3])
                    count = 2
                elif one_line[1] == bed1 and one_line[2] == bed2 and one_line[3] != bed3:
                    rooms.append([one_line[0], bed1, bed2, "NA"])
                    count = 2
                elif one_line[1] == bed1 and one_line[2] != bed2 and one_line[3] != bed3:
                    rooms.append([one_line[0], bed1, "NA", "NA"])
                    count = 2
                elif one_line[1] != bed1 and one_line[2] == bed2 and one_line[3] != bed3:
                    rooms.append([one_line[0], "NA", bed2, "NA"])
                    count = 2
                elif one_line[1] != bed1 and one_line[2] != bed2 and one_line[3] == bed3:
                    rooms.append([one_line[0], "NA", "NA", bed3])
                    count = 2
                elif one_line[1] != bed1 and one_line[2] != bed2 and one_line[3] != bed3:
                    rooms.append(["--", "NA", "NA", "NA"])
                    count = 2
                    
            if count == 1:
                x = Label(base, text="No Rooms Available", font=("Arial", 40), bg="dark slate grey", fg="white")
                x.place(x=1020, y=300)
            else:
                y1co = 200
                flag = 1
                for i in rooms:
                    Label(base, text=i[0], font=("Arial", 15), bg="silver", fg="black").place(x=1150, y=y1co)
                    r_bk_no = Label(base, text=i[1] + "   " + i[2] + "   " + i[3], font=("Arial", 15), bg="silver", fg="black")
                    r_bk_no.place(x=1350, y=y1co)
                    y1co += 40
                    if flag >= 8: break
                    flag += 1
            f1.close()

            Canvas(base, height=2, width=600).place(x=1000, y=550)
            Label(base, text="Room No.", font=("Arial 15 bold"), bg="silver", fg="black").place(x=1040, y=570)
            r2 = Entry(base, width=15, font=("Arial 15 bold"))
            r2.place(x=1150, y=570)
            
            Label(base, text="Bed No.", font=("Arial 15 bold"), bg="silver", fg="black").place(x=1040, y=610)
            r4 = Entry(base, width=15, font=("Arial 15 bold"))
            r4.place(x=1150, y=610)
            
            Label(base, text="(B1 B2 B3)", font=("Arial 10 bold"), bg="silver", fg="black").place(x=1040, y=640)
            Label(base, text="( Girl = G1 )", font=("Arial 15 bold"), bg="silver", fg="black").place(x=1350,y=570)
            Label(base, text="( Other = O1)",font=("Arial 15 bold"), bg="silver", fg="black").place(x=1350,y=610)

            def student():
                global G
                file_name = ""
                if G == 1: file_name, bed1, bed2, bed3 = "room_info_boys.txt", "B1", "B2", "B3"
                elif G == 2: file_name, bed1, bed2, bed3 = "room_info_girls.txt", "G1", "G2", "G3"
                elif G == 0: file_name, bed1, bed2, bed3 = "room_info_others.txt", "O1", "O2", "O3"

                n = str(fir_name_entry.get()).strip()
                b = str(r4.get()).upper().strip()
                ln = str(last_name_entry.get()).lower()
                f = str(fathr_name_entry.get()).lower()
                m = str(mther_name_entry.get()).lower()
                d = str(dob_entry.get()).lower()
                add = str(addrs_entry.get()).lower()
                c = str(cont_entry.get()).strip()
                e = str(email_entry.get()).strip()
                w = str(place_entry.get()).lower()
                v = str(vehicle_entry.get()).lower()
                da = date().lower()
                rom = str(r2.get()).lower().strip()

                # ==========================================
                # NAYA FEATURE: STRICT VALIDATIONS ADDED
                # ==========================================
                if not n or not rom or not b:
                    messagebox.showerror("Validation Error", "Name, Room No. aur Bed No. can not be empty!")
                    return
                
                if len(c) != 10 or not c.isdigit():
                    messagebox.showerror("Validation Error", "Contact number should be exactly 10 digits!")
                    return

                if e and ("@" not in e or "." not in e):
                    messagebox.showerror("Validation Error", "Please enter a valid Email ID (like: abc@gmail.com)")
                    return
                # ==========================================

                f1 = open("student_info.txt", "a")
                f1.write(c + "," + n + " " + ln + "," + f + "," + m + "," + d + "," + e + "," + w + "," + v + "," + da + "," + b + "," + rom + "," + "\n")
                f1.close()
                
                fobj = open(file_name, "r")
                fdata_ls = fobj.readlines()
                fobj.close()
                rdate = date()
                fobj = open(file_name, "w")
                
                if b == bed1:
                    for oneline in fdata_ls:
                        if oneline.startswith(rom + ",") and oneline.__contains__(","+bed1):
                            new_oneline = oneline.replace(","+bed1+",", "," + c + ",")
                            new_oneline2 = new_oneline.replace(",NOT,", "," + rdate + ",")
                            fobj.write(new_oneline)
                        else: fobj.write(oneline)
                elif b == bed2:
                    for oneline in fdata_ls:
                        if oneline.startswith(rom + ",") and oneline.__contains__(","+bed2):
                            new_oneline = oneline.replace(","+bed2+"," , "," + c + ",")
                            new_oneline2 = new_oneline.replace(",NOT," , "," + rdate + ",")
                            fobj.write(new_oneline)
                        else: fobj.write(oneline)
                else:
                    for oneline in fdata_ls:
                        if oneline.startswith(rom + ",") and oneline.__contains__(","+bed3):
                            new_oneline = oneline.replace(","+bed3+"," , "," + c + ",")
                            new_oneline2 = new_oneline.replace(",NOT," , "," + rdate + ",")
                            fobj.write(new_oneline)
                        else: fobj.write(oneline)
                fobj.close()

                messagebox.showinfo("Success", "Student Added Successfully....!")

            Button(base, text="Add Student", font=("Arial 20 bold"), bg="white", fg="black" ,command=student).place(x=1040, y=700)

        c1 = IntVar()
        Radiobutton(base, text="Male", bg="silver", fg="black", font=("Arial 15 bold"), variable=c1, value=1, command=selected).place(x=490,y=580)
        Radiobutton(base, text="Female", bg="silver", fg="black", font=("Arial 15 bold"), variable=c1, value=2, command=selected).place(x=580,y=580)
        Radiobutton(base, text="Other", bg="silver", fg="black", font=("Arial 15 bold"), variable=c1, value=0, command=selected).place(x=680,y=580)
        Button(base, text="Continue", font=("Arial 15 bold"), bg="white", command=available_roome).place(x=490, y=670)
        Canvas(base, height=670, width=2).place(x=1000, y=105)

    def add_room():
        canvas = Canvas(base, bg='silver', height=675, width=1210)
        canvas.place(x=320, y=105)
        Label(base, text="Add New Room", bg="dark slate grey", font=("Arial 20 bold"), fg="white", padx=500, pady=10).place(x=320, y=105)
        Label(base, text="New Room No.", font=("Arial 20 bold"), bg="silver", fg="black").place(x=500, y=300)
        rm_n_entry = Entry(base, width=20, font=("Arial 15 bold"))
        rm_n_entry.place(x=750, y=303)
        Label(base,text="Gender", font=("Arial 20 bold"), bg="silver", fg="black").place(x=500,y=350)

        global G
        G = 1
        def selected():
            global G
            if c1.get() == 1: G = 1
            if c1.get() == 2: G = 2
            if c1.get() == 0: G = 0

        c1 = IntVar()
        Radiobutton(base, text="Male", bg="silver", fg="black", font=("Arial 15 bold"), variable=c1, value=1, command=selected).place(x=750, y=350)
        Radiobutton(base, text="Female", bg="silver", fg="black", font=("Arial 15 bold"), variable=c1, value=2, command=selected).place(x=840, y=350)
        Radiobutton(base, text="Other", bg="silver", fg="black", font=("Arial 15 bold"), variable=c1, value=0, command=selected).place(x=950, y=350)

        def add():
            r = str(rm_n_entry.get()).strip()
            
            # Validation for room
            if not r:
                messagebox.showerror("Error", "Room No. cannot be empty!")
                return
                
            if G==1: bed1, bed2, bed3, file_name = "B1", "B2", "B3", "room_info_boys.txt"
            elif G==2: bed1, bed2, bed3, file_name = "G1", "G2", "G3", "room_info_girls.txt"
            elif G==0: bed1, bed2, bed3, file_name = "O1", "O2", "O3", "room_info_others.txt"

            f2 = open(file_name, "r")
            all_lines = f2.readlines()
            count = 0
            for i in all_lines:
                if i.split(',')[0] == r:
                    messagebox.showerror("Error", "Room Is Already Added....!")
                    f2.close()
                    count = 2
                    break
            f2.close()
            
            if count != 2:
                f1 = open(file_name, "a")
                f1.write(r + "," + bed1 + "," + bed2 + "," + bed3 + ",NOT,\n")
                f1.close()
                messagebox.showinfo("Success", "ROOM Successfully Added....!")

        Button(base, text="Add Room", font=("Arial 20 bold"), bg="white", fg="black", command=add).place(x=550, y=500)

    def in_out_time():
        canvas = Canvas(base, bg='silver', height=675, width=1210)
        canvas.place(x=320, y=105)
        Label(base, text="---------------Outtime---------------", font=("Arial 20 bold"), bg="dark slate grey", fg="white", padx=20, pady=10).place(x=320, y=115)
        Label(base, text="Enter ID", font=("Arial 20 bold"), bg="silver", fg="black").place(x=470, y=200)
        out_time_entry = Entry(base, width=20, font=("Arial 20 bold"))
        out_time_entry.place(x=620, y=200)

        Label(base, text="Purpose", font=("Arial 20 bold"), bg="silver", fg="black").place(x=470, y=270)
        purpose_entry = Entry(base, width=20, font=("Arial 20 bold"))
        purpose_entry.place(x=620, y=270)

        def save1():
            Id = str(out_time_entry.get()).strip()
            pur1 = str(purpose_entry.get()).strip()
            
            # Validation
            if not Id or not pur1:
                messagebox.showerror("Error", "ID and Purpose are required!")
                return
                
            t = date()
            f1 = open("inouttime.txt", "a")
            f1.write(Id + "," + pur1 + "," + t + ",OUTTIME,REMARK\n")
            f1.close()
            messagebox.showinfo("Success", "Outtime Saved Successfully...!")

        Button(base, text="Save", font=("Arial 20 bold"), bg="white", fg="black", command=save1).place(x=1050, y=220)

        Label(base, text="---------------Inttime---------------", font=("Arial 20 bold"), bg="dark slate grey", fg="white", padx=20, pady=10).place(x=320, y=400)
        Label(base, text="Enter ID", font=("Arial 20 bold"), bg="silver", fg="black").place(x=470, y=500)
        in_time_entry = Entry(base, width=20, font=("Arial 20 bold"))
        in_time_entry.place(x=680, y=500)

        Label(base, text="Outtime Entry", font=("Arial 20 bold"), bg="silver", fg="black").place(x=470, y=550)
        ot_entry_entry = Entry(base, width=20, font=("Arial 20 bold"))
        ot_entry_entry.place(x=680, y=550)

        def search_outtime():
            s_id = str(in_time_entry.get())
            fobj = open("inouttime.txt", "r")
            fdata_ls = fobj.readlines()
            count = 1
            for oneline in fdata_ls:
                if oneline.startswith(s_id + ",") and oneline.__contains__(",OUTTIME,"):
                    count = 2
                    y = oneline.split(",")
                    tv = StringVar()
                    tv.set(y[2] + "     " + y[3])
                    ot = Entry(base, width=20, textvariable=tv, font=("Arial 20 bold"))
                    ot.place(x=680, y=550)
                    break
            fobj.close()
            if count == 1:
                messagebox.showerror("Error", "Invalid ID or No Outtime found!")

        def save2():
            sel_opt = str(r_sel.get())
            s_id = str(in_time_entry.get())
            fobj = open("inouttime.txt", "r")
            fdata_ls = fobj.readlines()
            fobj.close()
            rdate = date()
            count = 1
            fobj = open("inouttime.txt", "w")
            for oneline in fdata_ls:
                if oneline.startswith(s_id + ",") and oneline.__contains__(",OUTTIME,"):
                    new_oneline = oneline.replace(",OUTTIME,", "," + rdate + ",")
                    new_oneline2 = new_oneline.replace(",REMARK", "," + sel_opt + ",")
                    fobj.write(new_oneline2)
                    count = 2
                else:
                    fobj.write(oneline)
            if count == 2:
                messagebox.showinfo("Success", "Intime Saved Successful...!")
            if count == 1:
                messagebox.showerror("Error", "Please Give Correct Information")
            fobj.close()

        Button(base, text="Search Outtime", font=("Arial 18 bold"), bg="white", command=search_outtime).place(x=1050, y=520)
        Button(base, text="Save", font=("Arial 20 bold"), bg="white", fg="black", command=save2).place(x=1050, y=700)

        r_sel = StringVar(base)
        ls = ['Before Time', 'On Time', 'Late']
        r_sel.set(ls[0])
        remark = OptionMenu(base, r_sel, *ls)
        remark.config(width=20, font=("Arial 15 bold"), fg="black")
        remark.place(x=680, y=610)

    def visitor():
        canvas = Canvas(base, bg='silver', height=675, width=1210)
        canvas.place(x=320, y=105)
        Label(base, text="Visitor's   Information", bg="dark slate grey", font=("Arial 20 bold"), fg="white", padx=480, pady=10).place(x=320, y=105)
        
        Label(base, text="Name", font=("Arial 20 bold"), bg="silver", fg="black").place(x=500, y=200)
        v_name_entry = Entry(base, width=20, font=("Arial 20 bold"))
        v_name_entry.place(x=650, y=200)

        Label(base, text="Contact", font=("Arial 20 bold"), bg="silver", fg="black").place(x=500, y=300)
        v_contact_entry = Entry(base, width=20, font=("Arial 20 bold"))
        v_contact_entry.place(x=650, y=300)

        Label(base, text="Reason", font=("Arial 20 bold"), bg="silver", fg="black").place(x=500, y=400)
        v_reason_entry = Entry(base, width=20, font=("Arial 20 bold"))
        v_reason_entry.place(x=650, y=400)

        Label(base, text="Address", font=("Arial 20 bold"), bg="silver", fg="black").place(x=500, y=500)
        v_address_entry = Entry(base, width=20, font=("Arial 20 bold"))
        v_address_entry.place(x=650, y=500)

        Label(base, text="Student Name", font=("Arial 20 bold"), bg="silver", fg="black").place(x=1020, y=200)
        st_name_entry = Entry(base, width=15, font=("Arial 20 "))
        st_name_entry.place(x=1250, y=200)

        def search():
            def reset():
                st_name_entry.delete(0, END)

            def add_visitor():
                vn = str(v_name_entry.get()).strip()
                vcon = str(v_contact_entry.get()).strip()
                vr = str(v_reason_entry.get()).strip()
                vadd = str(v_address_entry.get()).strip()
                sn = str(st_name_entry.get()).strip()
                
                # --- Visitor Validation ---
                if not vn or not sn:
                    messagebox.showerror("Error", "Visitor Name and Student Name are required!")
                    return
                if len(vcon) != 10 or not vcon.isdigit():
                    messagebox.showerror("Error", "Contact number must be exactly 10 digits!")
                    return
                # --------------------------

                d = str(date())
                fp = open("visitor_info.txt", "a")
                fp.write(sn + "," + vn + "," + vcon + "," + vr + "," + vadd + "," + d + "\n")
                fp.close()
                messagebox.showinfo("Success", "Visitor Added Successfully...!")

            Button(base, text="Reset", font=("Arial 20 bold"), command=reset).place(x=1340, y=280)
            
            s_n = str(st_name_entry.get()).strip()
            if not s_n:
                messagebox.showerror("Error", "Please enter Student Name to search!")
                return
                
            fobj = open("student_info.txt", "r")
            fdata_ls = fobj.readlines()
            count = 1
            for oneline in fdata_ls:
                if oneline.__contains__("," + s_n + ","):
                    count = 2
                    y = oneline.split(",")
                    tv = StringVar()
                    tv.set(y[11])
                    Label(base, text="Room No.", font=("Arial 20 bold"), bg="silver").place(x=1020, y=400)
                    Entry(base, width=15, textvariable=tv, font=("Arial 20 bold"), justify=CENTER).place(x=1250, y=400)
                    Button(base, text="Add Visitor", font=("Arial 20 bold"), command=add_visitor).place(x=1100, y=500)
                    break
            fobj.close()
            if count == 1:
                messagebox.showerror("Error", "Student Name not found!")

        Canvas(base, height=650, width=5).place(x=1000, y=162)
        Button(base, text="Search", font=("Arial 20 bold"), command=search).place(x=1180, y=280)


    def view_info():
        canvas = Canvas(base, bg='silver', height=675, width=1215)
        canvas.place(x=320, y=105)

        def all_girl_info():
            canvas = Canvas(base, bg='silver', height=675, width=810)
            canvas.place(x=715, y=105)
            Label(base, text="Information Of Students", font=("Arial 20 bold"), bg="dark slate grey", fg="white", padx=270, pady=5).place(x=720, y=105)

            def export_to_excel():
                try:
                    f1 = open("student_info.txt", "r")
                    lines = f1.readlines()
                    f1.close()
                    with open("Students_Data.csv", "w", newline="") as f2:
                        writer = csv.writer(f2)
                        writer.writerow(["Contact", "Name", "Father Name", "Mother Name", "DOB", "Email", "Workplace", "Vehicle", "Date Added", "Bed No", "Room No"])
                        for line in lines:
                            writer.writerow(line.strip().split(','))
                    messagebox.showinfo("Export Success", "Data has been added to 'Students_Data.csv'!")
                except Exception as e:
                    messagebox.showerror("Error", f"Error aagaya: {e}")

            Button(base, text="Export To Excel", font=("Arial 12 bold"), bg="dark green", fg="white", command=export_to_excel).place(x=1350, y=110)

            Label(base, text="Room NO.            Name                Contact              Workplace", font=("Arial 20 bold"), bg="dark orange", fg="white").place(x=723, y=150)

            students = []
            try:
                f1 = open("student_info.txt", "r")
                all_lines = f1.readlines()
                f1.close()
                for i in all_lines:
                    temp = str(i)
                    one_line = temp.split(',')
                    if len(one_line) > 11:
                        students.append([one_line[11], one_line[1], one_line[0], one_line[6]])
            except: pass

            y1co = 200
            for i, y in enumerate(students):
                Label(base, text=y[0], font=("Arial 15 bold"), bg="silver", fg="black").place(x=800, y=y1co)
                Label(base, text=y[1], font=("Arial 15 bold"), bg="silver", fg='black').place(x=900, y=y1co)
                Label(base, text=y[2], font=('Arial 15 bold'), bg="silver", fg='black').place(x=1160, y=y1co)
                Label(base, text=y[3], font=("Arial 15 bold"), bg="silver", fg="black").place(x=1380, y=y1co)
                y1co += 50
                if i >= 7: break

        def room_wise():
            canvas = Canvas(base, bg='silver', height=675, width=810)
            canvas.place(x=715, y=105)
            Label(base, text="Enter Room No.", font=("Arial 20 bold"), bg="silver", fg="black").place(x=750, y=150)
            l1_entry = Entry(base, width=10, font=("Arial 20 bold"))
            l1_entry.place(x=1000, y=150)

            def search():
                r_no = str(l1_entry.get())
                try:
                    f1 = open("student_info.txt", "r")
                    all_lines = f1.readlines()
                    f1.close()
                except: all_lines = []
                r_info = []
                for i in all_lines:
                    one_line = str(i).split(',')
                    if len(one_line) > 11 and one_line[11] == r_no:
                        r_info.append([one_line[10], one_line[1], one_line[0], one_line[6]])
                        
                Label(base, text="Information Of Students", font=("Arial 20 bold"), bg="dark slate grey", fg="white", padx=270, pady=5).place(x=720, y=250)
                Label(base, text="Bed No.               Name                  Contact                Workplace", font=("Arial 20 bold"), bg="dark orange", fg="white").place(x=723, y=300)
                
                y1co = 400
                for i, y in enumerate(r_info):
                    Label(base, text=y[0], font=("Arial 15 bold"), bg="silver", fg="black").place(x=780, y=y1co)
                    Label(base, text=y[1], font=("Arial 15 bold"), bg="silver", fg='black').place(x=900, y=y1co)
                    Label(base, text=y[2], font=('Arial 15 bold'), bg="silver", fg='black').place(x=1160, y=y1co)
                    Label(base, text=y[3], font=("Arial 15 bold"), bg="silver", fg="black").place(x=1380, y=y1co)
                    y1co += 100
                    if i >= 2: break

            Button(base, text="Search", font=("Arial 20 bold"), command=search).place(x=1200, y=140)

        # DELETE STUDENT FEATURE
        Label(base, text="Delete Student", font=("Arial 20 bold"), bg="silver", fg="red").place(x=400, y=500)
        Label(base, text="Enter Hostel ID (Contact):", font=("Arial 12 bold"), bg="silver", fg="black").place(x=400, y=540)
        del_entry = Entry(base, width=15, font=("Arial 15 bold"))
        del_entry.place(x=400, y=570)

        def delete_student():
            h_id = del_entry.get().strip()
            if not h_id:
                messagebox.showwarning("Warning", "Please enter Hostel ID!")
                return
            if not messagebox.askyesno("Confirm", f"Delete student with ID: {h_id}?"):
                return
            
            try:
                with open("student_info.txt", "r") as f:
                    lines = f.readlines()
            except:
                messagebox.showerror("Error", "Student data not found!")
                return

            found = False
            room_no = bed_no = gender_file = ""
            new_lines = []

            for line in lines:
                parts = line.split(',')
                if len(parts) > 11 and parts[0] == h_id:
                    found = True
                    bed_no = parts[9]
                    room_no = parts[10]
                    if bed_no.startswith('B'): gender_file = "room_info_boys.txt"
                    elif bed_no.startswith('G'): gender_file = "room_info_girls.txt"
                    elif bed_no.startswith('O'): gender_file = "room_info_others.txt"
                else:
                    new_lines.append(line)

            if not found:
                messagebox.showerror("Error", "Student not found!")
                return
            
            with open("student_info.txt", "w") as f:
                f.writelines(new_lines)
            
            if gender_file:
                try:
                    with open(gender_file, "r") as f: r_lines = f.readlines()
                    with open(gender_file, "w") as f:
                        for rline in r_lines:
                            if rline.startswith(room_no + ","):
                                rline = rline.replace("," + h_id + ",", "," + bed_no + ",")
                            f.write(rline)
                except: pass

            messagebox.showinfo("Success", f"Student Deleted!\nBed {bed_no} in Room {room_no} is free.")
            del_entry.delete(0, END)

        Button(base, text="Delete", font=("Arial 15 bold"), bg="red", fg="white", command=delete_student).place(x=590, y=565)

        Button(base, text="Information Of All Students", wraplength=180, justify=CENTER, font=("Arial 20 bold"), padx=50, pady=1, command=all_girl_info).place(x=400, y=200)
        Button(base, text="Room Info", font=("Arial 20 bold"), padx=60, pady=5, command=room_wise).place(x=400, y=400)
        Canvas(base, height=680, width=5).place(x=710, y=105)

    def leave_application():
        canvas = Canvas(base, bg='silver', height=675, width=1210)
        canvas.place(x=320, y=105)
        Label(base, text="Leave Application", bg="dark slate grey", font=("Arial 20 bold"), fg="white", padx=485, pady=10).place(x=320, y=105)

        Label(base, text="Hostel ID", bg="silver", font=("Arial 20 bold"), fg="black").place(x=400, y=200)
        id_entry = Entry(base, width=15, font=("Arial 20"))
        id_entry.place(x=550, y=200)

        Label(base, text="Name", bg="silver", font=("Arial 20 bold"), fg="black").place(x=800, y=200)
        n_entry = Entry(base, width=20, font=("Arial 20"))
        n_entry.place(x=900, y=200)

        Label(base, text="Room No.", bg="silver", font=("Arial 20 bold"), fg="black").place(x=400, y=300)
        r_entry = Entry(base, width=15, font=("Arial 20"))
        r_entry.place(x=550, y=300)

        Label(base, text="Mobile No.", bg="silver", font=("Arial 20 bold"), fg="black").place(x=800, y=300)
        m_entry = Entry(base, width=15, font=("Arial 20"))
        m_entry.place(x=950, y=300)

        Label(base, text="Reason For Leave", bg="silver", font=("Arial 20 bold"), fg="black").place(x=400, y=400)
        reason_entry = Entry(base, width=20, font=("Arial 20"))
        reason_entry.place(x=700, y=400)

        Label(base, text="Return Date", bg="silver", font=("Arial 20 bold"), fg="black").place(x=400, y=500)
        Label(base, text="(YEAR-MM-DD)", font=("Arial 15 bold"), bg="silver", fg="black").place(x=1000, y=500)
        date_entry = Entry(base, width=18, font=("Arial 20"))
        date_entry.place(x=700, y=500)

        def leave_info():
            i, n, r = str(id_entry.get()).strip(), str(n_entry.get()), str(r_entry.get())
            m, reas, rdate = str(m_entry.get()).strip(), str(reason_entry.get()), str(date_entry.get())
            
            # --- Leave Validation ---
            if not i or not n:
                messagebox.showerror("Error", "Hostel ID aur Name zaroori hain!")
                return
            if len(m) != 10 or not m.isdigit():
                messagebox.showerror("Error", "Mobile number exactly 10 digits ka hona chahiye!")
                return
            # ------------------------

            fopen = open("leave_applications.txt", "a")
            fopen.write(i + "," + n + "," + r + "," + m + "," + reas + "," + date() + "," + rdate + "\n")
            fopen.close()
            messagebox.showinfo("Success", "Leave Application Submitted Successfully!")

        Button(base, text="Submit", font=("Arial 20 bold"), fg="black", command=leave_info).place(x=700, y=600)

    Button(base, text="Add Student", font=("Arial 20 bold"), padx=15, bg="white", command=add_stud).place(x=50, y=150)
    Button(base, text="Add New Room", font=("Arial 20 bold"), bg="white", command=add_room).place(x=50, y=250)
    Button(base, text="In And Outtime", font=("Arial 20 bold"), bg="white", command=in_out_time).place(x=50, y=350)
    Button(base, text="Visitor", font=("Arial 20 bold"), bg="white", padx=55, command=visitor).place(x=50, y=450)
    Button(base, text="View Information", font=("Arial 18 bold"), bg="white", command=view_info).place(x=50, y=535)
    Button(base, text="Leave Application", font=("Arial 18 bold"), bg="white", command=leave_application).place(x=50, y=620)
    Button(base, text="EXIT", font=("Arial 18 bold"), bg="white", padx=70, command=quit).place(x=50, y=700)

Label(base, text="Username", font=("Arial 25 bold"), bg="silver", fg="black").place(x=470, y=240)
user_entry = Entry(base, width=17, font=("Arial 20"))
user_entry.place(x=650, y=245)
user_entry.focus()

Label(base, text="Password", font=("Arial 25 bold"), bg="silver", fg="black").place(x=470, y=350)
pass_entry = Entry(base, width=17, font="Arial 20", show="*")
pass_entry.place(x=650, y=355)

def login():
    # YAHAN SE AAP USERNAME PASSWORD CHANGE KAR SAKTE HAIN
    id = str(user_entry.get())
    key = str(pass_entry.get())
    if id == "admin" and key == "1234":
        main()
    else:
        user_entry.focus()
        user_entry.delete(0, END)
        pass_entry.delete(0, END)
        messagebox.showerror("Login Failed", "Wrong Username Or Password...!")

Button(base, text="Login", font=("Arial 25 bold"), bg="lightseagreen", fg="white", command=login).place(x=650, y=440)

base.mainloop()
