from .utils import is_manager, is_editor


def user_roles(request):
    """
    Add user role flags to all templates
    """
    if request.user.is_authenticated:
        return {
            'is_manager': is_manager(request.user),
            'is_editor': is_editor(request.user),
        }
    return {}