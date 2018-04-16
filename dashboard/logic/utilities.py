def convert_boolean_to_yes_no(value):
    if value:
        return 'yes'
    return 'no'


def item_not_found_message(item):
    return 'No {0} found with the given {0} id.'.format(item)
