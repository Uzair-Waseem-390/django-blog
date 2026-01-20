from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied

def manager_required(view_func):
    def check_manager(user):
        if user.is_authenticated and user.groups.filter(name='Manager').exists():
            return True
        raise PermissionDenied

    return user_passes_test(check_manager)(view_func)

def editor_required(view_func):
    def check_editor(user):
        if user.is_authenticated and user.groups.filter(name='Editor').exists():
            return True
        raise PermissionDenied

    return user_passes_test(check_editor)(view_func)


def manager_or_editor_required(view_func):
    def check_manager_or_editor(user):
        if user.is_authenticated:
            # Check if user is in Manager OR Editor group
            if user.groups.filter(name__in=['Manager', 'Editor']).exists():
                return True
        raise PermissionDenied
    
    return user_passes_test(check_manager_or_editor)(view_func)