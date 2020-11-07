# converter makes scheduler's output understandable to renderer


year_names_to_majors = {"BS - Year 1 (Computer Engineering)": ["B20-CE"],
                        "BS - Year 1 (Computer Science)": ["B20-CS"],
                        "BS - Year 2": ["B19-00"],
                        "BS - Year 3": ["B18-RO", "B18-DS", "B18-SE", "B18-SB"],
                        "BS - Year 4": ["B17-RO", "B17-DS", "B17-SE", "B17-SB"],
                        "MS - Year 1": ["M19-RO", "M19-DS", "M19-SE"],
                        "MS - Year 2": ["M20-RO", "M20-DS", "M20-SE"]
                        }
majors_to_year_names = {major: year_name
                        for year_name, majors in year_names_to_majors.items()
                        for major in majors
                        }

# tree-like DS for finding matching group names
targets = {
    "B17": {"DS": 2, "RO": 1, "SB": 1, "SE": 2},
    "B18": {"DS": 2, "RO": 1, "SB": 1, "SE": 2},
    "B19": {"00": 6},
    "B20": {"CE": 4, "CS": 2},
    "M19": {"DS": 1, "RO": 1},
    "M20": {"DS": 1, "RO": 1, "SE": 1},
}

# general patterns :
#   B18-**-**
#   B18-RO-**
#   B18-RO-**|B18-DS-**
#   B18-RO-01|B18-DS-**

# [day,slot,targets,a_name(a_type),a_inst,room] as header of dataframe

import pandas as pd

from pathlib import Path

cwd = Path(__file__).parent

def convert():
    df: pd.DataFrame = pd.read_csv((cwd / "../Scheduler/Output/Output.csv").resolve())

    # print full dataframe
    # with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    #     print(df)
    for index, row in df.iterrows():
        # delete these pesky brackets
        df.loc[index, 'targets'] = groups = str(row['targets'][1:-1])
        row = df.loc[index]

        # if several groups match this pattern
        if groups.find('**') != -1:
            # split group name into parts
            for group in groups.split('|'):
                year, major, number = group.split('-')
                # generate all group names and add the corresponding rows into DataFrame
                for major_name, group_quantity in targets[year].items():
                    # several groups may have the same activity at the same time
                    numbers = [f'0{group_number}' for group_number in range(1, group_quantity + 1)] \
                        if number == '**' else [number]
                    # several majors may match this pattern
                    if major == "**" or major == major_name:
                        for number in numbers:
                            new_row = row.copy()
                            new_row['targets'] = f'{year}-{major_name}-{number}'
                            df.loc[len(df)] = new_row.to_list()

    # just for debug
    special_slot = '9:00-10:30'
    df.loc[df['slot'] == special_slot, 'slot'] = '0' + special_slot
    df.sort_values(by=['targets', 'slot', 'day'], inplace=True)
    df.loc[df['slot'] == '0' + special_slot, 'slot'] = special_slot
    df = df[~df['targets'].str.contains('[*]')]

    # # print full dataframe
    # with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    #     print(df)


    # extract full group data into a dataframe
    columns = ["Monday", "Teacher1", "Room1",
               "Tuesday", "Teacher2", "Room2",
               "Wednesday", "Teacher3", "Room3",
               "Thursday", "Teacher4", "Room4",
               "Friday", "Teacher5", "Room5",
               "Saturday", "Teacher6", "Room6"]

    index = ["9:00-10:30", "10:40-12:10", "12:40-14:10", "14:20-15:50",
             "16:00-17:30", "17:40-19:10", "19:20-20:50"]

    for year_name, majors_groups in targets.items():
        for major_name, group_quantity in majors_groups.items():
            # create a dir based on year name and major
            path = cwd / Path(f"../data/groups_schedules/{majors_to_year_names[f'{year_name}-{major_name}']}")
            path.mkdir(parents=True, exist_ok=True)

            # list all group numbers
            group_names = [f'0{_}' for _ in range(1, group_quantity + 1)]
            for group_name in group_names:
                # target = f'{year_name}-{major_name}-{group_name}'
                target = df[df['targets'] == f"{year_name}-{major_name}-{group_name}"]
                group_data = pd.DataFrame(index=index, columns=columns)
                for _, row in target.iterrows():
                    entry_row = group_data.index.get_loc(row['slot'])
                    entry_column = group_data.columns.get_loc(row['day'])

                    activity, instructor_name, room = 'a_name(a_type)', 'a_inst', 'room'
                    group_data.iloc[entry_row, entry_column] = row[activity]
                    group_data.iloc[entry_row, entry_column + 1] = row[instructor_name]
                    group_data.iloc[entry_row, entry_column + 2] = row[room]

                group_data.to_csv((path / f"{year_name}-{group_name}.csv").resolve())


if __name__ == "__main__":
    convert()
