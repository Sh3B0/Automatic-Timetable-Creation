"""
 # Author : Ahmed Nouralla
 # Project: Automatic Timetable Creation
 # Input  : List of activities
 # Output : XLSX/CSV file of activities with respective allocation

 # Assumptions
    - Input data is valid!
    - Each activity take one time slot
    - Each activity can be lecture/tutorial/lab (order should be maintained, no exception)
    - Activities should be sorted by NAME -> type(lec>tut>lab)
    - Lecture/Tutorial are allocated in big_rooms, Labs in small_rooms

 # Conflict types
    1: Activities i, j by same instructor, different targets
    2: Activities i, j by different instructors, same targets
    3: Activities i, j by same instructor, same targets.
    4: Activities i != j using same room at same time

 # Allocation tuple: (day, slot, room)
    - day in [1="Monday", 5="Friday"]
    - slot in [1="9:00-10:30", 8="19:20-20:50"]
    - room in [big_rooms] union [small_rooms]

 # CSV Output
    day,slot,targets,a_name(a_type),a_inst,room
    Monday,9:00-10:30,[B19-00-**|...],FSE(Lec),Bobrov,108
    Tuesday,9:00-10:30,[B19-00-**|...],OS(Lec),Succi,108
    ...

 # XLSX Output
    For now, the application will use a template sheet with the current number of groups for each course
        TODO: generate table from scratch (input number of groups, time-slots, etc)

 # Template data:
    B20-CE-(01:04) (B-E)
    B20-CS-(01:02) (F-G)
    B19-00-(01:06) (H-M)
    B18-DS-(01:02) (N-O)
    B18-SE-(01:02) (P-Q)
    B18-SB-(01) (R)
    B18-RO-(01) (S)
    B17-DS-(01:02) (T-U)
    B17-SE-(01:02) (V-W)
    B17-SB-(01) (X)
    B17-RO-(01) (Y)
    M19-DS-01, M19-SE-01, M19-SB-01, M19-RO-01 (Z-AC)
    M20-DS-01, M20-SE-01, M20-SB-01, M20-RO-01 (AD-AG)
"""

from activity import *
from algorithm import *
from output import *


def prompt(a, a_id):
    """
    Prompts user for activity data, for creating/editing
    :param a: the activity object to operate on
    :param a_id: the id of activity
    """
    try:
        a[a_id].a_name = input("Enter activity name: ")
        a[a_id].a_inst = input("Enter activity instructor name: ")
        a[a_id].a_type = int(input("Enter activity type (1: Lec, 2: Tut, 3: Lab): "))
        if a[a_id].a_type not in range(1, 4):
            raise Exception("Invalid Activity type")

        cnt = 1
        a[a_id].targets = []
        while True:
            t1 = input("Enter activity target #" + str(cnt) + ", or -1 to end (Examples: B19, M20): ")
            if t1 == '-1':
                break
            t2 = input("Enter activity group: (Examples: CE, SE, 00 for not applicable, ** for all): ")
            t3 = input("Enter activity sub-group: (Examples: 01, 06, ** for all): ")
            a[a_id].targets.append((t1, t2, t3))
            cnt += 1
        inp = int(input("Enter activity prerequisite\n"
                        "(ID of respective tutorial/lecture activity, or -1 if not applicable): "))
        if inp != -1 and a_id in activity_by_id:
            a[a_id].refers_to = inp
    except:
        print("Error during prompt, please make sure you entered correct activity!")
        a.pop()


def get_id():
    """
    Prompts user for activity id until a valid input is given
    :return: the activity id obtained
    """
    while True:
        a_id = int(input("Enter activity ID: "))
        if a_id not in activity_by_id:
            print("Invalid ID")
            continue
        else:
            break
    return a_id


def input_mode():
    """
    Interactive input for the program
    """
    a = []
    print("Welcome to the fancy command-line GUI of Automatic Timetable Creation software:")
    while True:
        print("\t0- Generate table with sample activity", "\t1- Create activity", "\t2- Update activity",
              "\t3- Remove activity", "\t4- Check activity", "\t5- Generate schedule!",
              "\t6- Rate us xD", "\t7- Exit", sep="\n")
        # try:
        choice = int(input())
        if choice == 0:
            test_mode()
            print("Done! Check results in 'Output' folder")
            input("Press Enter to continue...")
            break
        elif choice == 1:
            a.append(Activity())
            print("Activity created with ID:", len(a) - 1, "\n\tPlease note down that number for further changes\t")
            prompt(a, -1)
            print("Activity added successfully")
        elif choice == 2:
            a_id = get_id()
            print("Enter new activity")
            prompt(a, a_id)
            print("Activity updated successfully")
        elif choice == 3:
            a_id = get_id()
            a.pop(a_id)
            print("Activity removed successfully")
        elif choice == 4:
            a_id = get_id()
            activity_by_id[a_id].pretty_print()
        elif choice == 5:
            a.sort()
            generate(a)
            csv_output(a)
            xlsx_output(a)
            print("Done! Check results in 'Output' folder")
            input("Press Enter to continue...")
            break
        elif choice == 6:
            print("Sad")
        elif choice == 7:
            break
        else:
            print("Invalid input")
        # except:
        #     print("An Error Occurred")


def test_mode():
    """
    Hard-coded sample data to test program logic
    """
    a = []
    for idx in range(98):
        a.append(None)

    a[0] = Activity(a_name="FSE", a_inst="Evgeniy Bobrov", a_type=1, targets=[("B19", "00", "**")])
    a[1] = Activity(a_name="FSE", a_inst="Pavel Kolychev", a_type=3, refers_to=0, targets=[("B19", "00", "01")])
    a[2] = Activity(a_name="FSE", a_inst="Pavel Kolychev", a_type=3, refers_to=0, targets=[("B19", "00", "02")])
    a[3] = Activity(a_name="FSE", a_inst="Nursultan Askarbekuly", a_type=3, refers_to=0,
                    targets=[("B19", "00", "03")])
    a[4] = Activity(a_name="FSE", a_inst="Nursultan Askarbekuly", a_type=3, refers_to=0,
                    targets=[("B19", "00", "04")])
    a[5] = Activity(a_name="FSE", a_inst="Oleg Ignatov", a_type=3, refers_to=0, targets=[("B19", "00", "05")])
    a[6] = Activity(a_name="FSE", a_inst="Oleg Ignatov", a_type=3, refers_to=0, targets=[("B19", "00", "06")])

    a[7] = Activity(a_name="OS", a_inst="Giancarlo Succi", a_type=1, targets=[("B19", "00", "**")])
    a[8] = Activity(a_name="OS", a_inst="Nikita Lozhnikov", a_type=2, refers_to=7, targets=[("B19", "00", "**")])
    a[9] = Activity(a_name="OS", a_inst="Nikita Lozhnikov", a_type=3, refers_to=8, targets=[("B19", "00", "01")])
    a[10] = Activity(a_name="OS", a_inst="Nikita Lozhnikov", a_type=3, refers_to=8, targets=[("B19", "00", "02")])
    a[11] = Activity(a_name="OS", a_inst="Xavier Vasquez", a_type=3, refers_to=8, targets=[("B19", "00", "03")])
    a[12] = Activity(a_name="OS", a_inst="Xavier Vasquez", a_type=3, refers_to=8, targets=[("B19", "00", "04")])
    a[13] = Activity(a_name="OS", a_inst="Shokhista Ergasheva", a_type=3, refers_to=8,
                     targets=[("B19", "00", "05")])
    a[14] = Activity(a_name="OS", a_inst="Shokhista Ergasheva", a_type=3, refers_to=8,
                     targets=[("B19", "00", "06")])

    a[15] = Activity(a_name="PM", a_inst="Igor Gaponov", a_type=1, targets=[("B19", "00", "**")])
    a[16] = Activity(a_name="PM", a_inst="Semen Kurkin", a_type=2, refers_to=15, targets=[("B19", "00", "**")])
    a[17] = Activity(a_name="PM", a_inst="Mikhail Ivanov", a_type=3, refers_to=16, targets=[("B19", "00", "01")])
    a[18] = Activity(a_name="PM", a_inst="Mikhail Ivanov", a_type=3, refers_to=16, targets=[("B19", "00", "02")])
    a[19] = Activity(a_name="PM", a_inst="Victor Nikiforov", a_type=3, refers_to=16, targets=[("B19", "00", "03")])
    a[20] = Activity(a_name="PM", a_inst="Victor Nikiforov", a_type=3, refers_to=16, targets=[("B19", "00", "04")])
    a[21] = Activity(a_name="PM", a_inst="Victor Nikiforov", a_type=3, refers_to=16, targets=[("B19", "00", "05")])
    a[22] = Activity(a_name="PM", a_inst="Victor Nikiforov", a_type=3, refers_to=16, targets=[("B19", "00", "06")])

    a[23] = Activity(a_name="PS", a_inst="Sergey Gorodetskiy", a_type=1, targets=[("B19", "00", "**")])
    a[24] = Activity(a_name="PS", a_inst="Sergey Gorodetskiy", a_type=2, refers_to=23,
                     targets=[("B19", "00", "**")])
    a[25] = Activity(a_name="PS", a_inst="Sergey Gorodetskiy", a_type=3, refers_to=24,
                     targets=[("B19", "00", "01")])
    a[26] = Activity(a_name="PS", a_inst="Alexey Shikulin", a_type=3, refers_to=24, targets=[("B19", "00", "02")])
    a[27] = Activity(a_name="PS", a_inst="Alexey Shikulin", a_type=3, refers_to=24, targets=[("B19", "00", "03")])
    a[28] = Activity(a_name="PS", a_inst="Alexey Shikulin", a_type=3, refers_to=24, targets=[("B19", "00", "04")])
    a[29] = Activity(a_name="PS", a_inst="Alexey Shikulin", a_type=3, refers_to=24, targets=[("B19", "00", "05")])
    a[30] = Activity(a_name="PS", a_inst="Azat Gaitudinov", a_type=3, refers_to=24, targets=[("B19", "00", "06")])

    a[31] = Activity(a_name="DE", a_inst="Nikolay Shilov", a_type=1, targets=[("B19", "00", "**")])
    a[32] = Activity(a_name="DE", a_inst="Ivan Konyukhov", a_type=2, refers_to=31, targets=[("B19", "00", "**")])
    a[33] = Activity(a_name="DE", a_inst="Marat Mingazov", a_type=3, refers_to=32, targets=[("B19", "00", "01")])
    a[34] = Activity(a_name="DE", a_inst="Marat Mingazov", a_type=3, refers_to=32, targets=[("B19", "00", "02")])
    a[35] = Activity(a_name="DE", a_inst="Victor Kazorin", a_type=3, refers_to=32, targets=[("B19", "00", "03")])
    a[36] = Activity(a_name="DE", a_inst="Victor Kazorin", a_type=3, refers_to=32, targets=[("B19", "00", "04")])
    a[37] = Activity(a_name="DE", a_inst="Marat Mingazov", a_type=3, refers_to=32, targets=[("B19", "00", "05")])
    a[38] = Activity(a_name="DE", a_inst="Marat Mingazov", a_type=3, refers_to=32, targets=[("B19", "00", "06")])

    a[39] = Activity(a_name="DM", a_inst="Andrey Frolov", a_type=1, targets=[("B20", "**", "**")])
    a[40] = Activity(a_name="DM", a_inst="Andrey Frolov", a_type=2, refers_to=39, targets=[("B20", "**", "**")])

    a[41] = Activity(a_name="PSS", a_inst="Eugene Zouev", a_type=1, targets=[("B20", "CE", "**")])
    a[42] = Activity(a_name="PSS", a_inst="Eugene Zouev", a_type=2, refers_to=41, targets=[("B20", "CE", "**")])
    a[43] = Activity(a_name="ITP", a_inst="Luiz Araujo", a_type=1, targets=[("B20", "CS", "**")])
    a[44] = Activity(a_name="ITP", a_inst="Luiz Araujo", a_type=2, refers_to=43, targets=[("B20", "CS", "**")])
    a[45] = Activity(a_name="FP", a_inst="Mirko Farina", a_type=1, targets=[("B20", "**", "**")])
    a[46] = Activity(a_name="C1", a_inst="Ivan Konyukhov", a_type=1, targets=[("B20", "CE", "**")])
    a[47] = Activity(a_name="C1", a_inst="Ivan Konyukhov", a_type=2, refers_to=46, targets=[("B20", "CE", "**")])
    a[48] = Activity(a_name="MA1", a_inst="Sergey Gorodetskiy", a_type=1, targets=[("B20", "CS", "**")])
    a[49] = Activity(a_name="MA1", a_inst="Sergey Gorodetskiy", a_type=2, refers_to=48,
                     targets=[("B20", "CS", "**")])
    a[50] = Activity(a_name="CA", a_inst="Alexander Tormasov", a_type=1, targets=[("B20", "**", "**")])
    a[51] = Activity(a_name="CA", a_inst="Artem Burmyakov", a_type=2, refers_to=50, targets=[("B20", "CE", "**")])
    a[52] = Activity(a_name="CA", a_inst="Muhammad Fahim", a_type=2, refers_to=50, targets=[("B20", "CS", "**")])
    a[53] = Activity(a_name="AGLA", a_inst="Vladimir Ivanov", a_type=1, targets=[("B20", "CE", "**")])
    a[54] = Activity(a_name="AGLA", a_inst="Leonid Merkin", a_type=1, targets=[("B20", "CS", "**")])
    a[55] = Activity(a_name="AGLA", a_inst="Mohammad Bahrami", a_type=2, refers_to=53,
                     targets=[("B20", "CE", "**")])
    a[56] = Activity(a_name="AGLA", a_inst="Ivan Konyukhov", a_type=2, refers_to=54, targets=[("B20", "CS", "**")])

    a[57] = Activity(a_name="AGLA", a_inst="Anastasiya Puzankova", a_type=3, refers_to=55,
                     targets=[("B20", "CE", "01")])
    a[58] = Activity(a_name="AGLA", a_inst="Anastasiya Puzankova", a_type=3, refers_to=55,
                     targets=[("B20", "CE", "02")])
    a[59] = Activity(a_name="AGLA", a_inst="Oleg Bulichev", a_type=3, refers_to=55, targets=[("B20", "CE", "03")])
    a[60] = Activity(a_name="AGLA", a_inst="Oleg Bulichev", a_type=3, refers_to=55, targets=[("B20", "CE", "04")])
    a[61] = Activity(a_name="AGLA", a_inst="Nikolay Kudasov", a_type=3, refers_to=56, targets=[("B20", "CS", "01")])
    a[62] = Activity(a_name="AGLA", a_inst="Nikolay Kudasov", a_type=3, refers_to=56, targets=[("B20", "CS", "02")])

    a[63] = Activity(a_name="PSS", a_inst="Sirojiddin Komolov", a_type=3, refers_to=42,
                     targets=[("B20", "CE", "01")])
    a[64] = Activity(a_name="PSS", a_inst="Sirojiddin Komolov", a_type=3, refers_to=42,
                     targets=[("B20", "CE", "02")])
    a[65] = Activity(a_name="PSS", a_inst="Mansur Khazeev", a_type=3, refers_to=42, targets=[("B20", "CE", "03")])
    a[66] = Activity(a_name="PSS", a_inst="Mansur Khazeev", a_type=3, refers_to=42, targets=[("B20", "CE", "04")])
    a[67] = Activity(a_name="ITP", a_inst="Munir Makhmutov", a_type=3, refers_to=44, targets=[("B20", "CS", "01")])
    a[68] = Activity(a_name="ITP", a_inst="Munir Makhmutov", a_type=3, refers_to=44, targets=[("B20", "CS", "02")])

    a[69] = Activity(a_name="C1", a_inst="Ivan Konyukhov", a_type=3, refers_to=47, targets=[("B20", "CE", "01")])
    a[70] = Activity(a_name="C1", a_inst="Ivan Konyukhov", a_type=3, refers_to=47, targets=[("B20", "CE", "02")])
    a[71] = Activity(a_name="C1", a_inst="Ramil Dautov", a_type=3, refers_to=47, targets=[("B20", "CE", "03")])
    a[72] = Activity(a_name="C1", a_inst="Ramil Dautov", a_type=3, refers_to=47, targets=[("B20", "CE", "04")])
    a[73] = Activity(a_name="MA1", a_inst="Pavel Khakimov", a_type=3, refers_to=49, targets=[("B20", "CS", "01")])
    a[74] = Activity(a_name="MA1", a_inst="Pavel Khakimov", a_type=3, refers_to=49, targets=[("B20", "CS", "02")])

    a[75] = Activity(a_name="CA", a_inst="Vladislav Ostankovich", a_type=3, refers_to=51,
                     targets=[("B20", "CE", "01")])
    a[76] = Activity(a_name="CA", a_inst="Vladislav Ostankovich", a_type=3, refers_to=51,
                     targets=[("B20", "CE", "02")])
    a[77] = Activity(a_name="CA", a_inst="Manuel Rodriguez", a_type=3, refers_to=51, targets=[("B20", "CE", "03")])
    a[78] = Activity(a_name="CA", a_inst="Manuel Rodriguez", a_type=3, refers_to=51, targets=[("B20", "CE", "04")])
    a[79] = Activity(a_name="CA", a_inst="Hamza Salem", a_type=3, refers_to=52, targets=[("B20", "CS", "01")])
    a[80] = Activity(a_name="CA", a_inst="Hamza Salem", a_type=3, refers_to=52, targets=[("B20", "CS", "02")])

    a[81] = Activity(a_name="FP", a_inst="Hamna Aslam", a_type=3, refers_to=45, targets=[("B20", "CE", "01")])
    a[82] = Activity(a_name="FP", a_inst="Hamna Aslam", a_type=3, refers_to=45, targets=[("B20", "CE", "02")])
    a[83] = Activity(a_name="FP", a_inst="Timur Fayzrakhmanov", a_type=3, refers_to=45,
                     targets=[("B20", "CE", "03")])
    a[84] = Activity(a_name="FP", a_inst="Mirko Farina", a_type=3, refers_to=45, targets=[("B20", "CE", "04")])
    a[85] = Activity(a_name="FP", a_inst="Timur Fayzrakhmanov", a_type=3, refers_to=45,
                     targets=[("B20", "CS", "01")])
    a[86] = Activity(a_name="FP", a_inst="Mirko Farina", a_type=3, refers_to=45, targets=[("B20", "CS", "02")])

    a[87] = Activity(a_name="DM", a_inst="Naumcheva Mariya", a_type=3, refers_to=40, targets=[("B20", "CE", "01")])
    a[88] = Activity(a_name="DM", a_inst="Ilya Khomyakov", a_type=3, refers_to=40, targets=[("B20", "CE", "02")])
    a[89] = Activity(a_name="DM", a_inst="Naumcheva Mariya", a_type=3, refers_to=40, targets=[("B20", "CE", "03")])
    a[90] = Activity(a_name="DM", a_inst="Ruzilia Mukhutdinova", a_type=3, refers_to=40,
                     targets=[("B20", "CE", "04")])
    a[91] = Activity(a_name="DM", a_inst="Ilya Khomyakov", a_type=3, refers_to=40, targets=[("B20", "CS", "01")])
    a[92] = Activity(a_name="DM", a_inst="Ruzilia Mukhutdinova", a_type=3, refers_to=40,
                     targets=[("B20", "CS", "02")])
    a[93] = Activity(a_name="DS", a_inst="Ahsan Kazmi", a_type=1,
                     targets=[("B18", "DS", "**"), ("B18", "SE", "**"), ("B18", "SB", "**")])
    a[94] = Activity(a_name="P2", a_inst="Artur Karimov", a_type=1,
                     targets=[("B18", "RO", "**"), ("B18", "SB", "**")])
    a[95] = Activity(a_name="EM", a_inst="Giancarlo Succi", a_type=1,
                     targets=[("M20", "SE", "**"), ("M20", "DS", "**")])
    a[96] = Activity(a_name="FME", a_inst="Hein Roelfsema", a_type=1,
                     targets=[("B17", "SE", "**"), ("B17", "SB", "**")])
    a[97] = Activity(a_name="CV", a_inst="Mohamed Fahim", a_type=1,
                     targets=[("B17", "RO", "**"), ("B17", "DS", "**")])

    a.sort()
    # for u in a:
    #     print(u)
    generate(a)
    csv_output(a)
    xlsx_output(a)


if __name__ == '__main__':
    # TestMode()
    input_mode()
