# Γεράσιμος Χριστοφύλλης
# Έκδοση: 5

import json
try:
    lesson_table_filename='lesson_table.json'
    with open(lesson_table_filename,'r') as lesson_table_file:
        lesson_table=json.load(lesson_table_file)
except:
    print "ERROR: Lesson table/list file not present, creating new file, lesson_table.json in the same folder as this script"
    print '\n'
    class_table=[]
    for tmima in range(10):
        lesson_week=[]
        for day in range(5):
            lesson_hour=[]
            for hour in range(7):
                lesson_hour.append("empty")
            lesson_week.append(lesson_hour)
        class_table.append(lesson_week)
else:
    print "Lesson table file 'lesson_table.json' found and loading to list 'class_table'."
    print '\n'
    class_table=lesson_table

day_search_list=["Monday","Tuesday","Wednesday","Thursday","Friday"]
day_index_list=[1,2,3,4,5]

hour_search_list=["1st lesson","2nd lesson","3rd lesson","4th lesson","5th lesson","6th lesson","7th lesson"]
hour_index_list=[1,2,3,4,5,6,7]
lesson_time_list=["8:20-9:05","9:10-9:50","10:00-10:40","10:50-11:30","11:40-12:20","12:25-13:05","13:10-13:50"]

teacher_name_list=[
    ["Stavropoulou","Pashalis","Mihalopoulos","Efthimiadis","Trikatsoula","Karageorgi","Kapaklis","Maniatis","Kalogeraki","Kalatha","empty"],#'Ολοι δάσκαλοι γενικής και ειδικής για μαθητές Α1
    ["Stavropoulou","Georgikou","Mihalopoulos","Efthimiadis","Sakka","Karageorgi","Kapaklis","Maniatis","Kalogeraki","Kalatha","empty"],#'Ολοι δάσκαλοι γενικής και ειδικής για μαθητές Α2
    ["Stavropoulou","Georgikou","Mihalopoulos","Efthimiadis","Maniatis","Dispiraki","Kalogeraki","Spanos","empty"],#'Ολοι δάσκαλοι γενικής και ειδικής για μαθητές Βγ
    ["Stavropoulou","Georgikou","Mihalopoulos","Efthimiadis","Skokos","Karadzoulias","Kapaklis","Spanos","empty"],#'Ολοι δάσκαλοι γενικής και ειδικής για μαθητές Βμ
    ["Stavropoulou","Georgikou","Mihalopoulos","Efthimiadis","Sakka","Trikatsoula","Karageorgi","Spanos","empty"],#'Ολοι δάσκαλοι γενικής και ειδικής για μαθητές Βο
    ["Stavropoulou","Georgikou","Mihalopoulos","Efthimiadis","Tserpe","Kalatha","Dimopoulos","Spanos","empty"],#'Ολοι δάσκαλοι γενικής και ειδικής για μαθητές Βπ
    ["Stavropoulou","Georgikou","Mihalopoulos","Rovoli","Efthimiadis","Skokos","Karadzoulias","Kapaklis","Spanos","empty"],#'Ολοι δάσκαλοι γενικής και ειδικής για μαθητές Γαφ
    ["Stavropoulou","Georgikou","Mihalopoulos","Rovoli","Efthimiadis","Maniatis","Dispiraki","Kalogeraki","Spanos","empty"],#'Ολοι δάσκαλοι γενικής και ειδικής για μαθητές Γγ
    ["Stavropoulou","Georgikou","Mihalopoulos","Rovoli","Efthimiadis","Sakka","Trikatsoula","Karageorgi","Spanos","empty"],#'Ολοι δάσκαλοι γενικής και ειδικής για μαθητές Γο
    ["Stavropoulou","Georgikou","Mihalopoulos","Rovoli","Efthimiadis","Tserpe","Kalatha","Dimopoulos","Spanos","empty"]#'Ολοι δάσκαλοι γενικής και ειδικής για μαθητές Γπ
    ]

teacher_index_list=[
    range(1,len(teacher_name_list[0])+1),#Δείκτες επολογής μενού για επώνυμα δασκάλων Α1, 
    range(1,len(teacher_name_list[1])+1),#Δείκτες επολογής μενού για επώνυμα δασκάλων Α2
    range(1,len(teacher_name_list[2])+1),#Δείκτες επολογής μενού για επώνυμα δασκάλων Βγ
    range(1,len(teacher_name_list[3])+1),#Δείκτες επολογής μενού για επώνυμα δασκάλων Βμ
    range(1,len(teacher_name_list[4])+1),#Δείκτες επολογής μενού για επώνυμα δασκάλων Βο
    range(1,len(teacher_name_list[5])+1),#Δείκτες επολογής μενού για επώνυμα δασκάλων Βπ
    range(1,len(teacher_name_list[6])+1),#Δείκτες επολογής μενού για επώνυμα δασκάλων Γαφ
    range(1,len(teacher_name_list[7])+1),#Δείκτες επολογής μενού για επώνυμα δασκάλων Γγ
    range(1,len(teacher_name_list[8])+1),#Δείκτες επολογής μενού για επώνυμα δασκάλων Γο
    range(1,len(teacher_name_list[9])+1)#Δείκτες επολογής μενού για επώνυμα δασκάλων Γπ
    ]

taxi_tmima_name_list=["A1","A2","Bg","Bm","Bo","Bp","Gaf","Gg","Go","Gp"]
taxi_tmima_index_list=[1,2,3,4,5,6,7,8,9,10]
menu_range_variable_list=[]
for i in range(10):
    menu_range_variable_list.append(len(teacher_name_list[i]))

general_studies_teachers=["Stavropoulou","Georgikou","Pashalis","Mihalopoulos","Rovoli","Efthimiadis","Spanos"]

all_teachers=[
    "Stavropoulou",
    "Georgikou",
    "Pashalis",
    "Mihalopoulos",
    "Rovoli",
    "Efthimiadis",
    "Trikatsoula",
    "Karageorgi",
    "Skokos",
    "Karadzoulias",
    "Kapaklis",
    "Maniatis",
    "Dispiraki",
    "Kalogeraki",
    "Tserpe",
    "Kalatha",
    "Dimopoulos",
    "Spanos",
    "EXIT"
    ]

def choose_day():
    global day_search,day_index
    repeat=True
    while repeat==True:
        try:
            day=input("Choose day, 1 for Monday, 2 for Tuesday, 3 for Wednesday, 4 for Thursday, 5 for Friday:")
            print '\n'
            while not(type(day)==int and day>=1 and day<=5):
                print "ERROR: Try again"
                day=input("Choose day, 1 for Monday, 2 for Tuesday, 3 for Wednesday, 4 for Thursday, 5 for Friday:")
                print '\n'
        except:
            print "ERROR: Try again"
        else:
            for i,n in zip((day_search_list),(day_index_list)):
                if n==day:
                    day_search,day_index=i,n-1
            repeat=False

def choose_lesson():
    global hour_search,hour_index
    repeat=True
    while repeat==True:
        try:
            hour=input("Choose lesson of the day, 1-7:")
            print '\n'
            while not(type(hour)==int and hour>=1 and hour<=7):
                print "ERROR: Try again"
                hour=input("Choose lesson of the day, 1-7:")
                print '\n'
        except:
            print "ERROR: Try again"
        else:
            for i,n in zip((hour_search_list),(hour_index_list)):
                if n==hour:
                    hour_search,hour_index=i,n-1
            repeat=False

def choose_teacher():
    global teacher_name,teacher_index
    for i in range(menu_range_variable):
        print "choose",teacher_index_list[taxi_tmima_index][i],"for",teacher_name_list[taxi_tmima_index][i]
    repeat=True
    while repeat==True:
        try:
            print "Choose teacher in range from 1-",menu_range_variable,":"
            teacher=input("=>>")
            print '\n'
            while not(type(teacher)==int and teacher>=1 and teacher<=menu_range_variable):
                print "ERROR: Try again"
                print "Choose teacher in range from 1-",menu_range_variable,":"
                teacher=input("=>>")
                print '\n'
        except:
            print "ERROR: Try again"
        else:
            for i,n in zip((teacher_index_list[taxi_tmima_index]),(teacher_name_list[taxi_tmima_index])):
                if i==teacher:
                    teacher_index,teacher_name=i,n
            repeat=False

def change_data():
    print "Choose the day and lesson time to schedule a teacher and choose teacher name."
    print "for the grade/vocational department",taxi_tmima_name
    print '\n'
    choose_day()
    choose_lesson()
    choose_teacher()
    conflict=False
    other_tmima_index=-1
    conflict_list=[]
    for compare_index in range(10):
        past_teach_booking=class_table[compare_index][day_index][hour_index]
        if compare_index!=taxi_tmima_index and past_teach_booking!="empty" and past_teach_booking==teacher_name:
            conflict=True
            other_tmima_index=compare_index
            conflict_list.append(compare_index)
    past_teach_booking=class_table[other_tmima_index][day_index][hour_index]
    if conflict==True:
        print "The teacher",teacher_name,"is already scheduled for",day_search,hour_search,"during the time frame",lesson_time_list[hour_index]
        if teacher_name in general_studies_teachers and other_tmima_index>=2 and other_tmima_index<=5:
            print "with the general studies class for B1. The new lesson booking will delete"
            print "the conflicting old booking for all students in B1"
        elif teacher_name in general_studies_teachers and other_tmima_index>=6 and other_tmima_index<=9:
            print "with the general studies class for G1. The new lesson booking will delete"
            print "the conflicting old booking for all students in G1"
        else:
            print "with the vocational department",taxi_tmima_name_list[other_tmima_index]
            print "The new lesson booking will delete the conflicting old booking with department",taxi_tmima_name_list[other_tmima_index]
    if teacher_name=="empty":
        print "Confirm allocation of lesson gap for",day_search,hour_search,"during the time frame",lesson_time_list[hour_index],"for",taxi_tmima_name
    else:
        print "Confirm allocation of teacher",teacher_name,"for",day_search,hour_search,"during the time frame",lesson_time_list[hour_index],"for",taxi_tmima_name
    confirm=raw_input("y for YES, any key for NO:")
    print '\n'
    if confirm=="y":
        if teacher_name in general_studies_teachers:
            if taxi_tmima_index==0 or taxi_tmima_index==1:
                class_table[taxi_tmima_index][day_index][hour_index]=teacher_name
            elif taxi_tmima_index>=2 and taxi_tmima_index<=5:
                print "This booking with",teacher_name,"also applies for students in vocational department"
                for i in range(2,6):
                    class_table[i][day_index][hour_index]=teacher_name
                    if i!=taxi_tmima_index:
                        print taxi_tmima_name_list[i],
                print "This is a general class, please check your individual weekly student itinerary"
                print '\n'
            else:
                print "This booking with",teacher_name,"also applies for students in vocational department"
                for i in range(6,10):
                    class_table[i][day_index][hour_index]=teacher_name
                    if i!=taxi_tmima_index:
                        print taxi_tmima_name_list[i],
                print "This is a general class, please check your individual weekly student itinerary"
                print '\n'
        else:
            if class_table[taxi_tmima_index][day_index][hour_index] in general_studies_teachers:
                class_table[taxi_tmima_index][day_index][hour_index]=teacher_name
                if taxi_tmima_index>=2 and taxi_tmima_index<=5:
                    print "This is a vocational lesson replacing a general studies lesson. A gap will replace"
                    print "the other grade B schedules in the same day and time for vocational departments"
                    for i in range(2,6):
                        if i!=taxi_tmima_index:
                            print taxi_tmima_name_list[i],
                            class_table[i][day_index][hour_index]="empty"
                elif taxi_tmima_index>=6 and taxi_tmima_index<=9:
                    print "This is a vocational lesson replacing a general studies lesson. A gap will replace"
                    print "the other grade B schedules in the same day and time for vocational departments"
                    for i in range(6,10):
                        if i!=taxi_tmima_index:
                            print taxi_tmima_name_list[i],
                            class_table[i][day_index][hour_index]="empty"
            else:
                class_table[taxi_tmima_index][day_index][hour_index]=teacher_name
        if conflict==True:
            if past_teach_booking in general_studies_teachers:
                if other_tmima_index==0 or other_tmima_index==1:
                    class_table[other_tmima_index][day_index][hour_index]="empty"
                elif other_tmima_index>=2 and other_tmima_index<=5:
                    if other_tmima_index>=2 and other_tmima_index<=5 and taxi_tmima_index>=2 and taxi_tmima_index<=5:
                        print "ERROR: CONFLICT MISIDENTIFIED: False conflict between",taxi_tmima_name_list[taxi_tmima_index],"and"
                        for i in conflict_list:
                            print taxi_tmima_name_list[i],
                        print "all vocational departments in grade B must attend the same general studies lesson for grade B"
                        print '\n'
                    else:
                        for i in range(2,6):
                            class_table[i][day_index][hour_index]="empty"
                else:
                    if other_tmima_index>=6 and other_tmima_index<=9 and taxi_tmima_index>=6 and taxi_tmima_index<=9:
                        print "ERROR: CONFLICT MISIDENTIFIED: False conflict between",taxi_tmima_name_list[taxi_tmima_index],"and"
                        for i in conflict_list:
                            print taxi_tmima_name_list[i],
                        print "all vocational departments in grade G must attend the same general studies lesson for grade G"
                        print '\n'
                    else:
                        for i in range(6,10):
                            class_table[i][day_index][hour_index]="empty"    
            else:
                class_table[other_tmima_index][day_index][hour_index]="empty"
            conflict=False
        print "Allocation confirmed"
        print '\n'
    else:
        print "Teacher allocation CANCELLED"
        print '\n'
    
def read_data():
    print "Choose the day and time of lesson to show teacher scheduled for that lesson."
    print "for the grade/vocational department",taxi_tmima_name
    print '\n'
    choose_day()
    choose_lesson()
    if class_table[taxi_tmima_index][day_index][hour_index]!="empty":
        print "The teacher",class_table[taxi_tmima_index][day_index][hour_index],"is scheduled for",day_search,hour_search,"during the time frame",lesson_time_list[hour_index]
    else:
        print "There is a lesson gap scheduled for",day_search,hour_search,"during the time frame",lesson_time_list[hour_index]
    print '\n'

def read_day():
    print "Choose a school day to show class schedule for that day."
    print "for the grade/vocational department",taxi_tmima_name
    print '\n'
    choose_day()
    print "schedule for",day_search
    print '\n'
    for i in range(7):
        print hour_search_list[i],lesson_time_list[i],'\t','\t',class_table[taxi_tmima_index][day_index][i]
        print '\n'

def read_teacher():
    print "Choose a teacher to show all days and times that are scheduled for that teacher for the whole week."
    print "for the grade/vocational department",taxi_tmima_name
    print '\n'
    choose_teacher()
    teacher_week_day=[]
    teacher_week_lesson=[]
    for i in range(5):
        for n in range(7):
            if teacher_name==class_table[taxi_tmima_index][i][n]:
                teacher_week_day.append(i)
                teacher_week_lesson.append(n)
    if len(teacher_week_day)>0 and teacher_index==menu_range_variable:
        for i in range(len(teacher_week_day)):
            print "There is a gap with no teacher on",day_search_list[teacher_week_day[i]],"during the",hour_search_list[teacher_week_lesson[i]]
            print "for the grade and vocational department of",taxi_tmima_name
    elif len(teacher_week_day)>0 and teacher_index!=menu_range_variable:
        for i in range(len(teacher_week_day)):
            print "The teacher",teacher_name,"is scheduled for",day_search_list[teacher_week_day[i]],"for the",hour_search_list[teacher_week_lesson[i]]
            print "for the grade and vocational department of",taxi_tmima_name
    elif len(teacher_week_day)==0 and teacher_index==menu_range_variable:
        print "There are no gaps with missing teachers in the schedule for the whole weeks"
        print "for the grade and vocational department of",taxi_tmima_name
    elif len(teacher_week_day)==0 and teacher_index!=menu_range_variable:
        print "The teacher",teacher_name,"is not available for lessons this week or has not been scheduled yet for this week"
        print "for the grade and vocational department of",taxi_tmima_name
    print '\n'

def taxi_tmima_menu():
    repeat=True
    while repeat==True:
        try:
            print "For grade/vocational department",taxi_tmima_name
            menu=input("1: Change one lesson, 2: View one lesson, 3: View schedule for one day, 4: View weekly schedule for one teacher, 0 to return to main menu>")
            print '\n'
            while not(type(menu)==int and menu>=0 and menu<=4):
                print "ERROR: Try again"
                print "For grade/vocational department",taxi_tmima_name
                menu=input("1: Change one lesson, 2: View one lesson, 3: View schedule for one day, 4: View weekly schedule for one teacher, 0 to return to main menu>")
            print '\n'
        except:
            print "ERROR: Try again"
        else:
            if menu==1:
                change_data()
            elif menu==2:
                read_data()
            elif menu==3:
                read_day()
            elif menu==4:
                read_teacher()
            else:
                repeat=False
                print "Weekly individual student itinerary, general and vocational lessons for",taxi_tmima_name
                print '\n'
                for i in range(5):
                    taxi_tmima_weekly_table=range(7)
                    for n in range(7):
                        teacher=class_table[taxi_tmima_index][i][n]
                        if teacher=="empty":
                            taxi_tmima_weekly_table[n]="empty"
                        else:
                            if taxi_tmima_index<2:
                                taxi_tmima_weekly_table[n]=teacher+"_"+taxi_tmima_name
                            elif taxi_tmima_index>=2 and taxi_tmima_index<=5:
                                if teacher in general_studies_teachers:
                                    taxi_tmima_weekly_table[n]=teacher+"_"+"B1"
                                else:
                                    taxi_tmima_weekly_table[n]=teacher+"_"+taxi_tmima_name
                            else:
                                if teacher in general_studies_teachers:
                                    taxi_tmima_weekly_table[n]=teacher+"_"+"G1"
                                else:
                                    taxi_tmima_weekly_table[n]=teacher+"_"+taxi_tmima_name  
                    print day_search_list[i],'\t','\t',taxi_tmima_weekly_table
                    print '\n'
                print "Returning to main menu."
                print '\n'

taxi_tmima_input=-1
while taxi_tmima_input!=0:
    print "Choose the grade/vocational department combination for all general and vocational teachers in that specific combination"
    print '\n'
    for i in range(10):
        print "Choose",taxi_tmima_index_list[i],"for",taxi_tmima_name_list[i]
    print "Choose 0 to exit program"
    print '\n'
    try:
        taxi_tmima_input=input("Choose grade and department:")
        print '\n'
        while not(type(taxi_tmima_input)==int and taxi_tmima_input>=0 and taxi_tmima_input<=10):
            print "ERROR: Try again"
            print "Choose the grade/vocaltional department combination for all general and vocational teachers in that specific combination"
            print '\n'
            for i in range(10):
                print "Choose",taxi_tmima_index_list[i],"for",taxi_tmima_name_list[i]
            print "Choose 0 to exit program"
            print '\n'
            taxi_tmima_input=input("Choose grade and department:")
            print '\n'
    except:
        print "ERROR: Try again"
    else:
        if taxi_tmima_input==0:
            print "Show schedule for whole week and all classed for 1 teacher before exit"
            print "List of all teachers"
            for i in range(19):
                print "Choose",i,"for",'\t',all_teachers[i]
            print '\n'
            teacher_choice=-1
            while teacher_choice!=18:
                try:
                    teacher_choice=input("Choose teacher from menu number:0-18>>")
                    while not(type(teacher_choice)==int and teacher_choice>=0 and teacher_choice<=18):
                        print "ERROR: Try again"
                        teacher_choice=input("Choose teacher from menu number:0-18>>")
                        print '\n'
                except:
                    print "ERROR: Try again"
                else:
                    if teacher_choice!=18:
                        for i in range(10):
                            for m in range(5):
                                for n in range(7):
                                    if all_teachers[teacher_choice]==class_table[i][m][n]:
                                        print "The teacher",all_teachers[teacher_choice],"is scheduled for",taxi_tmima_name_list[i],day_search_list[m],hour_search_list[n]
                        print '\n'
                    else:
                        lesson_table_filename='lesson_table.json'
                        with open(lesson_table_filename,'w') as lesson_table_file:
                            json.dump(class_table,lesson_table_file)
                        print "Lesson table saved in the same folder as this script."
                        print "Confirming the lesson table has been saved from 'class_table' list to 'lesson_table.json'."
                        print "End program"
        else:
            for i,m,n in zip((taxi_tmima_name_list),(taxi_tmima_index_list),(menu_range_variable_list)):
                if m==taxi_tmima_input:
                    taxi_tmima_name,taxi_tmima_index,menu_range_variable=i,m-1,n
            taxi_tmima_menu()
                
            
            
            
        
        
    




