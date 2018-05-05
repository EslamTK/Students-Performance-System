import numpy as np
import pandas as pd

columns = ['sex', 'age', 'famsize', 'Pstatus', 'Medu', 'Fedu',
           'Mjob', 'Fjob', 'guardian', 'traveltime', 'studytime',
           'failures', 'famsup', 'paid', 'activities', 'higher',
           'internet', 'romantic', 'famrel', 'freetime', 'goout',
           'health', 'absences', 'midterm']

nominal_columns = ['sex', 'famsize', 'Pstatus', 'Mjob', 'Fjob', 'guardian', 'famsup',
                   'paid', 'activities', 'higher', 'internet', 'romantic']


def get_data_array(user, dataset_path):
    data = get_user_data_format(user)

    students = pd.read_csv(dataset_path)

    df = pd.DataFrame(data=data, columns=columns)
    students = students.append(df)

    dummy_df = pd.get_dummies(students[nominal_columns])
    students = pd.concat([students, dummy_df], axis=1)
    students = students.drop(nominal_columns, axis=1)

    midterm = students['midterm']
    students = students.drop(['midterm'], axis=1)
    students = students.assign(midterm=midterm)

    students = students[-len(user['courses']):]

    return np.array(students, dtype=np.float64)


def get_user_data_format(user):
    user_data = {'sex': [],
                 'age': [],
                 'famsize': [],
                 'Pstatus': [],
                 'Medu': [],
                 'Fedu': [],
                 'Mjob': [],
                 'Fjob': [],
                 'guardian': [],
                 'traveltime': [],
                 'studytime': [],
                 'failures': [],
                 'famsup': [],
                 'paid': [],
                 'activities': [],
                 'higher': [],
                 'internet': [],
                 'romantic': [],
                 'famrel': [],
                 'freetime': [],
                 'goout': [],
                 'health': [],
                 'absences': [],
                 'midterm': []}

    for i in user['courses']:
        user_data['sex'].append(user['sex'])
        user_data['age'].append(user['age'])
        user_data['famsize'].append(user['famsize'])
        user_data['Pstatus'].append(user['Pstatus'])
        user_data['Medu'].append(user['Medu'])
        user_data['Fedu'].append(user['Fedu'])
        user_data['Mjob'].append(user['Mjob'])
        user_data['Fjob'].append(user['Fjob'])
        user_data['guardian'].append(user['guardian'])
        user_data['traveltime'].append(user['traveltime'])
        user_data['activities'].append(user['activities'])
        user_data['higher'].append(user['higher'])
        user_data['internet'].append(user['internet'])
        user_data['romantic'].append(user['romantic'])
        user_data['famrel'].append(user['famrel'])
        user_data['freetime'].append(user['freetime'])
        user_data['goout'].append(user['goout'])
        user_data['health'].append(user['health'])
        user_data['studytime'].append(i['studytime'])
        user_data['failures'].append(i['failures'])
        user_data['absences'].append(i['absences'])
        user_data['famsup'].append(i['famsup'])
        user_data['paid'].append(i['paid'])
        user_data['midterm'].append((i['midterm']/100)*20)

    return user_data
