from django.utils import timezone


def get_path_with_time_now(instance, filename):
    extension = ''
    stop = filename.rfind('.')

    if stop != -1:
        extension = filename[stop:]

    return '{0}/{1}'.format(type(instance).__name__,
                            timezone.now().strftime('%Y%m%d%H%M%S%f') + extension)
