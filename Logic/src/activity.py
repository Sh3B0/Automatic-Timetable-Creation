from globals import *

global_id = 0


class Activity:
    # activity name
    a_name = ''

    # activity instructor
    a_inst = ''

    # 1 for lec, 2 for tut, 3 for lab
    a_type = -1

    # ID of another activity
    # If activity is lab, it should refer to tut, if activity is tut, it should refer to lec
    refers_to = -1

    # targeted students, regex=(([BM]\d\d), (CE|CS|SE|RO|SB|DS|\*), (\d\d|\*))
    target = ('', '', '')

    # tuple(day, slot, room): zeros mean that the activity is unallocated
    alloc = (0, 0, 0)

    def __init__(self, a_name='', a_inst='', a_type=-1, target=None, refers_to=None):
        self.a_name = a_name
        self.a_inst = a_inst
        self.a_type = a_type
        self.target = target
        self.refers_to = refers_to
        global global_id
        activity_by_id[global_id] = self
        global_id += 1

    def __str__(self):
        return day_to_str[self.alloc[0]] + "," + slot_to_str[self.alloc[1]] + "," + self.target[0] + '-' + \
               self.target[1] + '-' + self.target[2] + "," + self.a_name + "(" + type_to_str[self.a_type] + \
               ")," + self.a_inst + "," + str(self.alloc[2])

    def __lt__(self, other):
        if self.a_name == other.a_name:
            return self.a_type < other.a_type
        else:
            return self.a_name < other.a_name

    def prettyPrint(self):
        print("Name:", self.a_name, "\nType:", type_to_str[self.a_type],
              "\nInstructor:", self.a_inst, "\nTarget:", self.target, "Refers To: [\n", self.refers_to, '\n]')
        if self.alloc != (0, 0, 0):
            print("Currently allocated in: ", day_to_str[self.alloc[0]], slot_to_str[self.alloc[1]], self.alloc[2])
