# Γεράσιμος Χριστοφύλλης
# Έκδοση: 4

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
    ["Stavropoulou","Pashalis","Mihalopoulos","Pandosti","Efthimiadis","Trikatsoula","Karageorgi","Maniatis","Kalogeraki","Kalatha","empty"],#'Ολοι δάσκαλοι για Α1
    ["Stavropoulou","Georgikou","Mihalopoulos","Pandosti","Efthimiadis","Sakka","Karageorgi","Maniatis","Kalogeraki","Kalatha","empty"],#'Ολοι δάσκαλοι για Α2
    ["Stavropoulou","Georgikou","Mihalopoulos","Pantosti","Efthimiadis","Maniatis","Dispiraki","Kalogeraki","Spanos","empty"],#'Ολοι δάσκαλοι για Βγ
    ["Stavropoulou","Georgikou","Mihalopoulos","Pantosti","Efthimiadis","Skokos","Karadzoulias","Spanos","empty"],#'Ολοι δάσκαλοι για Βμ
    ["Stavropoulou","Georgikou","Mihalipoulos","Pantosti","Efthimiadis","Sakka","Trikatsoula","Karageorgi","Spanos","empty"],#'Ολοι δάσκαλοι για Βο
    ["Stavropoulou","Georgikou","Mihalipoulos","Efthimiadis","Tserpe","Zevgitis","Kalatha","Dimopoulos","Spanos","empty"],#'Ολοι δάσκαλοι για Βπ
    ["Stavropoulou","Georgikou","Mihalipoulos","Pantosti","Efthimiadis","Skokos","Karatzoulias","Spanos","empty"],#'Ολοι δάσκαλοι για Γαφ
    ["Stavropoulou","Georgikou","Mihalipoulos","Pantosti","Efthimiadis","Maniatis","Dispiraki","Kalogeraki","Spanos","empty"],#'Ολοι δάσκαλοι για Γγ
    ["Stavropoulou","Georgikou","Mihalipoulos","Pantosti","Efthimiadis"," Sakka","Trikatsoula","Karageorgi","Spanos","empty"],#'Ολοι δάσκαλοι για Γο
    ["Stavropoulou","Georgikou","Michalopoulos","Pandosti","Efthimiadis","Tserpe","Zevgitis","Kalatha","Dimopoulos","Spanos","empty"]#'Ολοι δάσκαλοι για Γπ
    ]

teacher_index_list=[
    range(1,12),#Δείκτες επολογής μενού για επώνυμα δασκάλων Α1, 
    range(1,12),#Δείκτες επολογής μενού για επώνυμα δασκάλων Α2
    range(1,11),#Δείκτες επολογής μενού για επώνυμα δασκάλων Βγ
    range(1,10),#Δείκτες επολογής μενού για επώνυμα δασκάλων Βμ
    range(1,11),#Δείκτες επολογής μενού για επώνυμα δασκάλων Βο
    range(1,11),#Δείκτες επολογής μενού για επώνυμα δασκάλων Βπ
    range(1,10),#Δείκτες επολογής μενού για επώνυμα δασκάλων Γαφ
    range(1,11),#Δείκτες επολογής μενού για επώνυμα δασκάλων Γγ
    range(1,11),#Δείκτες επολογής μενού για επώνυμα δασκάλων Γο
    range(1,12)#Δείκτες επολογής μενού για επώνυμα δασκάλων Γπ
    ]

taxi_tmima_name_list=["A1","A2","Bg","Bm","Bo","Bp","Gaf","Gg","Go","Gp"]
taxi_tmima_index_list=[1,2,3,4,5,6,7,8,9,10]
menu_range_variable_list=[]
for i in range(10):
    menu_range_variable_list.append(len(teacher_name_list[i]))

def choose_day():
    global day_search,day_index
    repeat=True
    while repeat==True:
        try:
            day=input("Choose day, 1 for Monday, 2 for Tuesday, 3 for Wednesday, 4 for Thursday, 5 for Friday:")
            print '\n'
        except:
            print "ERROR: Try again"
        else:
            while not(type(day)==int and day>=1 and day<=5):
                print "ERROR: Try again"
                day=input("Choose day, 1 for Monday, 2 for Tuesday, 3 for Wednesday, 4 for Thursday, 5 for Friday:")
                print '\n'
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
        except:
            print "ERROR: Try again"
        else:
            while not(type(hour)==int and hour>=1 and hour<=7):
                print "ERROR: Try again"
                hour=input("Choose lesson of the day, 1-7:")
                print '\n'
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
        except:
            print "ERROR: Try again"
        else:
            while not(type(teacher)==int and teacher>=1 and teacher<=menu_range_variable):
                print "ERROR: Try again"
                teacher=input("choose teacher by number,1-11:")
                print '\n'
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
    print "Confirm allocation of teacher",teacher_name,"for",day_search,hour_search,"during the time frame",lesson_time_list[hour_index]
    confirm=raw_input("y for YES, any key for NO:")
    print '\n'
    if confirm=="y":
        class_table[taxi_tmima_index][day_index][hour_index]=teacher_name
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
    elif len(teacher_week_day)>0 and teacher_index!=menu_range_variable:
        for i in range(len(teacher_week_day)):
            print "The teacher",teacher_name,"is scheduled for",day_search_list[teacher_week_day[i]],"for the",hour_search_list[teacher_week_lesson[i]]
    elif len(teacher_week_day)==0 and teacher_index==menu_range_variable:
        print "There are no gaps with missing teachers in the schedule for the whole weeks"
    elif len(teacher_week_day)==0 and teacher_index!=menu_range_variable:
        print "The teacher",teacher_name,"is not available for lessons this week or has not been scheduled yet for this week."
    print '\n'

def taxi_tmima_menu():
    repeat=True
    while repeat==True:
        try:
            print "For grade/vocational department",taxi_tmima_name
            menu=input("1: Change one lesson, 2: View one lesson, 3: View schedule for one day, 4: View weekly schedule for one teacher, 0 to return to main menu>")
        except:
            print "ERROR: Try again"
        else:
            while not(type(menu)==int and menu>=0 and menu<=4):
                print "ERROR: Try again"
                menu=input("1: Change one lesson, 2: View one lesson, 3: View schedule for one day, 4: View weekly schedule for one teacher, 0 to return to main menu>")
            print '\n'
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
                print "Displaying weekly lesson table for chosen grade and vocational department",taxi_tmima_name
                print '\n'
                for i in range(5):
                    taxi_tmima_weekly_table=range(7)
                    for n in range(7):
                        if class_table[taxi_tmima_index][i][n]=="empty":
                            taxi_tmima_weekly_table[n]=class_table[taxi_tmima_index][i][n]
                        else:
                            taxi_tmima_weekly_table[n]=class_table[taxi_tmima_index][i][n]+"_"+taxi_tmima_name
                    print day_search_list[i],'\t','\t',taxi_tmima_weekly_table
                    print '\n'
                print "Returning to main menu."
                print '\n'

taxi_tmima_input=-1
while taxi_tmima_input!=0:
    print "Choose the grade/vocaltional department combination for all general and vocational teachers in that specific combination"
    print '\n'
    for i in range(10):
        print "Choose",taxi_tmima_index_list[i],"for",taxi_tmima_name_list[i]
    print "Choose 0 to exit program"
    print '\n'
    try:
        taxi_tmima_input=input("Choose grade and department:")
        print '\n'
    except:
        print "ERROR: Try again"
    else:
        while not(type(taxi_tmima_input)==int and taxi_tmima_input>=0 and taxi_tmima_input<=10):
            print "ERROR: Try again"
            print "Choose the grade/vocaltional department combination for all general and vocational teachers in that specific combination"
            print '\n'
            for i in range(10):
                print "Choose",taxi_tmima_index_list[i],"for",taxi_tmima_name_list[i]
            taxi_tmima_input=input("Choose grade and department:")
            print '\n'
        if taxi_tmima_input==0:
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
                
            
            
            
        
        
    




