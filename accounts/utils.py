from django.contrib.auth.models import Group

def is_manager(user):
    return user.groups.filter(name='Manager').exists()

def is_editor(user):
    return user.groups.filter(name='Editor').exists()
