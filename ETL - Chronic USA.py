import pandas as pd

#df = pd.read_csv(r'U.S._Chronic_Disease_Indicators__CDI_.csv')
#print(df.columns)

info = []

with open("latlong.txt") as f:
    contents = f.read().split('\n')
    for line in contents:
        if line != "":
            line = line.split(',')[3:]
            if len(line) > 3:
                line = [line[0], line[2], line[3]]
                info.append(','.join(line))

print(info)