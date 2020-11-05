from Table.Scheduler.Logic.src.globals import *


def disjoint(a, b):
    """
    :param a: 1st target list
    :param b: 2nd target list
    :return: True if given two lists are disjoint, false otherwise
    """
    for t1 in a:
        for t2 in b:
            if t1[0] == t2[0]:
                if (t1[1] == '**' or t2[1] == '**') and t1[0] != 'B19':
                    return False
                elif t1[1] == t2[1]:
                    if t1[2] == '**' or t2[2] == '**':
                        return False
                    elif t1[2] == t2[2]:
                        return False
    return True


def allocate_room(ac, p, day, slot):
    if ac.a_type == 2:
        for room in big_rooms:
            if not taken.get((day, slot, room)):
                p.append((day, slot, room))
    else:
        for room in small_rooms:
            if not taken.get((day, slot, room)):
                p.append((day, slot, room))


def generate(activities):
    """
    Implements 1st phase of the algorithm: generate a list (p) of potential allocations for activity ac.
        Constraints (for now):
            No two activities at the same exact allocation (day, time, room)
            Order Lec, Tut, Lab should be maintained
    :param activities: given list of activities to schedule
    :return: True on success
    """

    for ac in activities:
        # print("Renderer activity " + ac.a_inst)

        p = []

        # If ac is a lecture, check any free slot to add to list
        # Preferable to have lectures in different days, then slots, then rooms
        if ac.a_type == 1:
            for slot in range(1, 8):
                for room in big_rooms:
                    for day in range(1, 6):
                        if not taken.get((day, slot, room)):
                            p.append((day, slot, room))

        # Activity is tut or lab, assert dependencies
        # Preferable to have the lab in same day as tut, and tut in same day as lec
        # Late slots (latest 3) has Lower priority
        # Lowest priority: labs on next week
        else:
            s_day = activity_by_id[ac.refers_to].alloc[0]
            s_slot = activity_by_id[ac.refers_to].alloc[1] + 1
            # print(" at " + str(s_day) + ", " + str(s_slot))
            for day in range(s_day, 6):
                if day != s_day:
                    s_slot = 1
                for slot in range(s_slot, 5):
                    allocate_room(ac, p, day, slot)

            for day in range(s_day, 6):
                for slot in range(5, 8):
                    allocate_room(ac, p, day, slot)

            for day in range(1, s_day):
                for slot in range(1, 8):
                    allocate_room(ac, p, day, slot)

        if not p:
            print("Not enough slots!")
            return False

        # print("Activity " + ac.a_inst + "can be placed in one of the following:")
        # for ac in p:
        #    print(ac)

        conflicts(activities, ac, p)
    return True


def conflicts(activities, ac, p):
    """
    Implements 2nd phase of the algorithm, collect/count conflicts if ac is placed in each slot from p.
        If there is a (p) with 0 conflicts, immediately place ac there and return
        Otherwise
            Choose the (p) with smallest number of conflicts and place ac there
            Un-allocate conflicting events
            Recursively try to allocate the unallocated events (avoid cycles and TLE)
    :param activities: given list of activities to schedule
    :param ac: the new activity to be allocated
    :param p: a list of potential allocations for ac
    :return: True on success
    """
    for t in p:
        ac.alloc = t
        con = []
        for j in activities:
            # Excluding cases where conflicts cannot happen
            if ac == j or j.alloc == (0, 0, 0) or (ac.a_inst != j.a_inst and disjoint(ac.targets, j.targets)):
                continue

            # Both activities have the same instructor but different targets
            # Day, slot cannot be the same, room can be
            # ac, j are preferably be in different days
            elif ac.a_inst == j.a_inst and disjoint(ac.targets, j.targets):
                if ac.alloc[0] == j.alloc[0] and ac.alloc[1] == j.alloc[1]:
                    if ac.alloc[2] == j.alloc[2]:
                        con.append((j, 4))
                    else:
                        con.append((j, 1))

            # Both activities have the same targets but different instructors
            # Day, slot cannot be the same, room can be
            elif ac.a_inst != j.a_inst and (disjoint(ac.targets, j.targets) is False):
                if ac.alloc[0] == j.alloc[0] and ac.alloc[1] == j.alloc[1]:
                    if ac.alloc[2] == j.alloc[2]:
                        con.append((j, 4))
                    else:
                        con.append((j, 2))

            # Both activities have the same targets and same instructor (Extremely rare to happen with labs)
            # Day, slot cannot be the same, room can be
            elif ac.a_inst == j.a_inst and (disjoint(ac.targets, j.targets) is False):
                if ac.alloc[0] == j.alloc[0] and ac.alloc[1] == j.alloc[1]:
                    if ac.alloc[2] == j.alloc[2]:
                        con.append((j, 4))
                    else:
                        con.append((j, 3))

        if not con:
            # print("Placing " + str(ac) + " in " + str(t))
            # if t in taken:
            # print("Lol, you missed a conflict, " + ac.a_inst)
            taken[t] = True
            return True

        # print("Placing " + ac.a_inst + " in " + str(t) + " generated the following conflicts:")
        # for tmp in con:
        #    print("\t" + tmp[0].a_inst + str(tmp[0].alloc) + ", " + str(tmp[1]))

    # TODO: implement phase 3 of the algorithm
    # If we're here, it means that ac cannot be placed anywhere without generating at least one conflict
    print("Can't place " + ac + " without generating a conflict or more")
    return False
