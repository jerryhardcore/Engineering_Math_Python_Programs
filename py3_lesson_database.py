# Γεράσιμος Χριστοφύλλης
# Έκδοση: 6.2

# Βάση δεδομένων για εβδομαδιαίο ωρολόγιο πρόγραμμα ΕΠΑΛ Μεσσήνης, αλλά με δομή και οπτική
# γωνία ανά τμήματος αντί για το συνηθισμένο συνολικό πρόγραμμα, επιτρέπει ανάγνωση/εκχώρηση/τροποποίηση/αποθήκευση.
# -> Εκτεταμένο έλεγχο ορθότητας και συνοχής για την εσωτερική λειτουργία εκχώρησης ονομάτων και των εξωτερικών αρχείων αναφοράς/ευρετηρίου JSON
# -> Χρήση συναρτήσεων για τμηματοποίηση και αρθρωτή δομή
# -> Αριθμητικοί δείκτες μενού επιλογής, και γενικώς η διεπαφή, προσαρμόζονται μετά την πρόσθεση, αφαίρεση ή αλλαγή κατανομής δασκάλων στη βάση δεδομένων
# -> Βεβαίωση και απεικόνιση αλλαγών δεδομένων
# -> Αρχείο καταγραφής συμβάντων με Χρονόσημα
# Από έκδοση 6 και μετά:
# -> Χρήση κενού 'return' σε συναρτήσεις σε συνδυασμό με επιλογή για άμεση και εύκολη αποχώρηση από εμφωλευμένα επαναλαμβανόμενα μενού
# -> Έλεγχος ορθότητας και ακεραιότητας αρχέιων με λίστες JSON, ανίχνευση μη εξουσιοδοτημένης Παραποίησης στοιχείων
# -> καθαρό τερματισμό ακόμα και με σφάλμα και καθαρισμό μνύμης με έξοδο

# Αντιμετώπιση σφαλμάτων στην έκδοση 6 και 6.1:
# -> Μικρές επιδιορθώσεις στις λεπτομέρειες πληροφοριών με την εκτύπωση συμβάντων με χρονόσημα

import json
import datetime
import sys
import traceback

print("EPAL MESSINIS Lesson Schedule Database Program: 1st diagnostic beta test version 1.1")

try:
    event_log_filename='event_log.json'
    with open(event_log_filename,'r') as event_log_file:
        event_log=json.load(event_log_file)
except:
    print("ERROR: Event log file not present, creating new file, 'event_log.json' in the same folder as this script")
    print('\n')
    event_log_list=[]
else:
    print("Event log file 'event_log.json' found and loading to list 'event_log_list'")
    print('\n')
    event_log_list=event_log

try:
    lesson_table_filename='lesson_table.json'
    with open(lesson_table_filename,'r') as lesson_table_file:
        lesson_table=json.load(lesson_table_file)
except:
    print("ERROR: Lesson table/list file not present or corrupted, creating new file, lesson_table.json in the same folder as this script")
    event_log_entry=[]
    event_log_entry.append("Weekly lesson table not found or corrupted and creating default empty table")
    event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
    event_log_list.append(event_log_entry)
    print('\n')
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
    print("Lesson table file 'lesson_table.json' found and loading to list 'class_table'")
    event_log_entry=[]
    event_log_entry.append("Weekly lesson table loading from file")
    event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
    event_log_list.append(event_log_entry)
    print('\n')
    class_table=lesson_table

try:
    teacher_vocation_filename='teacher_vocation.json'
    with open(teacher_vocation_filename,'r') as teacher_vocation_file:
        teacher_vocation=json.load(teacher_vocation_file)
except:
    print("ERROR: Teachers per vocational department list file not present or corrupted, creating new file, teacher_vocation.json in the same folder as this script")
    event_log_entry=[]
    event_log_entry.append("Class sector menu name allocation not found or corrupted, creating default list")
    event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
    event_log_list.append(event_log_entry)
    print('\n')
    teacher_name_list=[
        ["Stavropoulou","Georgikou","Mihalopoulos","Pandosti_general","Efthimiadis","Trikatsoula","Karageorgi","Kapaklis","Maniatis","Kalogeraki","Kalatha","empty"],#Α1
        ["Stavropoulou","Georgikou","Mihalopoulos","Pandosti_general","Efthimiadis","Sakka","Karageorgi","Kapaklis","Maniatis","Kalogeraki","Kalatha","empty"],#Α2
        ["Stavropoulou","Georgikou","Mihalopoulos","Pandosti_general","Pandosti_vocational","Efthimiadis","Maniatis","Dispiraki","Kalogeraki","Spanos","empty"],#Βγ
        ["Stavropoulou","Georgikou","Mihalopoulos","Pandosti_general","Pandosti_vocational","Efthimiadis","Skokos","Karadzoulias","Kapaklis","Spanos","empty"],#Βμ
        ["Stavropoulou","Georgikou","Mihalopoulos","Pandosti_general","Pandosti_vocational","Efthimiadis","Sakka","Trikatsoula","Karageorgi","Spanos","empty"],#Βο
        ["Stavropoulou","Georgikou","Mihalopoulos","Pandosti_general","Efthimiadis","Tserpe","Zevgitis","Kalatha","Dimopoulos","Spanos","empty"],#Βπ
        ["Stavropoulou","Georgikou","Mihalopoulos","Pandosti_general","Efthimiadis","Skokos","Karadzoulias","Kapaklis","Spanos","empty"],#Γαφ
        ["Stavropoulou","Georgikou","Mihalopoulos","Pandosti_general","Efthimiadis","Maniatis","Dispiraki","Kalogeraki","Spanos","empty"],#Γγ
        ["Stavropoulou","Georgikou","Mihalopoulos","Pandosti_general","Efthimiadis","Sakka","Trikatsoula","Karageorgi","Spanos","empty"],#Γο
        ["Stavropoulou","Georgikou","Mihalopoulos","Pandosti_general","Efthimiadis","Tserpe","Zevgitis","Kalatha","Dimopoulos","Spanos","empty"]#Γπ
        ]
else:
    teacher_name_list=teacher_vocation
    print("Checking for the right amount of grade/vocation class sectors(10)...")
    print('\n')
    if len(teacher_name_list)==10:
        print("'teacher_vocation.json' file found and loading to list 'teacher_name_list'")
        event_log_entry=[]
        event_log_entry.append("'teacher_vocation.json' file found and loading to list 'teacher_name_list'")
        event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
        event_log_list.append(event_log_entry)
        print('\n')
    else:
        print("ERROR: 'teacher_vocation.json' file found but the list 'teacher_name_list' is corrupted or tampered with, loading default")
        event_log_entry=[]
        event_log_entry.append("ERROR: 'teacher_vocation.json' file found but the list 'teacher_name_list' is corrupted or tampered with, loading default")
        event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
        event_log_list.append(event_log_entry)
        print('\n')
        teacher_name_list=[
            ["Stavropoulou","Georgikou","Mihalopoulos","Pandosti_general","Efthimiadis","Trikatsoula","Karageorgi","Kapaklis","Maniatis","Kalogeraki","Kalatha","empty"],#Α1
            ["Stavropoulou","Georgikou","Mihalopoulos","Pandosti_general","Efthimiadis","Sakka","Karageorgi","Kapaklis","Maniatis","Kalogeraki","Kalatha","empty"],#Α2
            ["Stavropoulou","Georgikou","Mihalopoulos","Pandosti_general","Pandosti_vocational","Efthimiadis","Maniatis","Dispiraki","Kalogeraki","Spanos","empty"],#Βγ
            ["Stavropoulou","Georgikou","Mihalopoulos","Pandosti_general","Pandosti_vocational","Efthimiadis","Skokos","Karadzoulias","Kapaklis","Spanos","empty"],#Βμ
            ["Stavropoulou","Georgikou","Mihalopoulos","Pandosti_general","Pandosti_vocational","Efthimiadis","Sakka","Trikatsoula","Karageorgi","Spanos","empty"],#Βο
            ["Stavropoulou","Georgikou","Mihalopoulos","Pandosti_general","Efthimiadis","Tserpe","Zevgitis","Kalatha","Dimopoulos","Spanos","empty"],#Βπ
            ["Stavropoulou","Georgikou","Mihalopoulos","Pandosti_general","Efthimiadis","Skokos","Karadzoulias","Kapaklis","Spanos","empty"],#Γαφ
            ["Stavropoulou","Georgikou","Mihalopoulos","Pandosti_general","Efthimiadis","Maniatis","Dispiraki","Kalogeraki","Spanos","empty"],#Γγ
            ["Stavropoulou","Georgikou","Mihalopoulos","Pandosti_general","Efthimiadis","Sakka","Trikatsoula","Karageorgi","Spanos","empty"],#Γο
            ["Stavropoulou","Georgikou","Mihalopoulos","Pandosti_general","Efthimiadis","Tserpe","Zevgitis","Kalatha","Dimopoulos","Spanos","empty"]#Γπ
            ]
try:
    general_studies_filename='general_studies.json'
    with open(general_studies_filename,'r') as general_studies_file:
        general_studies=json.load(general_studies_file)
except:
    print("ERROR: General studies teacher list file not present or corrupted, creating new file, general_studies.json in the same folder as this script")
    event_log_entry=[]
    event_log_entry.append("General studies registry not found or corrupted, creating default list")
    event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
    event_log_list.append(event_log_entry)
    print('\n')
    general_studies_teachers=["Stavropoulou","Georgikou","Mihalopoulos","Pandosti_general","Efthimiadis","Spanos"]
else:
    print("General studies teacher list file 'general_studies.json' found and loading to list 'general_studies_teachers'")
    event_log_entry=[]
    event_log_entry.append("General studies registry file found, loading to list")
    event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
    event_log_list.append(event_log_entry)
    print('\n')
    general_studies_teachers=general_studies

try:
    teachers_complete_filename='teachers_complete.json'
    with open(teachers_complete_filename,'r') as teachers_complete_file:
        teachers_complete=json.load(teachers_complete_file)
except:
    print("ERROR: Complete teachers list file not present or corrupted, creating new file, teachers_complete.json in the same folder as this script")
    event_log_entry=[]
    event_log_entry.append("Complete central name registry file not found or corrupted, creating default list")
    event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
    event_log_list.append(event_log_entry)
    print('\n')
    all_teachers=[
        "Stavropoulou",
        "Georgikou",
        "Mihalopoulos",
        "Pandosti_general",
        "Pandosti_vocational",
        "Efthimiadis",
        "Sakka",
        "Trikatsoula",
        "Karageorgi",
        "Skokos",
        "Karadzoulias",
        "Kapaklis",
        "Maniatis",
        "Dispiraki",
        "Kalogeraki",
        "Tserpe",
        "Zevgitis",
        "Kalatha",
        "Dimopoulos",
        "Spanos",
        "EDIT TEACHER DATABASE",
        "EXIT TO MAIN MENU"
        ]
else:
    all_teachers=teachers_complete
    print("Checking if central teacher registry/menu list contains system options in the right place...")
    print('\n')
    if all_teachers[len(all_teachers)-1]=="EXIT TO MAIN MENU" and all_teachers[len(all_teachers)-2]=="EDIT TEACHER DATABASE":
        print("'teachers_complete.json' found and loading to list 'all_teachers'")
        event_log_entry=[]
        event_log_entry.append("'teachers_complete.json' found and loading to list 'all_teachers'")
        event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
        event_log_list.append(event_log_entry)
        print('\n')
    else:
        print("ERROR: 'teachers_complete.json' file found but 'all_teachers' list is corrupted or tampered with, loading default")
        event_log_entry=[]
        event_log_entry.append("ERROR: File found but'all_teachers' list is corrupted or tampered with, loading default")
        event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
        event_log_list.append(event_log_entry)
        print('\n')
        all_teachers=[
            "Stavropoulou",
            "Georgikou",
            "Mihalopoulos",
            "Pandosti_general",
            "Pandosti_vocational",
            "Efthimiadis",
            "Sakka",
            "Trikatsoula",
            "Karageorgi",
            "Skokos",
            "Karadzoulias",
            "Kapaklis",
            "Maniatis",
            "Dispiraki",
            "Kalogeraki",
            "Tserpe",
            "Zevgitis",
            "Kalatha",
            "Dimopoulos",
            "Spanos",
            "EDIT TEACHER DATABASE",
            "EXIT TO MAIN MENU"
            ]

day_search_list=["Monday","Tuesday","Wednesday","Thursday","Friday"]
day_index_list=[1,2,3,4,5]

hour_search_list=["1st lesson","2nd lesson","3rd lesson","4th lesson","5th lesson","6th lesson","7th lesson"]
hour_index_list=[1,2,3,4,5,6,7]
lesson_time_list=["8:20-9:05","9:10-9:50","10:00-10:40","10:50-11:30","11:40-12:20","12:25-13:05","13:10-13:50"]


taxi_tmima_name_list=["A1","A2","Bg","Bm","Bo","Bp","Gaf","Gg","Go","Gp"]
taxi_tmima_index_list=[1,2,3,4,5,6,7,8,9,10]
menu_range_variable_list=[]
for i in range(10):
    menu_range_variable_list.append(len(teacher_name_list[i]))

option_list=[
    "1 to add name to A1",
    "2 to remove name from A1",
    "3 to add name to A2",
    "4 to remove name from A2",
    "5 to add name to Bg",
    "6 to remove name from Bg",
    "7 to add name to Bm",
    "8 to remove name from Bm",
    "9 to add name to Bo",
    "10 to remove name from Bo",
    "11 to add name to Bp",
    "12 to remove name from Bp",
    "13 to add name to Gaf",
    "14 to remove name from Gaf",
    "15 to add name to Gg",
    "16 to remove name from Gg",
    "17 to add name to Go",
    "18 to remove name from Go",
    "19 to add name to Gp",
    "20 to remove name from Gp",
    "21 to add name to B1",
    "22 to remove name from B1",
    "23 to add name to G1",
    "24 to remove name from G1",
    "25 to completely remove name from the record",
    "26 to add privileged access to BOTH general AND vocational studies",
    "0 to exit"
    ]

print("Running STARTUP data coherence and consistency check to resolve data conflict, or duplicate data if found...")
print('\n')
check_pass=[]
integrity_reference_list=[]
for i in range(10):
    for m in range(5):
        for n in range(7):
            if class_table[i][m][n] not in integrity_reference_list and class_table[i][m][n]!="empty":
                integrity_reference_list.append(class_table[i][m][n])
for i in range(10):
    for m in teacher_name_list[i]:
        if m not in integrity_reference_list and m!="empty":
            integrity_reference_list.append(m)
for i in range(len(all_teachers)-2):
    if all_teachers[i] not in integrity_reference_list:
        integrity_reference_list.append(i)
for i in general_studies_teachers:
    if i not in integrity_reference_list:
        integrity_reference_list.append(i)
for k in integrity_reference_list:
    count_class_table=0
    count_all_teachers=0
    count_general_studies_teachers=0
    count_teacher_name_list=0
    for i in range(10):
        for m in range(5):
            for n in range(7):
                if class_table[i][m][n]==k:
                    count_class_table+=1
    for i in range(10):
        for m in teacher_name_list[i]:
            if m==k:
                count_teacher_name_list+=1
    for i in range(len(all_teachers)-2):
        if all_teachers[i]==k:
            count_all_teachers+=1
    for i in general_studies_teachers:
        if i==k:
            count_general_studies_teachers+=1
    if count_class_table>0 and(count_teacher_name_list==0 or count_all_teachers==0):
        check_pass.append(False)
        print("ERROR: found corrupted data for",k,"in the weekly class table")
        event_log_entry=[]
        x="Data consistency error 'class_table', redundant name",k
        event_log_entry.append(x)
        event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
        event_log_list.append(event_log_entry)
        remove_data=input("Do you want to delete? y for YES, any key for NO:")
        print('\n')
        if remove_data=="y":
            for i in range(10):
                for m in range(5):
                    for n in range(7):
                        if class_table[i][m][n]==k:
                            class_table[i][m][n]="empty"
            print("Deletion CONFIRMED")
            event_log_entry=[]
            event_log_entry.append("Deletion of 'class_table' entries confirmed")
            event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
            event_log_list.append(event_log_entry)
            print('\n')
        else:
            print("Deletion CANCELLED")
            print('\n')
    else:
        check_pass.append(True)
    if count_teacher_name_list>0 and count_all_teachers==0:
        check_pass.append(False)
        print("ERROR: found corrupted data for",k,"in the allocation by grade and class sector registry")
        event_log_entry=[]
        x="Data consistency error in 'teacher_name_list', redundant name",k
        event_log_entry.append(x)
        event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
        event_log_list.append(event_log_entry)
        remove_data=input("Do you want to delete? y for YES, any key for NO:")
        print('\n')
        if remove_data=="y":
            for i in range(10):
                for m in teacher_name_list[i]:
                    if m==k:
                        teacher_name_list[i].remove(k)
            print("Deletion CONFIRMED")
            event_log_entry=[]
            event_log_entry.append("Deletion of 'teacher_name_list' entries confirmed")
            event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
            event_log_list.append(event_log_entry)
            print('\n')
        else:
            print("Deletion CANCELLED")
            print('\n')
    else:
        check_pass.append(True)
    if count_general_studies_teachers>0 and(count_teacher_name_list==0 or count_all_teachers==0):
        check_pass.append(False)
        print("ERROR: found corrupted data for",k,"in B1/G1 general studies teacher registry")
        event_log_entry=[]
        x="Data consisency error in 'general_studies_teachers', redundant name",k
        event_log_entry.append(x)
        event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
        event_log_list.append(event_log_entry)
        remove_data=input("Do you want to delete? y for YES, any key for NO:")
        if remove_data=="y":
            for i in general_studies_teachers:
                if i==k:
                    general_studies_teachers.remove(k)
            print("Deletion CONFIRMED")
            event_log_entry=[]
            event_log_entry.append("Deletion of 'general_studies_teachers' entries confirmed")
            event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
            event_log_list.append(event_log_entry)
            print('\n')
        else:
            print("Deletion CANCELLED")
            print('\n')
    else:
        check_pass.append(True)
for i in all_teachers:
    count_all_teachers=0
    for m in range(10):
        for n in teacher_name_list[m]:
            if n==i and i!="EDIT TEACHER DATABASE" and i!="EXIT TO MAIN MENU":
                count_all_teachers+=1
    if count_all_teachers==0 and i!="EDIT TEACHER DATABASE" and i!="EXIT TO MAIN MENU":
        check_pass.append(False)
        event_log_entry=[]
        x="Data consistency ERROR in 'all_teachers',redundant name",i
        event_log_entry.append(x)
        event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
        event_log_list.append(event_log_entry)
        print("ERROR: Corrupt data in 'all_teachers'redundant name",i)
        if i not in general_studies_teachers:
            print(i,"is not a B1/G1 general studies teacher, if you keep the name, you can still allocate them to a class sector")
        remove_data=input("Do you want to delete? y for YES, any key for NO:")
        print('\n')
        if remove_data=="y":
            all_teachers.remove(i)
            print("Deletion CONFIRMED")
            event_log_entry=[]
            event_log_entry.append("Deletion of 'all_teachers' entries confirmed")
            event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
            event_log_list.append(event_log_entry)
            print('\n')
        else:
            print("Deletion CANCELLED")
            print('\n')
print("Checking for duplicate name entries...")
print('\n')
duplicate_checklist=[]
for i in all_teachers:
    if i!="EDIT TEACHER DATABASE" and i!="EXIT TO MAIN MENU":
        if i not in duplicate_checklist:
            duplicate_checklist.append(i)
        else:
            check_pass.append(False)
            print("Duplicate name ERROR found and DELETED in 'all_teachers':",i)
            all_teachers.remove(i)
            event_log_entry=[]
            x="Duplicate name ERROR found and DELETED  in 'all_teachers':",i
            event_log_entry.append(x)
            event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
            event_log_list.append(event_log_entry)
            print('\n')
duplicate_checklist=[]
for i in general_studies_teachers:
    if i not in duplicate_checklist:
        duplicate_checklist.append(i)
    else:
        check_pass.append(False)
        print("Duplicate name ERROR found and DELETED in 'general_studies_teachers':",i)
        general_studies_teachers.remove(i)
        event_log_entry=[]
        x="Duplicate name ERROR found and DELETED  in 'general_studies_teachers':",i
        event_log_entry.append(x)
        event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
        event_log_list.append(event_log_entry)
        print('\n')
for m in range(10):
    duplicate_checklist=[]
    for i in teacher_name_list[m]:
        if i!="empty":
            if i not in duplicate_checklist:
                duplicate_checklist.append(i)
            else:
                check_pass.append(False)
                print("Duplicate name ERROR found and DELETED in 'teacher_name_list':",i,"in",taxi_tmima_name_list[m])
                teacher_name_list[m].remove(i)
                event_log_entry=[]
                x="Duplicate name ERROR found and DELETED in 'teacher_name_list':",i,"in",taxi_tmima_name_list[m]
                event_log_entry.append(x)
                event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                event_log_list.append(event_log_entry)
                print('\n')
if all(check_pass)==True:
    print("Check successfully PASSED")
    print('\n')
    event_log_entry=[]
    event_log_entry.append("Data coherence and consistency check passed")
    event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
    event_log_list.append(event_log_entry)
print("The event log keeps a maximum of 70 timestamps and deletes oldest timestamps before exit when limit exceeded")
pause_key=input("Do you want to see the timestamped EVENT LOG? y for YES, any key for NO:")
print ('\n')
if pause_key=="y":
    for i in range(len(event_log_list)):
        if i%10==0 and i!=0:
            pause_input=input("Press any key to keep scrolling")
            print('\n')
        print(event_log_list[i][0])
        print(event_log_list[i][1])
        print('\n')
        
def choose_day():
    global day_search,day_index
    repeat=True
    while repeat==True:
        try:
            day=int(input("Choose day, 1 for Monday, 2 for Tuesday, 3 for Wednesday, 4 for Thursday, 5 for Friday:"))
            print('\n')
            while not(type(day)==int and day>=1 and day<=5):
                print("ERROR: Try again")
                day=int(input("Choose day, 1 for Monday, 2 for Tuesday, 3 for Wednesday, 4 for Thursday, 5 for Friday:"))
                print('\n')
        except:
            print("String ERROR: Value must be integer")
            print('\n')
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
            hour=int(input("Choose lesson of the day, 1-7:"))
            print('\n')
            while not(type(hour)==int and hour>=1 and hour<=7):
                print("ERROR: Try again")
                hour=int(input("Choose lesson of the day, 1-7:"))
                print('\n')
        except:
            print("String ERROR: Value must be integer")
            print('\n')
        else:
            for i,n in zip((hour_search_list),(hour_index_list)):
                if n==hour:
                    hour_search,hour_index=i,n-1
            repeat=False

def choose_teacher():
    global teacher,teacher_name,teacher_index,menu_range_variable,menu_range_variable_list,teacher_index_list,teacher_name_list
    repeat=True
    while repeat==True:
        try:
            print("If no teachers are available in this menu or your teacher of choice is not available, choose 0 to exit,")
            print("then choose 'SUB-MENU' from the main menu and then choose 'EDIT TEACHER DATABASE' to add teachers")
            print('\n')
            try:
                for i in range(menu_range_variable):
                    print("choose",teacher_index_list[taxi_tmima_index][i],"for",teacher_name_list[taxi_tmima_index][i])
                print('\n')
            except:
                print("Error synchronizing teacher choice menu index...correcting...")
                print('\n')
                teacher_index_list=[
                    range(1,len(teacher_name_list[0])+1),
                    range(1,len(teacher_name_list[1])+1),
                    range(1,len(teacher_name_list[2])+1),
                    range(1,len(teacher_name_list[3])+1),
                    range(1,len(teacher_name_list[4])+1),
                    range(1,len(teacher_name_list[5])+1),
                    range(1,len(teacher_name_list[6])+1),
                    range(1,len(teacher_name_list[7])+1),
                    range(1,len(teacher_name_list[8])+1),
                    range(1,len(teacher_name_list[9])+1)
                    ]
                menu_range_variable_list=[]
                for i in range(10):
                    menu_range_variable_list.append(len(teacher_name_list[i]))
                for i,m,n in zip((taxi_tmima_name_list),(taxi_tmima_index_list),(menu_range_variable_list)):
                    if m==taxi_tmima_input:
                        taxi_tmima_name,taxi_tmima_index,menu_range_variable=i,m-1,n
                for i in range(menu_range_variable):
                    print("choose",teacher_index_list[taxi_tmima_index][i],"for",teacher_name_list[taxi_tmima_index][i])
                print('\n')
            print("Choose teacher in range from 1-",menu_range_variable,",or",menu_range_variable+1,"to exit:")
            teacher=int(input("=>>"))
            print('\n')
            while not(type(teacher)==int and teacher>=1 and teacher<=menu_range_variable+1):
                print("ERROR: Try again")
                print('\n')
                print("If no teachers are available in this menu or your teacher of choice is not available,")
                print("choose 'SUB-MENU' from the main menu and then choose 'EDIT TEACHER DATABASE' to add teachers")
                print('\n')
                try:
                    for i in range(menu_range_variable):
                        print("choose",teacher_index_list[taxi_tmima_index][i],"for",teacher_name_list[taxi_tmima_index][i])
                    print('\n')
                except:
                    print("Error synchronizing teacher choice menu index...correcting...")
                    print('\n')
                    teacher_index_list=[
                        range(1,len(teacher_name_list[0])+1),
                        range(1,len(teacher_name_list[1])+1),
                        range(1,len(teacher_name_list[2])+1),
                        range(1,len(teacher_name_list[3])+1),
                        range(1,len(teacher_name_list[4])+1),
                        range(1,len(teacher_name_list[5])+1),
                        range(1,len(teacher_name_list[6])+1),
                        range(1,len(teacher_name_list[7])+1),
                        range(1,len(teacher_name_list[8])+1),
                        range(1,len(teacher_name_list[9])+1)
                        ]
                    menu_range_variable_list=[]
                    for i in range(10):
                        menu_range_variable_list.append(len(teacher_name_list[i]))
                    for i,m,n in zip((taxi_tmima_name_list),(taxi_tmima_index_list),(menu_range_variable_list)):
                        if m==taxi_tmima_input:
                            taxi_tmima_name,taxi_tmima_index,menu_range_variable=i,m-1,n
                    for i in range(menu_range_variable):
                        print("choose",teacher_index_list[taxi_tmima_index][i],"for",teacher_name_list[taxi_tmima_index][i])
                    print('\n')
                print("Choose teacher in range from 1-",menu_range_variable,",or",menu_range_variable+1,"to exit:")
                teacher=int(input("=>>"))
                print('\n')
        except:
            print("String ERROR: Value must be integer")
            print('\n')
        else:
            if teacher!=menu_range_variable+1:
                repeat=False
                for i,n in zip((teacher_index_list[taxi_tmima_index]),(teacher_name_list[taxi_tmima_index])):
                    if i==teacher:
                        teacher_index,teacher_name=i,n
            else:
                print("Returning to MAIN MENU")
                print('\n')
                return 
                
def change_data():
    global teacher,teacher_name,teacher_index,menu_range_variable,menu_range_variable_list
    print("Choose the day and lesson time to schedule a teacher and choose teacher name.")
    print("for the grade/vocational department",taxi_tmima_name)
    print('\n')
    choose_teacher()
    if teacher==menu_range_variable+1:
        return 
    choose_day()
    choose_lesson()
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
        print("The teacher",teacher_name,"is already scheduled for",day_search,hour_search,"during the time frame",lesson_time_list[hour_index])
        if teacher_name in general_studies_teachers and other_tmima_index>=2 and other_tmima_index<=5:
            print("with the general studies class for B1. The new lesson booking will delete")
            print("the conflicting old booking for all students in B1")
        elif teacher_name in general_studies_teachers and other_tmima_index>=6 and other_tmima_index<=9:
            print("with the general studies class for G1. The new lesson booking will delete")
            print("the conflicting old booking for all students in G1")
        else:
            print("with the vocational department",taxi_tmima_name_list[other_tmima_index])
            print("The new lesson booking will delete the conflicting old booking with department",taxi_tmima_name_list[other_tmima_index])
    if teacher_name=="empty":
        print("Confirm allocation of lesson gap for",day_search,hour_search,"during the time frame",lesson_time_list[hour_index],"for",taxi_tmima_name)
    else:
        print("Confirm allocation of teacher",teacher_name,"for",day_search,hour_search,"during the time frame",lesson_time_list[hour_index],"for",)
        if teacher_name not in general_studies_teachers:
            print(taxi_tmima_name)
        else:
            if taxi_tmima_index>=2 and taxi_tmima_index<=5:
                print("B1")
            elif taxi_tmima_index>=6 and taxi_tmima_index<=9:
                print("G1")
            else:
                print(taxi_tmima_name)
    confirm=input("y for YES, any key for NO:")
    print('\n')
    if confirm=="y":
        if teacher_name in general_studies_teachers:
            if taxi_tmima_index==0 or taxi_tmima_index==1:
                class_table[taxi_tmima_index][day_index][hour_index]=teacher_name
                event_log_entry=[]
                x=teacher_name,"scheduled in lesson table to",taxi_tmima_name_list[taxi_tmima_index],day_search_list[day_index],hour_search_list[hour_index]
                event_log_entry.append(x)
                event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                event_log_list.append(event_log_entry)
            elif taxi_tmima_index>=2 and taxi_tmima_index<=5:
                print("This booking with",teacher_name,"also applies for students in vocational department")
                for i in range(2,6):
                    class_table[i][day_index][hour_index]=teacher_name
                    event_log_entry=[]
                    if i==taxi_tmima_index:
                        x=teacher_name,"scheduled by user in lesson table to",taxi_tmima_name_list[i],day_search_list[day_index],hour_search_list[hour_index]
                    else:
                        x=teacher_name,"automatically scheduled additionally in lesson table to",taxi_tmima_name_list[i],day_search_list[day_index],hour_search_list[hour_index]
                    event_log_entry.append(x)
                    event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                    event_log_list.append(event_log_entry)
                    if i!=taxi_tmima_index:
                        print(taxi_tmima_name_list[i],)
                print("This is a general class, please check your individual weekly student itinerary")
                print('\n')
            else:
                print("This booking with",teacher_name,"also applies for students in vocational department")
                for i in range(6,10):
                    class_table[i][day_index][hour_index]=teacher_name
                    event_log_entry=[]
                    if i==taxi_tmima_index:
                        x=teacher_name,"scheduled by user in lesson table to",taxi_tmima_name_list[i],day_search_list[day_index],hour_search_list[hour_index]
                    else:
                        x=teacher_name,"automatically scheduled additionally in lesson table to",taxi_tmima_name_list[i],day_search_list[day_index],hour_search_list[hour_index]
                    event_log_entry.append(x)
                    event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                    event_log_list.append(event_log_entry)
                    if i!=taxi_tmima_index:
                        print(taxi_tmima_name_list[i],)
                print("This is a general class, please check your individual weekly student itinerary")
                print('\n')
        else:
            if class_table[taxi_tmima_index][day_index][hour_index] in general_studies_teachers:
                class_table[taxi_tmima_index][day_index][hour_index]=teacher_name
                if taxi_tmima_index>=2 and taxi_tmima_index<=5:
                    print("This is a vocational lesson replacing a general studies lesson. A gap will replace")
                    print("the other grade B1 schedules in the same day and time for vocational departments")
                    for i in range(2,6):
                        if i!=taxi_tmima_index:
                            print(taxi_tmima_name_list[i],)
                            class_table[i][day_index][hour_index]="empty"
                            event_log_entry=[]
                            x="gap allocation in lesson table to",taxi_tmima_name_list[i],day_search_list[day_index],hour_search_list[hour_index]
                            event_log_entry.append(x)
                            event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                            event_log_list.append(event_log_entry)
                elif taxi_tmima_index>=6 and taxi_tmima_index<=9:
                    print("This is a vocational lesson replacing a general studies lesson. A gap will replace")
                    print("the other grade G1 schedules in the same day and time for vocational departments")
                    for i in range(6,10):
                        if i!=taxi_tmima_index:
                            print(taxi_tmima_name_list[i],)
                            class_table[i][day_index][hour_index]="empty"
                            event_log_entry=[]
                            x="gap allocation in lesson table to",taxi_tmima_name_list[i],day_search_list[day_index],hour_search_list[hour_index]
                            event_log_entry.append(x)
                            event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                            event_log_list.append(event_log_entry)
            else:
                class_table[taxi_tmima_index][day_index][hour_index]=teacher_name
                event_log_entry=[]
                x=teacher_name,"scheduled in lesson table to",taxi_tmima_name_list[taxi_tmima_index],day_search_list[day_index],hour_search_list[hour_index]
                event_log_entry.append(x)
                event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                event_log_list.append(event_log_entry)
        if conflict==True:
            if past_teach_booking in general_studies_teachers:
                if other_tmima_index==0 or other_tmima_index==1:
                    class_table[other_tmima_index][day_index][hour_index]="empty"
                    event_log_entry=[]
                    x="gap allocation in lesson table to",taxi_tmima_name_list[other_tmima_index],day_search_list[day_index],hour_search_list[hour_index]
                    event_log_entry.append(x)
                    event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                    event_log_list.append(event_log_entry)
                elif other_tmima_index>=2 and other_tmima_index<=5:
                    if other_tmima_index>=2 and other_tmima_index<=5 and taxi_tmima_index>=2 and taxi_tmima_index<=5:
                        print("ERROR: CONFLICT MISIDENTIFIED: False conflict between",taxi_tmima_name_list[taxi_tmima_index],"and")
                        for i in conflict_list:
                            print(taxi_tmima_name_list[i],)
                        print("all vocational departments in grade B must attend the same general studies lesson for B1")
                        print('\n')
                    else:
                        for i in range(2,6):
                            class_table[i][day_index][hour_index]="empty"
                            event_log_entry=[]
                            x="gap allocation in lesson table to",taxi_tmima_name_list[i],day_search_list[day_index],hour_search_list[hour_index]
                            event_log_entry.append(x)
                            event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                            event_log_list.append(event_log_entry)
                else:
                    if other_tmima_index>=6 and other_tmima_index<=9 and taxi_tmima_index>=6 and taxi_tmima_index<=9:
                        print("ERROR: CONFLICT MISIDENTIFIED: False conflict between",taxi_tmima_name_list[taxi_tmima_index],"and")
                        for i in conflict_list:
                            print(taxi_tmima_name_list[i],)
                        print("all vocational departments in grade G must attend the same general studies lesson for G1")
                        print('\n')
                    else:
                        for i in range(6,10):
                            class_table[i][day_index][hour_index]="empty"
                            event_log_entry=[]
                            x="gap allocation in lesson table to",taxi_tmima_name_list[i],day_search_list[day_index],hour_search_list[hour_index]
                            event_log_entry.append(x)
                            event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                            event_log_list.append(event_log_entry)
            else:
                class_table[other_tmima_index][day_index][hour_index]="empty"
            conflict=False
        print("Allocation confirmed")
        print('\n')
    else:
        print("Teacher allocation CANCELLED")
        print('\n')
    
def read_data():
    print("Choose the day and time of lesson to show teacher scheduled for that lesson.")
    print("for the grade/vocational department",taxi_tmima_name)
    print('\n')
    choose_day()
    choose_lesson()
    if class_table[taxi_tmima_index][day_index][hour_index]!="empty":
        print("The teacher",class_table[taxi_tmima_index][day_index][hour_index],"is scheduled for",day_search,hour_search,"during the time frame",lesson_time_list[hour_index])
    else:
        print("There is a lesson gap scheduled for",day_search,hour_search,"during the time frame",lesson_time_list[hour_index])
    print('\n')

def read_day():
    print("Choose a school day to show class schedule for that day.")
    print("for the grade/vocational department",taxi_tmima_name)
    print('\n')
    choose_day()
    print("schedule for",day_search)
    print('\n')
    for i in range(7):
        print(hour_search_list[i],lesson_time_list[i],'\t','\t',class_table[taxi_tmima_index][day_index][i])
        print('\n')

def read_teacher():
    global teacher
    print("Choose a teacher to show all days and times that are scheduled for that teacher for the whole week.")
    print("for the grade/vocational department",taxi_tmima_name)
    print('\n')
    choose_teacher()
    if teacher==menu_range_variable+1:
        return 
    teacher_week_day=[]
    teacher_week_lesson=[]
    for i in range(5):
        for n in range(7):
            if teacher_name==class_table[taxi_tmima_index][i][n]:
                teacher_week_day.append(i)
                teacher_week_lesson.append(n)
    if len(teacher_week_day)>0 and teacher_index==menu_range_variable:
        for i in range(len(teacher_week_day)):
            print("There is a gap with no teacher on",day_search_list[teacher_week_day[i]],"during the",hour_search_list[teacher_week_lesson[i]])
            print("for the grade and vocational department of",taxi_tmima_name)
            print('\n')
    elif len(teacher_week_day)>0 and teacher_index!=menu_range_variable:
        for i in range(len(teacher_week_day)):
            print("The teacher",teacher_name,"is scheduled for",day_search_list[teacher_week_day[i]],"for the",hour_search_list[teacher_week_lesson[i]])
            if teacher_name not in general_studies_teachers:
                print("for the grade and vocational department of",taxi_tmima_name)
                print('\n')
            else:
                if taxi_tmima_index>=2 and taxi_tmima_index<=5:
                    print("for the grade and vocational department of B1")
                    print('\n')
                elif taxi_tmima_index>=6 and taxi_tmima_index<=9:
                    print("for the grade and vocational department of G1")
                    print('\n')
    elif len(teacher_week_day)==0 and teacher_index==menu_range_variable:
        print("There are no gaps with missing teachers in the schedule for the whole weeks")
        print("for the grade and vocational department of",taxi_tmima_name)
        print('\n')
    elif len(teacher_week_day)==0 and teacher_index!=menu_range_variable:
        print("The teacher",teacher_name,"is not available for lessons this week or has not been scheduled yet for this week")
        if teacher_name not in general_studies_teachers:
            print("for the grade and vocational department of",taxi_tmima_name)
            print('\n')
        else:
            if taxi_tmima_index>=2 and taxi_tmima_index<=5:
                print("for the grade and vocational department of B1")
                print('\n')
            elif taxi_tmima_index>=6 and taxi_tmima_index<=9:
                print("for the grade and vocational department of G1")
                print('\n')
    print('\n')

def taxi_tmima_menu():
    global teacher,taxi_tmima_name,taxi_tmima_index,menu_range_variable,taxi_tmima_index_list,menu_range_variable_list
    repeat=True
    while repeat==True:
        try:
            print("For grade/vocational department",taxi_tmima_name)
            menu=int(input("1: Change one lesson, 2: View one lesson, 3: View schedule for one day, 4: View weekly schedule for one teacher, 0 to return to main menu>"))
            print('\n')
            while not(type(menu)==int and menu>=0 and menu<=4):
                print("ERROR: Try again")
                print("For grade/vocational department",taxi_tmima_name)
                menu=int(input("1: Change one lesson, 2: View one lesson, 3: View schedule for one day, 4: View weekly schedule for one teacher, 0 to return to main menu>"))
            print('\n')
        except:
            print("String ERROR: Value must be integer")
            print('\n')
        else:
            if menu==1:
                change_data()
                if teacher==menu_range_variable+1:
                    return 
            elif menu==2:
                read_data()
            elif menu==3:
                read_day()
            elif menu==4:
                read_teacher()
                if teacher==menu_range_variable+1:
                    return 
            else:
                repeat=False
                if taxi_tmima_index>=2 and taxi_tmima_index<=9:
                    print("Weekly individual student itinerary, general and vocational lessons for",taxi_tmima_name)
                    print('\n')
                else:
                    print("Weekly individual student itinerary, general lessons for",taxi_tmima_name)
                    print('\n')
                for i in range(5):
                    taxi_tmima_weekly_table=list(range(7))
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
                    print(day_search_list[i],'\t','\t',taxi_tmima_weekly_table)
                    print('\n')
                print("Returning to main menu.")
                print('\n')

def name():
    global name_allocation
    name_repeat=True
    while name_repeat==True:
        try:
            name_allocation=input("Type in surname of teacher:")
            print('\n')
            while "EDIT" in name_allocation or "EXIT" in name_allocation or "DATABASE" in name_allocation or name_allocation.replace('_','',1).isalpha()==False or name_allocation[0].isupper()==False:
                print("ERROR: Try again")
                print('\n')
                if name_allocation[0].isupper()==False:
                    print("ERROR: Name must start with a capital letter")
                if name_allocation.isalpha()==False:
                    print("ERROR: Name must not contain numbers or special characters, but allows for '_general' or' _vocational'")
                if "EDIT" in name_allocation or "EXIT" in name_allocation or "DATABASE" in name_allocation:
                    print("ERROR: Name must not contain system commands")
                name_allocation=input("Type in surname of teacher:")
                print('\n')
        except:
            print("Empty string ERROR: Try again")
            print('\n')
        else:
            name_repeat=False
            
def global_delete():
    global teacher_index_list,menu_range_variable_list
    duplicate_1=0
    for i in all_teachers:
        if i==name_allocation:
            duplicate_1+=1
            all_teachers.remove(i)
    if duplicate_1>1:
        print("ERROR: Name duplication for",name_allocation,"found and removed in central teacher registry")
        event_log_entry=[]
        x="ERROR: Name duplication for",name_allocation,"and removed"
        event_log_entry.append(x)
        event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
        event_log_list.append(event_log_entry)
        print('\n')
    duplicate_2=0
    for i in general_studies_teachers:
        if i==name_allocation:
            duplicate_2+=1
            general_studies_teachers.remove(i)
    if duplicate_2>1:
        print("ERROR: Name duplication for",name_allocation,"found and removed in general studies B1/G1 registry")
        event_log_entry=[]
        x="ERROR: Name duplication for",name_allocation,"and removed"
        event_log_entry.append(x)
        event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
        event_log_list.append(event_log_entry)
        print('\n')
    print("B1/G1 general studies registry",'\t',general_studies_teachers)
    print('\n')
    for i in range(10):
        duplicate_3=0
        for n in teacher_name_list[i]:
            if n==name_allocation:
                duplicate_3+=1
                teacher_name_list[i].remove(n)
                print(name_allocation,"removed from",taxi_tmima_name_list[i])
        if duplicate_3>1:
            print("ERROR: Name duplication for",name_allocation,"found and removed in name assignment choice menu for class sector",taxi_tmima_name_list[i])
            event_log_entry=[]
            x="ERROR: Name duplication for",name_allocation,"and removed"
            event_log_entry.append(x)
            event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
            event_log_list.append(event_log_entry)
            print('\n')
    for i in range(10):
        print(taxi_tmima_name_list[i],'\t',teacher_name_list[i])
    print('\n')
    for i in range(10):
        for m in range(5):
            for n in range(7):
                if class_table[i][m][n]==name_allocation:
                    class_table[i][m][n]="empty"
                    print(name_allocation,"found in",taxi_tmima_name_list[i],day_search_list[m],hour_search_list[n],", removed and allocated 'empty'")
    print('\n')
    print("Complete deletion CONFIRMED")
    print('\n')

def integrity_check():
    global integrity_checklist
    integrity_checklist=[]
    if name_allocation in general_studies_teachers:
        integrity_checklist.append(False)
    else:
        integrity_checklist.append(True)
    for i in range(10):
        if name_allocation in teacher_name_list[i]:
            integrity_checklist.append(False)
        else:
            integrity_checklist.append(True)
        for m in range(5):
            for n in range(7):
                if class_table[i][m][n]==name_allocation:
                    integrity_checklist.append(False)
                else:
                    integrity_checklist.append(True)

def edit_option_1_20_odd():
    global edit_option_end,edit_option
    edit_option_end=True
    name()
    if name_allocation not in all_teachers:
        if name_allocation not in teacher_name_list[(edit_option-1)//2]:
            print("Confirm allocation of",name_allocation,"to",taxi_tmima_name_list[(edit_option-1)//2],"? y for YES, any key for NO:")
            confirm2=input("=>")
            print('\n')
            if confirm2=="y":
                integrity_check()
                if all(integrity_checklist)==True:
                    all_teachers.insert(0,name_allocation)
                    teacher_name_list[(edit_option-1)//2].insert(0,name_allocation)
                    event_log_entry=[]
                    x=name_allocation,"added to 'all_teachers' and 'teacher_name_list' at",taxi_tmima_name_list[(edit_option-1)//2]
                    event_log_entry.append(x)
                    event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                    event_log_list.append(event_log_entry)
                    print("Allocation CONFIRMED")
                    print('\n')
                    for i in range(10):
                        print(taxi_tmima_name_list[i],'\t',teacher_name_list[i])
                    print('\n')
                else:
                    print("ERROR: Data consistency and integrity check FAILED, conflict between multiple lists")
                    print("Choose option 25 to completely remove",name_allocation,"and then reassign")
                    confirm_delete=input("Do you want to remove now? y for YES, any key for NO:")
                    print('\n')
                    if confirm_delete=="y":
                        global_delete()
                        event_log_entry=[]
                        x=name_allocation,"deleted from everywhere, integrity check failed"
                        event_log_entry.append(x)
                        event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                        event_log_list.append(event_log_entry)
                    else:
                        print("Deletion CANCELLED")
                        print('\n')
            else:
                print("Allocation CANCELLED")
                print ('\n')
        else:
            print("ERROR: The teacher",name_allocation,"is assigned to class sector",taxi_tmima_name_list[(edit_option-1)//2],"without being")
            print("registered to this school, or data corrupted, choose option 25 to remove completely, then reassign")
            confirm_delete=input("Do you want to remove now? y for YES, any key for NO:")
            print('\n')
            if confirm_delete=="y":
                global_delete()
                event_log_entry=[]
                x=name_allocation,"deleted from everywhere, corrupted data"
                event_log_entry.append(x)
                event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                event_log_list.append(event_log_entry)
            else:
                print("Deletion CANCELLED")
                print('\n')
    else:
        if name_allocation not in teacher_name_list[(edit_option-1)//2]:
            print("The teacher",name_allocation,"is already registered to this school, but not assigned to class sector",taxi_tmima_name_list[(edit_option-1)//2])
            print("Do you want to assign",name_allocation,"to an additional class sector or transfer from one to the other?")
            confirm1=input("1 for additonal assignment, 2 for transfer of assignment:")
            print('\n')
            while confirm1!="1" and confirm1!="2":
                print("ERROR: Try again")
                print('\n')
                confirm1=input("1 for additonal assignment, 2 for transfer of assignment:")
                print('\n')
            if confirm1=="1" or confirm1=="2":
                print("Confirm allocation of",name_allocation,"to",taxi_tmima_name_list[(edit_option-1)//2],"? y for YES, any key for NO:")
                confirm2=input("=>")
                print('\n')
                if confirm2=="y":
                    confirm_or_cancel=True
                    if edit_option==1 or edit_option==3:
                        teacher_name_list[(edit_option-1)//2].insert(0,name_allocation)
                        event_log_entry=[]
                        x=name_allocation,"added to 'teacher_name_list' at",taxi_tmima_name_list[(edit_option-1)//2]
                        event_log_entry.append(x)
                        event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                        event_log_list.append(event_log_entry)
                        print("Allocation CONFIRMED")
                        print('\n')
                        for i in range(10):
                            print(taxi_tmima_name_list[i],'\t',teacher_name_list[i])
                        print('\n')
                    elif edit_option>=5 and edit_option<=20:
                        if name_allocation not in general_studies_teachers:
                            teacher_name_list[(edit_option-1)//2].insert(0,name_allocation)
                            event_log_entry=[]
                            x=name_allocation,"added to 'teacher_name_list' at",taxi_tmima_name_list[(edit_option-1)//2]
                            event_log_entry.append(x)
                            event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                            event_log_list.append(event_log_entry)
                            print("Allocation CONFIRMED")
                            print('\n')
                            for i in range(10):
                                print(taxi_tmima_name_list[i],'\t',teacher_name_list[i])
                            print('\n')
                        else:
                            print("ERROR: Allocation halted,",name_allocation,"is not in this class sector but listed for general studies")
                            print('\n')
                else:
                    confirm_or_cancel=False
                    print("Allocation CANCELLED")
                    print('\n')
            if confirm1=="2" and confirm_or_cancel==True:
                print("Confirm transfer of",name_allocation,"to",taxi_tmima_name_list[(edit_option-1)//2],"and delete past allocations? y for YES, any key for NO:")
                confirm2=input("=>")
                print('\n')
                if confirm2=="y":
                    if name_allocation not in general_studies_teachers:
                        for i in range(10):
                            duplicate=0
                            for n in teacher_name_list[i]:
                                if n==name_allocation and i!=(edit_option-1)//2:
                                    duplicate+=1
                                    teacher_name_list[i].remove(n)
                                    event_log_entry=[]
                                    x=name_allocation,"removed from",taxi_tmima_name_list[i],"'teacher_name_list'"
                                    event_log_entry.append(x)
                                    event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                                    event_log_list.append(event_log_entry)
                                    print(name_allocation,"removed from",taxi_tmima_name_list[i],"before transfer")
                            if duplicate>1:
                                print("ERROR: Name duplication found and removed in class sector",taxi_tmima_name_list[i])
                            for m in range(5):
                                for n in range(7):
                                    if class_table[i][m][n]==name_allocation and i!=(edit_option-1)//2:
                                        class_table[i][m][n]="empty"
                                        event_log_entry=[]
                                        x=name_allocation,"removed from",taxi_tmima_name_list[i],day_search_list[m],hour_search_list[n],"in 'class_table'"
                                        event_log_entry.append(x)
                                        event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                                        event_log_list.append(event_log_entry)
                                        print(taxi_tmima_name_list[i],day_search_list[m],hour_search_list[n],"allocated empty before transfer")
                                        print('\n')
                        event_log_entry=[]
                        x=name_allocation,"added to",taxi_tmima_name_list[(edit_option-1)//2],"in 'teacher_name_list'"
                        event_log_entry.append(x)
                        event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                        event_log_list.append(event_log_entry)
                        print("Transfer CONFIRMED")
                        print('\n')
                        for i in range(10):
                            print(taxi_tmima_name_list[i],'\t',teacher_name_list[i])
                        print('\n')
                    else:
                        if (edit_option-1)//2==0 or (edit_option-1)//2==1:
                            print("ERROR: Transfer halted,",)
                            print("choose <1> allocate instead of <2> transfer to assign",name_allocation,"to",taxi_tmima_name_list[(edit_option-1)//2])
                            print("while preserving general studies classes in B1 or G1")
                            print('\n')
                        else:
                            print("ERROR: Transfer halted,",name_allocation,"is not in this class sector",taxi_tmima_name_list[(edit_option-1)//2],"but listed for general studies")
                            print('\n')
                else:
                    print("Transfer CANCELLED")
                    print('\n')
        else:
            print("ERROR:",name_allocation,"already registered with the school and assigned to class sector",taxi_tmima_name_list[(edit_option-1)//2])
            print('\n')
    edit_option=-1

def edit_option_1_20_even():
    global edit_option_end,edit_option
    edit_option_end=True
    name()
    if name_allocation in all_teachers:
        if name_allocation in teacher_name_list[edit_option//2-1]:
            if edit_option==2 or edit_option==4:
                print("Confirm removal of",name_allocation,"from",taxi_tmima_name_list[edit_option/2-1],"? y for YES, any key for NO:")
                confirm2=input("=>")
                print('\n')
                if confirm2=="y":
                    duplicate=0
                    for n in teacher_name_list[edit_option//2-1]:
                        if n==name_allocation:
                            duplicate+=1
                            teacher_name_list[edit_option//2-1].remove(n)
                            event_log_entry=[]
                            x=name_allocation,"removed from",taxi_tmima_name_list[edit_option//2-1],"in 'teacher_name_list'"
                            event_log_entry.append(x)
                            event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                            event_log_list.append(event_log_entry)
                    if duplicate>1:
                        print("ERROR: Name duplication found and removed in class sector",taxi_tmima_name_list[i])
                    for m in range(5):
                        for n in range(7):
                            if class_table[edit_option//2-1][m][n]==name_allocation:
                                class_table[edit_option//2-1][m][n]="empty"
                                event_log_entry=[]
                                x=name_allocation,"removed from",taxi_tmima_name_list[edit_option//2-1],day_search_list[m],hour_search_list[n],"in 'class_table'"
                                event_log_entry.append(x)
                                event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                                event_log_list.append(event_log_entry)
                                print(taxi_tmima_name_list[edit_option//2-1],day_search_list[m],hour_search_list[n],"allocated empty")
                    print("Removal CONFIRMED")
                    print('\n')
                    if name_allocation in general_studies_teachers:
                        general_count=0
                        for i in range(10):
                            if name_allocation in teacher_name_list[i]:
                                general_count+=1
                        if general_count==0:
                            print(name_allocation,"is a general studies teacher with no other allocation in any class sector and will be completely removed")
                            print('\n')
                            global_delete()
                            event_log_entry=[]
                            x=name_allocation,"deleted from everywhere, redundant general studies teacher with no A1,A2,B1 or G1 allocation"
                            event_log_entry.append(x)
                            event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                            event_log_list.append(event_log_entry)
                        else:
                            for i in range(10):
                                print(taxi_tmima_name_list[i],'\t',teacher_name_list[i])
                            print('\n')
                    else:
                        for i in range(10):
                            print(taxi_tmima_name_list[i],'\t',teacher_name_list[i])
                        print('\n')
                else:
                    print("Removal CANCELLED")
                    print('\n')
            elif edit_option>=5 and edit_option<=20:
                if name_allocation not in general_studies_teachers:
                    print("Confirm removal of",name_allocation,"from",taxi_tmima_name_list[edit_option//2-1],"? y for YES, any key for NO:")
                    confirm2=input("=>")
                    print('\n')
                    if confirm2=="y":
                        duplicate=0
                        for n in teacher_name_list[edit_option//2-1]:
                            if n==name_allocation:
                                duplicate+=1
                                teacher_name_list[edit_option//2-1].remove(n)
                                event_log_entry=[]
                                x=name_allocation,"removed from",taxi_tmima_name_list[edit_option//2-1],"in 'teacher_name_list'"
                                event_log_entry.append(x)
                                event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                                event_log_list.append(event_log_entry)
                        if duplicate>1:
                            print("ERROR: Name duplication found and removed in class sector",taxi_tmima_name_list[i])
                        for m in range(5):
                            for n in range(7):
                                if class_table[edit_option//2-1][m][n]==name_allocation:
                                    class_table[edit_option//2-1][m][n]="empty"
                                    event_log_entry=[]
                                    x=name_allocation,"removed from",taxi_tmima_name_list[edit_option//2-1],day_search_list[m],hour_search_list[n],"in 'class_table'"
                                    event_log_entry.append(x)
                                    event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                                    event_log_list.append(event_log_entry)
                                    print(taxi_tmima_name_list[edit_option//2-1],day_search_list[m],hour_search_list[n],"allocated empty")
                        print("Removal CONFIRMED")
                        print('\n')
                        for i in range(10):
                            print(taxi_tmima_name_list[i],'\t',teacher_name_list[i])
                        print('\n')
                    else:
                        print("Removal CANCELLED")
                        print('\n')
                else:
                    print("ERROR:",name_allocation,"is listed in this class sector but as a general studies teacher for grade",end=" ")
                    if edit_option//2-1>=2 and edit_option//2-1<=5:
                        print("B1, choose option 22",end=" ")
                    elif edit_option//2-1>=6 and edit_option//2-1<=9:
                        print("G1, choose option 24",end=" ")
                    print("to remove")
                    print('\n')
        else:
            print("The teacher",name_allocation,"is registered at the school but not in the class sector",taxi_tmima_name_list[edit_option//2-1])
            print("Choose option",end=" ")
            print_count=0
            for i in range(10):
                if name_allocation in teacher_name_list[i]:
                    if i==0 or i==1:
                        print((i+1)*2,end=" ")
                    elif i>=2 and i<=5:
                        if name_allocation not in general_studies_teachers:
                            print((i+1)*2,end=" ")
                        else:
                            print_count+=1
                            if print_count==1:
                                print("22",end=" ")
                    elif i>=6 and i<=9:
                        if name_allocation not in general_studies_teachers:
                            print((i+1)*2,end=" ")
                        else:
                            print_count+=1
                            if print_count==1:
                                print("24",end=" ")
            print("to remove")
            print('\n')
    else:
        print("ERROR: Cannot remove",name_allocation,"from",teacher_name_list[edit_option//2-1],"this teacher is not registered with the school")
        print('\n')
    edit_option=-1

def edit_option_21_23():
    global edit_option_end,edit_option
    edit_option_end=True
    name()
    if name_allocation not in all_teachers:
        integrity_check()
        if all(integrity_checklist)==True:
            if edit_option==21:
                print("Confirm allocation of",name_allocation,"to B1? y for YES, any key for NO:")
                confirm2=input("=>")
                print('\n')
                if confirm2=="y":
                    all_teachers.insert(0,name_allocation)
                    general_studies_teachers.insert(0,name_allocation)
                    event_log_entry=[]
                    x=name_allocation,"added to 'all_teachers' and 'general_studies_teachers'"
                    event_log_entry.append(x)
                    event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                    event_log_list.append(event_log_entry)
                    for i in range(2,6):
                        teacher_name_list[i].insert(0,name_allocation)
                        event_log_entry=[]
                        x=name_allocation,"added to",taxi_tmima_name_list[i],"in 'teacher_name_list' as a B1 general studies teacher"
                        event_log_entry.append(x)
                        event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                        event_log_list.append(event_log_entry)
                    print("Registration to school and assignment to B1 CONFIRMED")
                    print('\n')
                    for i in range(10):
                        print(taxi_tmima_name_list[i],'\t',teacher_name_list[i])
                    print('\n')
                    print("B1/G1 general studies registry",'\t',general_studies_teachers)
                    print('\n')
                else:
                    print("Registration to school and assignment to B1 CANCELLED")
                    print('\n')
            else:
                print("Confirm allocation of",name_allocation,"to G1? y for YES, any key for NO:")
                confirm2=input("=>")
                print('\n')
                if confirm2=="y":
                    all_teachers.insert(0,name_allocation)
                    general_studies_teachers.insert(0,name_allocation)
                    event_log_entry=[]
                    x=name_allocation,"added to 'all_teachers' and 'general_studies_teachers'"
                    event_log_entry.append(x)
                    event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                    event_log_list.append(event_log_entry)
                    for i in range(6,10):
                        teacher_name_list[i].insert(0,name_allocation)
                        event_log_entry=[]
                        x=name_allocation,"added to",taxi_tmima_name_list[i],"in 'teacher_name_list' as a G1 general studies teacher"
                        event_log_entry.append(x)
                        event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                        event_log_list.append(event_log_entry)
                    print("Registration to school and assignment to G1 CONFIRMED")
                    print('\n')
                    for i in range(10):
                        print(taxi_tmima_name_list[i],'\t',teacher_name_list[i])
                    print('\n')
                    print("B1/G1 general studies registry",'\t',general_studies_teachers)
                    print('\n')
                else:
                    print("Registration to school and assignment G1 CANCELLED")
                    print('\n')
        else:
            print("ERROR: Data consistency and integrity check FAILED, conflict between multiple lists")
            print("Choose option 25 to completely remove",name_allocation,"and then reassign")
            confirm_delete=input("Do you want to remove now? y for YES, any key for NO:")
            print('\n')
            if confirm_delete=="y":
                global_delete()
                event_log_entry=[]
                x=name_allocation,"deleted from everywhere, integrity check failed"
                event_log_entry.append(x)
                event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                event_log_list.append(event_log_entry)
            else:
                print("Deletion CANCELLED")
                print('\n')
    else:
        if name_allocation in general_studies_teachers:
            b1=0
            for i in range(2,6):
                if name_allocation in teacher_name_list[i]:
                    b1+=1
            g1=0
            for i in range(6,10):
                if name_allocation in teacher_name_list[i]:
                    g1+=1
            if b1==4 and g1==0:
                if edit_option==23:
                    print("Confirm allocation of",name_allocation,"to G1? y for YES, any key for NO:")
                    confirm2=input("=>")
                    print('\n')
                    if confirm2=="y":
                        for i in range(6,10):
                            teacher_name_list[i].insert(0,name_allocation)
                            event_log_entry=[]
                            x=name_allocation,"added to",taxi_tmima_name_list[i],"in 'teacher_name_list' as a G1 general studies teacher"
                            event_log_entry.append(x)
                            event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                            event_log_list.append(event_log_entry)
                        print("Allocation to G1 CONFIRMED")
                        print('\n')
                        for i in range(10):
                            print(taxi_tmima_name_list[i],'\t',teacher_name_list[i])
                        print('\n')
                        print("B1/G1 general studies registry",'\t',general_studies_teachers)
                        print('\n')
                        print("Do you want to make this a transfer and reassignment from B1 to G1 by deleting",name_allocation,"from all B1 assignments?")
                        confirm2=input("y for YES, any key for NO:")
                        print('\n')
                        if confirm2=="y":
                            for i in range(2,6):
                                duplicate=0
                                for n in teacher_name_list[i]:
                                    if n==name_allocation:
                                        duplicate+=1
                                        teacher_name_list[i].remove(n)
                                        event_log_entry=[]
                                        x=name_allocation,"removed from",taxi_tmima_name_list[i],"in 'teacher_name_list' as a B1 general studies teacher"
                                        event_log_entry.append(x)
                                        event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                                        event_log_list.append(event_log_entry)
                                        print(name_allocation,"removed from",taxi_tmima_name_list[i],"before transfer")
                                if duplicate>1:
                                    print("ERROR: Name duplication found and removed in class sector",taxi_tmima_name_list[i])
                            for i in range(2,6):
                                for m in range(5):
                                    for n in range(7):
                                        if class_table[i][m][n]==name_allocation:
                                            class_table[i][m][n]="empty"
                                            event_log_entry=[]
                                            x=name_allocation,"removed from",taxi_tmima_name_list[i],day_search_list[m],hour_search_list[n],"in 'class_table'"
                                            event_log_entry.append(x)
                                            event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                                            event_log_list.append(event_log_entry)
                            print("Deletion and reassignment CONFIRMED")
                            print('\n')
                            for i in range(10):
                                print(taxi_tmima_name_list[i],'\t',teacher_name_list[i])
                            print('\n')
                        else:
                            print("Deletion of past assignments to B1 CANCELLED")
                            print('\n')
                    else:
                        print("Assignment to G1 CANCELLED")
                        print('\n')                         
                else:
                    print("ERROR:",name_allocation,"already assigned to B1 as a general studies teacher")
                    print("choose option 23 to assign the general studies teacher to G1 as well")
                    print('\n')
            elif b1==0 and g1==4:
                if edit_option==21:
                    print("Confirm allocation of",name_allocation,"to B1? y for YES, any key for NO:")
                    confirm2=input("=>")
                    print('\n')
                    if confirm2=="y":
                        for i in range(2,6):
                            teacher_name_list[i].insert(0,name_allocation)
                            event_log_entry=[]
                            x=name_allocation,"added to",taxi_tmima_name_list[i],"in 'teacher_name_list' as a B1 general studies teacher"
                            event_log_entry.append(x)
                            event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                            event_log_list.append(event_log_entry)
                        for i in range(10):
                            print(taxi_tmima_name_list[i],'\t',teacher_name_list[i])
                        print('\n')
                        print("B1/G1 general studies registry",'\t',general_studies_teachers)
                        print('\n')
                        print("Allocation to B1 CONFIRMED")
                        print('\n')
                        print("Do you want to make this a transfer and reassignment from G1 to B1 by deleting",name_allocation,"from all G1 assignments?")
                        confirm2=input("y for YES, any key for NO:")
                        print('\n')
                        if confirm2=="y":
                            for i in range(6,10):
                                duplicate=0
                                for n in teacher_name_list[i]:
                                    if n==name_allocation:
                                        duplicate+=1
                                        teacher_name_list[i].remove(n)
                                        event_log_entry=[]
                                        x=name_allocation,"removed from",taxi_tmima_name_list[i],"in 'teacher_name_list' as a G1 general studies teacher"
                                        event_log_entry.append(x)
                                        event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                                        event_log_list.append(event_log_entry)
                                        print(name_allocation,"removed from",taxi_tmima_name_list[i],"before transfer")
                                if duplicate>1:
                                    print("ERROR: Name duplication found and removed in class sector",taxi_tmima_name_list[i])
                            for i in range(6,10):
                                for m in range(5):
                                    for n in range(7):
                                        if class_table[i][m][n]==name_allocation:
                                            class_table[i][m][n]="empty"
                                            event_log_entry=[]
                                            x=name_allocation,"removed from",taxi_tmima_name_list[i],day_search_list[m],hour_search_list[n],"in 'class_table'"
                                            event_log_entry.append(x)
                                            event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                                            event_log_list.append(event_log_entry)
                            print("Deletion and reassignment CONFIRMED")
                            print('\n')
                            for i in range(10):
                                print(taxi_tmima_name_list[i],'\t',teacher_name_list[i])
                            print('\n')
                        else:
                            print("Deletion of past assignments to G1 CANCELLED")
                            print('\n')
                    else:
                        print("Assignment to B1 CANCELLED")
                        print('\n')                           
                else:
                    print("ERROR:",name_allocation,"already assigned to G1 as a general studies teacher")
                    print("choose option 21 to assign the general studies teacher to B1 as well")
                    print('\n')
            elif b1==4 and g1==4:
                print("ERROR:",name_allocation," already assigned to B1 AND G2 as a general studies teacher")
                print('\n')
            elif b1==0 and g1==0 and(name_allocation in teacher_name_list[0] or name_allocation in teacher_name_list[1]):
                print("NOTE: A general studies teacher without B1/G1 allocation can reserve the right for new B1/G1 assignments")
                print("is they maintain at least 1 allocation in A1 or A2")
                if edit_option==23:
                    print("Confirm allocation of",name_allocation,"to G1? y for YES, any key for NO:")
                    confirm2=input("=>")
                    print('\n')
                    if confirm2=="y":
                        for i in range(6,10):
                            teacher_name_list[i].insert(0,name_allocation)
                            event_log_entry=[]
                            x=name_allocation,"added to",taxi_tmima_name_list[i],"in 'teacher_name_list' as a G1 general studies teacher"
                            event_log_entry.append(x)
                            event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                            event_log_list.append(event_log_entry)
                        print("Allocation to G1 CONFIRMED")
                        print('\n')
                        for i in range(10):
                            print(taxi_tmima_name_list[i],'\t',teacher_name_list[i])
                        print('\n')
                        print("B1/G1 general studies registry",'\t',general_studies_teachers)
                        print('\n')
                    else:
                        print("Assignment to G1 CANCELLED")
                        print('\n') 
                else:
                    print("Confirm allocation of",name_allocation,"to B1? y for YES, any key for NO:")
                    confirm2=input("=>")
                    print('\n')
                    if confirm2=="y":
                        for i in range(2,6):
                            teacher_name_list[i].insert(0,name_allocation)
                            event_log_entry=[]
                            x=name_allocation,"added to",taxi_tmima_name_list[i],"in 'teacher_name_list' as a B1 general studies teacher"
                            event_log_entry.append(x)
                            event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                            event_log_list.append(event_log_entry)
                        for i in range(10):
                            print(taxi_tmima_name_list[i],'\t',teacher_name_list[i])
                        print('\n')
                        print("B1/G1 general studies registry",'\t',general_studies_teachers)
                        print('\n')
                        print("Allocation to B1 CONFIRMED")
                        print('\n')
                    else:
                        print("Assignment to B1 CANCELLED")
                        print('\n' ) 
            else:
                print("ERROR: The teacher",name_allocation,"has been allocated incorrectly for general studies or data corrupted,")
                print("choose option 25 to remove teacher completely from the record and then reregister and then reassign")
                confirm_delete=input("Do you want to remove now? y for YES, any key for NO:")
                print('\n')
                if confirm_delete=="y":
                    global_delete()
                    event_log_entry=[]
                    x=name_allocation,"voluntarily deleted from everywhere, B1/G1 registration error"
                    event_log_entry.append(x)
                    event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                    event_log_list.append(event_log_entry)
                else:
                    print("Deletion CANCELLED")
                    print('\n')
        else:
            tmima_count=0
            for i in range(2,10):
                if name_allocation in teacher_name_list[i]:
                    tmima_count+=1
            if tmima_count==0:
                print(name_allocation,"is already registered with the school and can be registered as a general studies teacher with B1/G1")
                print('\n')
                if edit_option==21:
                    print("Confirm allocation of",name_allocation,"to B1? y for YES, any key for NO:")
                    confirm2=input("=>")
                    print('\n')
                    if confirm2=="y":
                        general_studies_teachers.insert(0,name_allocation)
                        event_log_entry=[]
                        x=name_allocation,"added to 'general_studies_teachers'"
                        event_log_entry.append(x)
                        event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                        event_log_list.append(event_log_entry)
                        for i in range(2,6):
                            teacher_name_list[i].insert(0,name_allocation)
                            event_log_entry=[]
                            x=name_allocation,"added to",taxi_tmima_name_list[i],"in 'teacher_name_list' as a B1 general studies teacher"
                            event_log_entry.append(x)
                            event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                            event_log_list.append(event_log_entry)
                        for i in range(10):
                            print(taxi_tmima_name_list[i],'\t',teacher_name_list[i])
                        print('\n')
                        print("B1/G1 general studies registry",'\t',general_studies_teachers)
                        print('\n')
                        print("Allocation to B1 CONFIRMED")
                        print('\n')
                    else:
                        print("Assignment to B1 CANCELLED")
                        print('\n')
                else:
                    print("Confirm allocation of",name_allocation,"to G1? y for YES, any key for NO:")
                    confirm2=input("=>")
                    print('\n')
                    if confirm2=="y":
                        general_studies_teachers.insert(0,name_allocation)
                        event_log_entry=[]
                        x=name_allocation,"added to 'general_studies_teachers'"
                        event_log_entry.append(x)
                        event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                        event_log_list.append(event_log_entry)
                        for i in range(6,10):
                            teacher_name_list[i].insert(0,name_allocation)
                            event_log_entry=[]
                            x=name_allocation,"added to",taxi_tmima_name_list[i],"in 'teacher_name_list' as a G1 general studies teacher"
                            event_log_entry.append(x)
                            event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                            event_log_list.append(event_log_entry)
                        for i in range(10):
                            print(taxi_tmima_name_list[i],'\t',teacher_name_list[i])
                        print('\n')
                        print("B1/G1 general studies registry",'\t',general_studies_teachers)
                        print('\n')
                        print("Allocation to G1 CONFIRMED")
                        print('\n')
                    else:
                        print("Assignment to G1 CANCELLED")
                        print('\n')
            else:
                print("ERROR: The teacher",name_allocation,"is registered at this school but not for general studies,")
                print("keep as a vocational teacher or choose option 25 to completely delete later")
                confirm_delete=input("Do you want to remove now? y for YES, any key for NO:")
                print('\n')
                if confirm_delete=="y":
                    global_delete()
                    event_log_entry=[]
                    x=name_allocation,"voluntarily deleted from everywhere, B1/G1 registration error"
                    event_log_entry.append(x)
                    event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                    event_log_list.append(event_log_entry)
                else:
                    print("Deletion CANCELLED")
                    print('\n')
    edit_option=-1

def edit_option_22_24():
    global edit_option_end,edit_option
    edit_option_end=True
    name()
    integrity_checklist_b1_empty=[]                        
    for i in range(2,6):
        if name_allocation in teacher_name_list[i]:
            integrity_checklist_b1_empty.append(False)
        else:
            integrity_checklist_b1_empty.append(True)
    integrity_b1_empty=all(integrity_checklist_b1_empty)
    integrity_checklist_b1_full=[]                        
    for i in range(2,6):
        if name_allocation in teacher_name_list[i]:
            integrity_checklist_b1_full.append(True)
        else:
            integrity_checklist_b1_full.append(False)
    integrity_b1_full=all(integrity_checklist_b1_full)
    integrity_checklist_g1_empty=[]                        
    for i in range(6,10):
        if name_allocation in teacher_name_list[i]:
            integrity_checklist_g1_empty.append(False)
        else:
            integrity_checklist_g1_empty.append(True)
    integrity_g1_empty=all(integrity_checklist_g1_empty)
    integrity_checklist_g1_full=[]                        
    for i in range(6,10):
        if name_allocation in teacher_name_list[i]:
            integrity_checklist_g1_full.append(True)
        else:
            integrity_checklist_g1_full.append(False)
    integrity_g1_full=all(integrity_checklist_g1_full)
    if name_allocation in all_teachers and name_allocation in general_studies_teachers:
        if edit_option==22 and integrity_b1_full==True:
            print("Confirm deletion of",name_allocation,"from B1?")
            confirm_remove=input("y for YES, n for NO:")
            print('\n')
            if confirm_remove=="y":
                for i in range(2,6):
                    duplicate=0
                    for n in teacher_name_list[i]:
                        if n==name_allocation:
                            duplicate+=1
                            teacher_name_list[i].remove(n)
                            event_log_entry=[]
                            x=name_allocation,"removed as a B1 general studies teacher from",taxi_tmima_name_list[i],"in 'teacher_name_list'"
                            event_log_entry.append(x)
                            event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                            event_log_list.append(event_log_entry)
                            print(name_allocation,"removed as a B1 general studies teacher from",taxi_tmima_name_list[i])
                    if duplicate>1:
                        print("ERROR: Name duplication found and removed in class sector",taxi_tmima_name_list[i])
                    for m in range(5):
                        for n in range(7):
                            if class_table[i][m][n]==name_allocation:
                                class_table[i][m][n]="empty"
                                event_log_entry=[]
                                x=name_allocation,"removed from",taxi_tmima_name_list[i],day_search_list[m],hour_search_list[n],"in 'class_table'"
                                event_log_entry.append(x)
                                event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                                event_log_list.append(event_log_entry)
                if integrity_g1_empty==True and(name_allocation in teacher_name_list[0] or name_allocation in teacher_name_list[1]):
                    for i in range(10):
                        print(taxi_tmima_name_list[i],'\t',teacher_name_list[i])
                    print('\n')
                elif integrity_g1_full==True:
                    for i in range(10):
                        print(taxi_tmima_name_list[i],'\t',teacher_name_list[i])
                    print('\n')
                print("Deletion from B1 CONFIRMED")
                print('\n')
                if integrity_g1_empty==True and name_allocation not in teacher_name_list[0] and name_allocation not in teacher_name_list[1]:
                    print(name_allocation,"is not teaching general studies in B1 or G1 and no other lesson in A1 or A2,")
                    print("will be completely DELETED")
                    print('\n')
                    global_delete()
                    event_log_entry=[]
                    x=name_allocation,"deleted from everywhere, especially 'general_studies_teachers' list, inactive general studies teacher"
                    event_log_entry.append(x)
                    event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                    event_log_list.append(event_log_entry)
                elif integrity_g1_empty==True and(name_allocation in teacher_name_list[0] or name_allocation in teacher_name_list[1]):
                    print("NOTE: A general studies teacher without B1/G1 allocation can reserve the right for new B1/G1 assignments")
                    print("if they maintain at least 1 allocation in A1 or A2")
                    print('\n')
                    print("B1/G1 general studies registry",'\t',general_studies_teachers)
                    print('\n')
            else:
                print("Deletion from B1 CANCELLED")
                print('\n')                               
        elif edit_option==24 and integrity_g1_full==True:
            print("Confirm deletion of",name_allocation,"from G1?")
            confirm_remove=input("y for YES, n for NO:")
            print('\n')
            if confirm_remove=="y":
                for i in range(6,10):
                    duplicate=0
                    for n in teacher_name_list[i]:
                        if n==name_allocation:
                            duplicate+=1
                            teacher_name_list[i].remove(n)
                            event_log_entry=[]
                            x=name_allocation,"removed as a G1 general studies teacher from",taxi_tmima_name_list[i],"in 'teacher_name_list'"
                            event_log_entry.append(x)
                            event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                            event_log_list.append(event_log_entry)
                            print(name_allocation,"removed as a G1 general studies teacher from",taxi_tmima_name_list[i])
                    if duplicate>1:
                        print("ERROR: Name duplication found and removed in class sector",taxi_tmima_name_list[i])  
                    for m in range(5):
                        for n in range(7):
                             if class_table[i][m][n]==name_allocation:
                                class_table[i][m][n]="empty"
                                event_log_entry=[]
                                x=name_allocation,"removed from",taxi_tmima_name_list[i],day_search_list[m],hour_search_list[n],"in 'class_table'"
                                event_log_entry.append(x)
                                event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                                event_log_list.append(event_log_entry)   
                if integrity_b1_empty==True and(name_allocation in teacher_name_list[0] or name_allocation in teacher_name_list[1]):
                    for i in range(10):
                        print(taxi_tmima_name_list[i],'\t',teacher_name_list[i])
                    print('\n')
                elif integrity_b1_full==True:
                    for i in range(10):
                        print(taxi_tmima_name_list[i],'\t',teacher_name_list[i])
                    print('\n')
                print("Deletion from G1 CONFIRMED")
                print('\n')
                if integrity_b1_empty==True and name_allocation not in teacher_name_list[0] and name_allocation not in teacher_name_list[1]:
                    print(name_allocation,"is not teaching general studies in B1 or G1 and no other lesson in A1 or A2,")
                    print("will be completely DELETED")
                    print('\n')
                    global_delete()
                    event_log_entry=[]
                    x=name_allocation,"deleted from everywhere, especially 'general_studies_teachers' list, inactive general studies teacher"
                    event_log_entry.append(x)
                    event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                    event_log_list.append(event_log_entry)
                elif integrity_b1_empty==True and(name_allocation in teacher_name_list[0] or name_allocation in teacher_name_list[1]):
                    print("NOTE: A general studies teacher without B1/G1 allocation can reserve the right for new B1/G1 assignments")
                    print("if they maintain at least 1 allocation in A1 or A2")
                    print('\n')
                    print("B1/G1 general studies registry",'\t',general_studies_teachers)
                    print('\n')
            else:
                print("Deletion from G1 CANCELLED")
                print('\n')                              
        elif edit_option==22 and integrity_b1_empty==True:
            print("ERROR: Cannot remove",name_allocation,"because teacher not assigned to B1 general studies")
            print('\n')
        elif edit_option==24 and integrity_g1_empty==True:
            print("ERROR: Cannot remove",name_allocation,"because teacher not assigned to G1 general studies")
            print('\n')
        else:
            print("ERROR: class sector allocation for general studies inconsistent and corrupted, deleting",name_allocation)
            print("completely from the school, you need to reregister and reassign the name correctly")
            print('\n')
            global_delete()
            event_log_entry=[]
            x=name_allocation,"deleted from everywhere, data corrupted"
            event_log_entry.append(x)
            event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
            event_log_list.append(event_log_entry)
    else:
        print("ERROR: Cannot remove general studies teacher,",name_allocation,"not registered")
        print('\n')
    edit_option=-1

def edit_option_25():
    global edit_option_end,edit_option
    edit_option_end=True
    name()
    print("Do you want to completely remove",name_allocation,"from the school database?")
    confirm_delete=input("y for YES, any key for NO:")
    print('\n')
    if confirm_delete=="y":
        global_delete()
        event_log_entry=[]
        x="voluntary complete removal of",name_allocation
        event_log_entry.append(x)
        event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
        event_log_list.append(event_log_entry)
    else:
        print("Complete deletion CANCELLED")
        print('\n')
    edit_option=-1

def edit_option_26():
    global edit_option_end,edit_option
    edit_option_end=True
    print("NOTE: If you want to add a teacher with privileged access to BOTH general studies AND vocational studies for B1/G1,")
    print("add (surname) in option 26, the program will create '(surname)_general' and '(surname)_vocational'")
    print("The program will automatically assign '(surname)_general' to all class sectors, you can assign '(surname)_vocational' later")
    print('\n')
    name()
    check=0
    for i in all_teachers:
        if i!="EDIT TEACHER DATABASE" and i!="EXIT TO MAIN MENU":
            if name_allocation in i or i in name_allocation:
                check+=1
    if check==0:
        print("CONFIRM: Add",name_allocation,"with privileged access to both general and vocational classes?")
        privilege=input("y for YES, any key for NO:")
        print('\n')
        if privilege=="y":
            name_allocation_1,name_allocation_2=name_allocation+"_general",name_allocation+"_vocational"
            all_teachers.insert(0,name_allocation_1)
            general_studies_teachers.insert(0,name_allocation_1)
            event_log_entry=[]
            x=name_allocation_1,"added to 'all_teachers' and 'general_studies_teachers'"
            event_log_entry.append(x)
            event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
            event_log_list.append(event_log_entry)
            for i in range(10):
                teacher_name_list[i].insert(0,name_allocation_1)
                event_log_entry=[]
                x=name_allocation,"added to",taxi_tmima_name_list[i],"in 'teacher_name_list' as privileged general studies teacher"
                event_log_entry.append(x)
                event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                event_log_list.append(event_log_entry)
            for i in range(10):
                print(taxi_tmima_name_list[i],'\t',teacher_name_list[i])
            print('\n')
            print("B1/G1 general studies registry",'\t',general_studies_teachers)
            print('\n')
            all_teachers.insert(0,name_allocation_2)
            event_log_entry=[]
            x=name_allocation_2,"added to 'all_teachers'"
            event_log_entry.append(x)
            event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
            event_log_list.append(event_log_entry)
            print("Allocation of",name_allocation_1,"to all class sectors and general studies registry, and",name_allocation_2," in central registry CONFIRMED")
            print('\n')
        else:
            print("Allocation CANCELLED")
    else:
        print("ERROR: Name already exists in system")
    edit_option=-1

def edit_database():
    global edit_option,edit_option_end,teacher_index_list,menu_range_variable_list
    process_repeat=True
    while process_repeat==True or edit_option==-1:
        try:
            print("Assign or remove teachers in school central registry, customize availability for assignment menus, error checking/troubleshooting:")
            print('\n')
            for i in range(26):
                print(option_list[i])
            print("0 to return to SUB-MENU")
            print('\n')
            edit_option=int(input("Enter option number 0-26:"))
            print('\n')
            while not(type(edit_option)==int and edit_option>=0 and edit_option<=26):
                print("ERROR: Try again")
                print('\n')
                print("Assign or remove teachers in school central registry, customize availability for assignment menus, error checking/troubleshooting:")
                print('\n')
                for i in range(25):
                    print(option_list[i])
                print("0 to return to SUB-MENU")
                print('\n')
                edit_option=int(input("Enter option number 0-26:"))
                print('\n')
        except:
            print("String ERROR: Value must be integer")
            print('\n')
        else:
            if edit_option==0:
                process_repeat=False
                print("Returning to SUB-MENU")
                print('\n')
            elif edit_option==-1:
                process_repeat=True
                edit_option_end=False
            else:
                if edit_option>=1 and edit_option<=20 and edit_option%2!=0:
                    edit_option_1_20_odd()
                    if edit_option_end==True:
                        process_repeat=False
                elif edit_option>=1 and edit_option<=20 and edit_option%2==0:
                    edit_option_1_20_even()
                    if edit_option_end==True:
                        process_repeat=False
                elif edit_option==21 or edit_option==23:
                    edit_option_21_23()
                    if edit_option_end==True:
                        process_repeat=False
                elif edit_option==22 or edit_option==24:
                    edit_option_22_24()
                    if edit_option_end==True:
                        process_repeat=False
                elif edit_option==25:
                    edit_option_25()
                    if edit_option_end==True:
                        process_repeat=False
                elif edit_option==26:
                    edit_option_26()
                    if edit_option_end==True:
                        process_repeat=False
                                           
def save():
    lesson_table_filename='lesson_table.json'
    with open(lesson_table_filename,'w') as lesson_table_file:
        json.dump(class_table,lesson_table_file)
    print("Lesson table file saved in the same folder as this script")
    print("Confirming the weekly lesson table has been saved from 'class_table' list to 'lesson_table.json'")
    print('\n')
    teacher_vocation_filename='teacher_vocation.json'
    with open(teacher_vocation_filename,'w') as teacher_vocation_file:
        json.dump(teacher_name_list,teacher_vocation_file)
    print("Teachers per vocational department list file saved in the same folder as this script")
    print("Confirming the teachers per vocational department list has been saved from 'teacher_name_list' list to 'teacher_vocation.json'")
    print('\n')
    general_studies_filename='general_studies.json'
    with open(general_studies_filename,'w') as general_studies_file:
        json.dump(general_studies_teachers,general_studies_file)
    print("General studies teachers list file saved in the same folder as this script")
    print("Confirming the general studies teachers list has been saved from 'general_studies_teachers' list to 'general_studies.json'")
    print('\n')
    teachers_complete_filename='teachers_complete.json'
    with open(teachers_complete_filename,'w') as teachers_complete_file:
        json.dump(all_teachers,teachers_complete_file)
    print("Complete teachers list file saved in the same folder as this script")
    print("Confirming the complete teachers list has been saved from 'all_teachers' list to 'teachers_complete.json'")
    print('\n') 

def global_itinerary_database_manager():
    main_repeat_2=True
    while main_repeat_2==True:
        try:
            print("Show weekly lesson schedule for 1 teacher, for all their class sectors and lessons, and which class sectors they are allocated to")
            print('\n')
            print("Choose teacher or edit database or exit from menu:0-",len(all_teachers)-1,":")
            print('\n')
            for i in range(len(all_teachers)):
                print("Choose",i,"for",'\t',all_teachers[i])
            print('\n')
            teacher_choice=int(input("=>>"))
            print('\n')
            while not(type(teacher_choice)==int and teacher_choice>=0 and teacher_choice<=len(all_teachers)-1):
                print("ERROR: Try again")
                print('\n')
                print("Choose teacher or edit database or exit from menu:0-",len(all_teachers)-1,":")
                print('\n')
                for i in range(len(all_teachers)):
                    print("Choose",i,"for",'\t',all_teachers[i])
                print('\n')
                teacher_choice=int(input("=>>"))
                print('\n')
        except:
            print("String ERROR: Value must be integer")
            print('\n')
        else:
            if teacher_choice!=len(all_teachers)-1 and teacher_choice!=len(all_teachers)-2:
                count=0
                for i in range(10):
                    for m in range(5):
                        for n in range(7):
                            if all_teachers[teacher_choice]==class_table[i][m][n]:
                                count+=1
                                if all_teachers[teacher_choice] in general_studies_teachers and i>=2 and i<=5:
                                    print("The teacher",all_teachers[teacher_choice],"is scheduled for B1",day_search_list[m],hour_search_list[n])
                                elif all_teachers[teacher_choice] in general_studies_teachers and i>=6 and i<=9:
                                    print("The teacher",all_teachers[teacher_choice],"is scheduled for G1",day_search_list[m],hour_search_list[n])
                                else:
                                    print("The teacher",all_teachers[teacher_choice],"is scheduled for",taxi_tmima_name_list[i],day_search_list[m],hour_search_list[n])
                if count==0:
                    print("The teacher",all_teachers[teacher_choice],"is unavailable or not scheduled yet")              
                print('\n')
                count=0
                for i in range(10):
                    if all_teachers[teacher_choice] in teacher_name_list[i]:
                        count+=1
                        print(all_teachers[teacher_choice],"is allocated as available for class sectors",taxi_tmima_name_list[i],)
                        if all_teachers[teacher_choice] in general_studies_teachers and  i>=2 and i<=5:
                            print("as a B1 general studies teacher")
                        elif all_teachers[teacher_choice] in general_studies_teachers and  i>=6 and i<=9:
                            print("as a G1 general studies teacher")
                        elif all_teachers[teacher_choice] in general_studies_teachers and(i==0 or i==1):
                            print("and can also be allocated to B1/G1 general studies")
                if count==0:
                    print(all_teachers[teacher_choice],"currently has no allocation to any class sector but can be allocated in the following combinations,")
                    if "_vocational" in all_teachers[teacher_choice]:
                        print("vocational grades B/G")
                    elif "_vocational" not in all_teachers[teacher_choice] and all_teachers[teacher_choice] not in general_studies_teachers:
                        print("grade A and vocational grades B/G")   
                print('\n')
            elif teacher_choice==len(all_teachers)-2:
                edit_database()
            else:
                main_repeat_2=False
                print("Returning to Main Menu")
                print('\n')
                
try:
    main_repeat=True
    while main_repeat==True:
        print("MAIN MENU:")
        print("Choose YOUR grade/vocational sector to access all general and vocational teachers available in your grade and vocational sector")
        print('\n')
        for i in range(10):
            print("Choose",taxi_tmima_index_list[i],"for",taxi_tmima_name_list[i])
        print("Or 0 for SUB-MENU: Show all teachers/Edit database")
        print("Or 11 to end program")
        print('\n')
        try:
            taxi_tmima_input=int(input("Choose grade and department:"))
            print('\n')
            while not(type(taxi_tmima_input)==int and taxi_tmima_input>=0 and taxi_tmima_input<=11):
                print("ERROR: Try again")
                print('\n')
                print("MAIN MENU:")
                print("Choose YOUR grade/vocational sector to access all general and vocational teachers available in your grade and vocational sector")
                print('\n')
                for i in range(10):
                    print("Choose",taxi_tmima_index_list[i],"for",taxi_tmima_name_list[i])
                print("Or 0 for SUB-MENU: Show all teachers/Edit database")
                print("Or 11 to end program")
                print('\n')
                taxi_tmima_input=int(input("Choose grade and department:"))
                print('\n')
        except:
            print("String ERROR: Value must be integer")
            print('\n')
        else:
            if taxi_tmima_input==0:
                global_itinerary_database_manager()
            elif taxi_tmima_input>=1 and taxi_tmima_input<=10:
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
                for i,m,n in zip((taxi_tmima_name_list),(taxi_tmima_index_list),(menu_range_variable_list)):
                    if m==taxi_tmima_input:
                        taxi_tmima_name,taxi_tmima_index,menu_range_variable=i,m-1,n
                taxi_tmima_menu()
            else:
                main_repeat=False
                confirm_save=input("Save changes before exit? y for YES, any key for NO:")
                print('\n')
                if confirm_save=="y":
                    save()
                    event_log_entry=[]
                    event_log_entry.append("Changes SAVED")
                    event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
                    event_log_list.append(event_log_entry)
                    print("Save CONFIRMED")
                    print('\n')
                else:
                    print("Changes discarded")
                    print('\n')
                pause_key=input("Do you want to see the timestamped EVENT LOG before exit? y for YES, any key for NO:")
                print ('\n')
                if pause_key=="y":
                    for i in range(len(event_log_list)):
                        if i%10==0 and i!=0:
                            pause_input=input("Press any key to keep scrolling")
                            print('\n')
                        print(event_log_list[i][0])
                        print(event_log_list[i][1])
                        print('\n')
                if len(event_log_list)>70:
                    print("The timestamped EVENT LOG has exceeded maximum length, deleting oldest entries to conserve memory")
                    print('\n')
                    del event_log_list[0:len(event_log_list)-70]
                event_log_filename='event_log.json'
                with open(event_log_filename,'w') as event_log_file:
                    json.dump(event_log_list,event_log_file)
                print("Event log file saved in the same folder as this script")
                print("Confirming the event log list has been saved from 'event_log_list' list to 'event_log.json'")
                print('\n')
                try:
                    sys.exit("Program Safely Ended")
                except SystemExit as error:
                    print(error)
                    print('\n')
                finally:
                    print("Cleaning up memory")
                    print('\n')
                    for key in list(globals().keys()):
                        if "__" not in key and "sys" not in key and "main" not in key:
                            globals()[key]=None
                        else:
                            print("SAFETY ALERT: No deletion:",'\t',key,'\t',globals()[key])
                    for key,val in zip((list(globals().keys())),(list(globals().values()))):
                        print("Resetting data...",'\t',"Key:",key,'\t',"Data:",val)
                    print('\n')
                    print("Cleanup Completed")
                    close_window=input("Press ENTER to close window")
except:
    try:
        sys.exit(sys.exc_info())
    except SystemExit as error:
        print("ERROR: Program Terminated")
        error_code=error.code[1]
        print("Error type:",error_code)
        trace_back=traceback.format_tb(error.code[2])[-1]
        print("Error_location:",trace_back)
        event_log_entry=[]
        x=[str(error_code),str(trace_back)]
        event_log_entry.append(x)
        event_log_entry.append(datetime.datetime.now().strftime("event timestamp: date:%d/%m/%Y time:%H:%M:%S day:%A"))
        event_log_list.append(event_log_entry)
        event_log_filename='event_log.json'
        with open(event_log_filename,'w') as event_log_file:
            json.dump(event_log_list,event_log_file)
        print("Error timestamp saved to event log but data changes NOT saved")
    finally:
        print("Cleanup complete")
        close_window=input("Press ENTER to close window")
     

    
                
            
            
            
        
        
    




