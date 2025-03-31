from django.apps import AppConfig


class UsersprofileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usersprofile'

    def ready(self):
        import usersprofile.signals