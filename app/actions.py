from django.contrib.auth.models import User, ContentType, Group, Permission
from objectpack.actions import ObjectPack
from objectpack.ui import ModelEditWindow

from . import controller
from .ui import UserAddWindow


class UserObjectPack(ObjectPack):
    """
    ObjectPack для модели User
    """

    model = User
    add_to_desktop = True
    add_to_menu = True
    add_window = edit_window = UserAddWindow


class ContentTypeObjectPack(ObjectPack):
    """
    ObjectPack для модели ContentType
    """

    model = ContentType
    add_to_desktop = True
    add_to_menu = True
    add_window = edit_window = ModelEditWindow.fabricate(model=ContentType)


class GroupObjectPack(ObjectPack):
    """
    ObjectPack для модели Group
    """

    model = Group
    add_to_desktop = True
    add_to_menu = True
    add_window = edit_window = ModelEditWindow.fabricate(model=Group)


class PermissionObjectPack(ObjectPack):
    """
    ObjectPack для модели Permission
    """
    model = Permission
    add_to_desktop = True
    add_to_menu = True
    add_window = edit_window = ModelEditWindow.fabricate(model=Permission, model_register=controller.observer)
