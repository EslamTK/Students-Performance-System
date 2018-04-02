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
        user_data['traveltime'].append(user['traveltime'])
        user_data['freetime'].append(user['freetime'])
        user_data['goout'].append(user['goout'])
        user_data['studytime'].append(i['studytime'])
        user_data['failures'].append(i['failures'])
        user_data['absences'].append(i['absences'])
        user_data['midterm'].append(i['midterm'])

    return user_data


def data_list(user):
    data = get_user_data_format(user)
    list = []
    for i in range(len(user['courses'])):
        tmp = []
        tmp.append(data['traveltime'][i])
        tmp.append(data['studytime'][i])
        tmp.append(data['freetime'][i])
        tmp.append(data['goout'][i])
        tmp.append(data['absences'][i])
        tmp.append(data['midterm'][i])
        list.append(tmp)
    return list
