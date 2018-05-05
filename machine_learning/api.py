from os import path

from .prediction.data_format import get_data_array
from .prediction.neural_network import get_prediction
from .recommendation.data_format_rec import data_list
from .recommendation.recommend import recommend

site_root = path.realpath(path.dirname(__file__)) + '/'
format_dataset_path = path.join(site_root, 'static/prediction', 'format_dataset.csv')
learning_dataset_path = path.join(site_root, 'static/prediction', 'learning_dataset.csv')
dataset_path = path.dirname(path.abspath(__file__)) + '/static/recommendation/Dataset-Original.csv'


def prediction(student_data):
    result = get_prediction(get_data_array(student_data, format_dataset_path), learning_dataset_path)

    courses = {
        'courses': []
    }

    for i in range(len(student_data['courses'])):

        course = {
            'id': student_data['courses'][i]['id'],
            'prediction': int((result[i]/20)*100),
            'name': student_data['courses'][i]['name'],
            'midterm': student_data['courses'][i]['midterm']
        }
        courses['courses'].append(course)

    return courses


def recommendation(student_data):
    data = data_list(student_data)

    result, student = [], []

    for i in range(len(data)):
        student = data[i]
        result.append(recommend(dataset_path, student))

    courses = {
        'general_recommendations': [],
        'courses': [],
    }

    general_recommendation = []

    if len(result) > 0:
        if 'traveltime' in result[0]:
            general_recommendation.append('Decrease your travel time by ' + str(result[0]['traveltime'])
                                          + ' hours')

        if 'freetime' in result[0]:
            general_recommendation.append('Increase your free time by ' + str(result[0]['freetime']) + ' hours')

        if 'goout' in result[0]:
            general_recommendation.append('Increase your go out time  by ' + str(result[0]['goout']) + ' hours')

    courses['general_recommendations'].append(general_recommendation)

    for i in range(len(student_data['courses'])):

        course = {
            'id': student_data['courses'][i]['id'],
            'name': student_data['courses'][i]['name'],
            'recommendations': []
        }

        if 'studytime' in result[i]:
            course['recommendations'].append('Increase your study time by ' + str(result[i]['studytime']) +
                                             ' hours')

        if 'absences' in result[i]:
            course['recommendations'].append('Decrease your absences')

        courses['courses'].append(course)

    return courses
