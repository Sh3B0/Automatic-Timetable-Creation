import csv


def schedule():
    arr = []
    for i in range(5):
        arr.append([])
        for j in range(8):
            arr[i].append([])

    # print (arr)

    time_to_slots = {"9:00": 0, "10:40": 1, "12:40": 2, "14:20": 3}
    days_to_slot = {"Mon": 0, "Tus": 1, "Wed": 2, "Thr": 3, "Fri": 4}
    slot_to_time = {0: "9:00", 1: "10:40", 2: "12:40", 3: "14:20"}
    slot_to_day = {0: "Mon", 1: "Tus", 2: "Wed", 3: "Thr", 4: "Fri"}
    # size of the room, lecturer, time slot, day of the week, subjects, number of the study group
    Classes = [["Big", "Shilov", "10:40", "Tus", "DE", "BS-19", "lec"],
               ["Big", "Babrov", "10:40", "Mon", "FSE", "BS-19", "lec"],
               ["Big", "Babrov", "12:40", "Mon", "FSE", "BS-19", "tut"],
               ["small", "Marat", "12:40", "Tus", "DE", "BS-19", "tut"],
               ["small", "Marat", "12:40", "Fri", "DE", "BS-19-01", "lab"],
               ["small", "Pavel", "9:00", "Tus", "FSE", "BS-19-01", "lab"],
               ["small", "Pavel", "12:40", "Fri", "FSE", "BS-19-02", "lab"],
               ["small", "Marat", "14:20", "Fri", "DE", "BS-19-02", "lab"]]

    def disp(A):
        for i in A:
            for j in i:
                print(j, end=" > ")
            print("")

    # check the oderd of lec > tut > lab
    def ok(A, cl, d, t):
        if cl[6] == "lec":
            return True
        elif cl[6] == "tut":
            for i in range(5):
                for j in range(8):
                    if d == i and j == t:
                        return False
                    for k in range(len(A[i][j])):
                        if A[i][j][k][6] == "lec" and A[i][j][k][4] == cl[4]:
                            return True
        else:
            for i in range(5):
                for j in range(8):
                    if d == i and j == t:
                        return False
                    for k in range(len(A[i][j])):
                        if A[i][j][k][6] == "tut" and A[i][j][k][4] == cl[4]:
                            return True
        return False

    def preferable(A, cl):
        if cl[6] == "lec" or cl[6] == "tut":
            for x in A[days_to_slot[cl[3]]][time_to_slots[cl[2]]]:
                if cl[5] in x or cl[1] in x:
                    return False
        else:
            for x in A[days_to_slot[cl[3]]][time_to_slots[cl[2]]]:
                if (cl[5] in x and cl[6] in x) or cl[1] in x:
                    return False
        return True

    def solve(ar, num, day, time):
        if time == 4:
            day += 1
            time = 0
        if num == len(Classes):
            disp(ar)
            print("")
            print(" >> ")
            print("")
            return
        if day == 3:
            day = 0
            time = 0
        # check if the preferable date is valid
        # print (Classes[num] ,Classes[num][3] , Classes[num][2])
        if preferable(ar, Classes[num]) and ok(ar, Classes[num], days_to_slot[Classes[num][3]],
                                               time_to_slots[Classes[num][2]]):
            ar[days_to_slot[Classes[num][3]]][time_to_slots[Classes[num][2]]].append(Classes[num])
            solve(ar, num + 1, day, time)
            return
        print(num)
        while not ok(ar, Classes[num], day, time):
            print(num, day, time)
            time += 1
            if time == 8:
                day += 1
                time = 0
            if day == 5:
                day = 0
                time = 0
        # put the date and time of the lectures in the as they are in the table
        Classes[num][3] = slot_to_day[day]
        Classes[num][2] = slot_to_time[time]
        ar[day][time].append(Classes[num])
        solve(ar, num + 1, day, time + 1)
        return

    solve(arr, 0, 0, 0)

    def print_to_file(year, group):
        with open(group + ".csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')

            # printing header
            writer.writerow(["Time slots", "Monday", "Teacher", "Room", "Tuesday", "Teacher", "Room",
                             "Wednesday", "Teacher", "Room",
                             "Thursday", "Teacher", "Room", "Friday", "Teacher", "Room"
                             ])

            # checking it the group for which we print schedule should attend the class
            def for_this_group(expected_year, expected_group, actual_group):
                return actual_group == expected_group or actual_group == expected_year

            for t in range(4):  # iterating over timeslots
                # adding timestamp
                timeslot = [slot_to_time[t]]
                for d in range(5):  # iterating over days
                    lecture = arr[d][t]
                    if len(lecture) == 0:  # if timeslot is empty - skip it
                        for i in range(3):
                            timeslot.append(None)
                        continue
                    group_is_free = True
                    for lec in lecture:
                        if for_this_group(year, group, lec[5]):
                            # add class name
                            timeslot.append(lec[4] + "(" + lec[6] + ")")
                            # add professor name
                            timeslot.append(lec[1])
                            # add room
                            timeslot.append(lec[0])
                            print(timeslot)
                            group_is_free = False
                    if group_is_free:
                        for i in range(3):
                            timeslot.append(None)
                writer.writerow(timeslot)

    # print_to_file("BS-19", "BS-19-01")
    # print_to_file("BS-19", "BS-19-02")
