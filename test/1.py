from Expressway.Dataset.Basic_Data import AboutData

path = 'E:/expressway project/Data/source_sichuan/基础数据/'
class_data = AboutData(file_path = [path + 'Road_S.shp'], get_pos = False)

a = []
b = []
c = []
num = []

for index, row in class_data.data[0].iterrows():

    LDJSDJ = row['LDJSDJ']
    b.append(row['LXBH'])

    if row['LXBH'] != None:
        num.append(row['LXBH'])

    if LDJSDJ == "1" or LDJSDJ == None:
        LXBH = row['LXBH']
        a.append(LXBH)

    if len(row['LXBH']) == 4 and row['LXBH'].startswith("S"):
        LXBH = row['LXBH']
        c.append(LXBH)
    else:
        print(row['LXBH'],row['LDJSDJ'])

print(len(a))
print(len(b))
print(len(c))
print(len(num))