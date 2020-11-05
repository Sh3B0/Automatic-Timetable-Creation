# Maps Allocation tuple (day, slot, room) to [0="free", 1="taken"]
taken = {}

# Gets activity object by ID
activity_by_id = {}

# Converting numbers to human readable info
day_to_str = {0: "None", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday"}
type_to_str = {0: "None", 1: "Lec", 2: "Tut", 3: "Lab"}
slot_to_str = {0: "None", 1: "9:00-10:30", 2: "10:40-12:10", 3: "12:40-14:10", 4: "14:20-15:50", 5: "16:00-17:30",
               6: "17:40-19:10", 7: "19:20-20:50"}

# For each category, gives (base column, grp_size)
grp_cnt = {
    ('B20', '**'): (2, 6), ('B19', '00'): (8, 6),
    ('B18', '**'): (14, 6), ('B17', '**'): (20, 6),
    ('M19', '**'): (30, 4), ('M20', '**'): (26, 4),
    ('B20', 'CE'): (2, 4), ('B20', 'CS'): (6, 2),
    ('B18', 'DS'): (14, 2), ('B17', 'DS'): (20, 2),
    ('B18', 'SE'): (16, 2), ('B17', 'SE'): (22, 2),
    ('B18', 'SB'): (18, 1), ('B17', 'SB'): (24, 1),
    ('B18', 'RO'): (19, 1), ('B17', 'RO'): (25, 1),
    ('M19', 'DS'): (30, 1), ('M20', 'DS'): (26, 1),
    ('M19', 'SE'): (31, 1), ('M20', 'SE'): (27, 1),
    ('M19', 'SB'): (32, 1), ('M20', 'SB'): (28, 1),
    ('M19', 'RO'): (33, 1), ('M20', 'RO'): (29, 1),
}

# For table colors hex values
colors = {"B20": "DB4437", "B19": "F4B400", "B18": "0F9D58", "B17": "4285F4", "M20": "7F00FF", "M19": "FFC0CB"}

# big_rooms are used for lectures and tutorials, small rooms are used for labs
big_rooms = [108, 107, 106, 105, 321, 306]
small_rooms = [101, 102, 103, 104, 300, 301, 302, 303, 304, 305, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317,
               318, 319, 320]

from pathlib import Path

cwd = Path(__file__).parent
