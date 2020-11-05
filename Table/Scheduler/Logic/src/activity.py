from Table.Scheduler.Logic.src.globals import *

global_id = 0


# Main class for activities
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

    # a list of targeted students, element regex=(([BM]\d\d), (CE|CS|SE|RO|SB|DS|\*), (\d\d|\*))
    targets = []

    # tuple(day, slot, room): zeros mean that the activity is unallocated
    alloc = (0, 0, 0)

    def __init__(self, a_name='', a_inst='', a_type=-1, targets=None, refers_to=None):
        if targets is None:
            targets = []
        self.a_name = a_name
        self.a_inst = a_inst
        self.a_type = a_type
        self.targets = targets
        self.refers_to = refers_to
        global global_id
        activity_by_id[global_id] = self
        global_id += 1

    def __str__(self):
        res = day_to_str[self.alloc[0]] + "," + slot_to_str[self.alloc[1]]
        res += ',['
        for t in self.targets:
            res += t[0] + '-' + t[1] + '-' + t[2] + '|'
        res = res[:-1] + ']'
        res += "," + self.a_name + "(" + type_to_str[self.a_type] + ")," + self.a_inst + "," + str(self.alloc[2])
        return res

    def __lt__(self, other):
        if self.a_name == other.a_name:
            return self.a_type < other.a_type
        else:
            return self.a_name < other.a_name

    def pretty_print(self):
        print("Name:", self.a_name, "\nType:", type_to_str[self.a_type],
              "\nInstructor:", self.a_inst, "\nTarget:", self.targets, "Refers To: [\n", self.refers_to, '\n]')
        if self.alloc != (0, 0, 0):
            print("Currently allocated in: ", day_to_str[self.alloc[0]], slot_to_str[self.alloc[1]], self.alloc[2])
