from math import ceil

import pandas as pd
from sklearn.neighbors import NearestNeighbors


def recommend(dataset, student):
    students = pd.read_csv(dataset)
    students.columns = ['school', 'sex', 'age', 'address', 'famsize', 'Pstatus',
                        'Medu', 'Fedu', 'Mjob', 'Fjob', 'reason', 'guardian',
                        'traveltime', 'studytime', 'failures', 'schoolsup', 'famsup',
                        'paid', 'activities', 'nursery', 'higher', 'internet',
                        'romantic', 'famrel', 'freetime', 'goout', 'Dalc', 'Walc',
                        'health', 'absences', 'G1', 'G2', 'G3']

    value = student
    # positions of these values in the dataset
    pos = students.ix[:, (12, 13, 24, 25, 29, 31)].values
    k = 100
    nbrs = NearestNeighbors(n_neighbors=k).fit(pos)

    A, B = nbrs.kneighbors([value])

    myList = students.iloc[B[0], [12, 13, 24, 25, 29, 31]]

    myList['distance'] = A[0]

    df1 = myList[myList['traveltime'] <= value[0]]
    df2 = df1[df1['studytime'] > value[1]]
    df3 = df2[df2['freetime'] > value[2]]
    df4 = df3[df3['goout'] >= value[3]]
    df5 = df4[df4['absences'] <= value[4]]
    df6 = df5[df5['G2'] > value[5]]

    # handling the special case of empty frame------------------------------------------------------------
    list2 = list()
    list3 = list()

    if df6.empty:

        # print('DataFrame is empty!')
        item1 = value[0] - ceil(0.5 * value[0])
        if item1 < 0: item1 = 0
        list3.append(abs(item1))
        item2 = abs(value[1] + ceil(0.5 * value[1]))
        if item2 >= 4: item2 = 4 - value[1]
        list3.append(item2)
        item3 = abs(value[2] + ceil(0.5 * value[2]))
        if item3 >= 5: item3 = 5 - value[2]
        list3.append(item3)
        item4 = abs(value[3] + ceil(0.5 * value[3]))
        if item4 >= 5: item4 = 5 - value[3]
        list3.append(item4)
        item5 = abs(value[4] - ceil(0.5 * value[4]))
        if item5 >= 75: item5 = 75 - value[4]
        list3.append(item5)

        list2 = list3


    else:
        df7 = df6.loc[df6['distance'].idxmax()]
        for i in range(0, 5):
            list2.append(abs(df7[i] - value[i]))
    list3 = {}
    if list2[0] > 0:
        list3['traveltime'] = str(int(list2[0]))

    if list2[1] > 0:
        list3['studytime'] = str(int(list2[1]))

    if list2[2] > 0:
        list3['freetime'] = str(int(list2[2]))

    if list2[3] > 0:
        list3['goout'] = str(int(list2[3]))

    if list2[4] > 0:
        list3['absences'] = str(int(list2[4]))

    return list3
