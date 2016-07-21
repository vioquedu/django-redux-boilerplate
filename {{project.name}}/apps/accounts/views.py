
import datetime

# Django imports
from django.contrib.auth.models import Group
from rest_framework import permissions

# Local imports
from config.settings import JWT_AUTH

# Create your views here.
def jwt_payload_handler(user):
    """Defines payload to be stored in JWT passed to the client.
    """
    return {
        'user_id': user.id,
        'email': user.email,
        'username': user.get_username(),
        'groups' : list(user.groups.all().values_list('name', flat=True)),
        'exp': datetime.datetime.utcnow() + JWT_AUTH['JWT_EXPIRATION_DELTA'],  }
    
def is_in_group(user, group_name):
    """Takes a user and a group name, and returns `True` if the user is in that group.        
    """
    return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()


class HasGroupPermission(permissions.BasePermission):
    """Ensure user is in required groups.
    """
    def has_permission(self, request, view):
        # Get a mapping of methods -> required group.
        required_groups_mapping = getattr(view, 'required_groups', {})

        # Determine the required groups for this particular request method.
        required_groups = required_groups_mapping.get(request.method, [])

        # Return True if the user has all the required groups.
        return all([is_in_group(request.user, group_name) for group_name in required_groups])
