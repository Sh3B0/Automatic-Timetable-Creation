years = {year: index for year, index in zip(["B20", "B19", "B18", "B17", "M20", "M19"], list(range(6)))}

groups = [["B20-CE-01", "B20-CE-02", "B20-CE-03", "B20-CE-04", "B20-CS-01", "B20-CS-02"],
          ["B19-00-01", "B19-00-02", "B19-00-03", "B19-00-04", "B19-00-05", "B19-00-06"],
          ["B18-DS-01", "B18-DS-02", "B18-RO-01", "B18-SB-01", "B18-SE-01", "B18-SE-02"],
          ["B18-DS-01", "B18-DS-02", "B18-RO-01", "B18-SB-01", "B18-SE-01", "B18-SE-02"],
          ["B17-DS-01", "B17-DS-02", "B17-RO-01", "B17-SB-01", "B17-SE-01", "B17-SE-02"],
          ["M20-DS-01", "M20-RO-01", "M20-SE-01"],
          ["M19-DS-01", "M19-RO-01"]]

year_names = ["BS - Year 1 (Computer Engineering)", "BS - Year 1 (Computer Science)",
              "BS - Year 2", "BS - Year 3", "BS - Year 4", "MS - Year 1", "MS - Year 2"]

import pandas as pd

from pathlib import Path
cwd = Path(__file__).parent

def convert():
    df = pd.read_csv((cwd / "input.csv").resolve())

    # print full dataframe
    # with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    #     print(df)

    for index, row in df.iterrows():
        group = row['targets']
        if group.find('**') != -1:


            pass

    pass


if __name__ == "__main__":
    convert()
