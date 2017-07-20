from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User, Group

def deanery_auth(user):
    if user:
        if user.is_authenticated():
            print('deanery')
            return user.groups.filter(name='Deanery').exists()
    print('not deanery')
    return False


def student_auth(user):
    if user:
        if user.is_authenticated():
            return Group.objects.get(user=user) in user.groups.all()
    return False


def is_deanery(fn=None):
    decorator = user_passes_test(deanery_auth)
    if fn:
        return decorator(fn)
    return decorator


def is_student(fn=None):
    decorator = user_passes_test(student_auth)
    if fn:
        return decorator(fn)
    return decorator
