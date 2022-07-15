from django.conf import settings

class AppRouter:

    def db_for_read(self, model, **hints):
        """
        Attempts to read user models go to DB1.
        """
        if model._meta.app_label in ['app_db_routing','app_db_serializer','app_db_querysets','app_db_custom_sql']:
            return 'DB1'

        return None 

    def db_for_write(self, model, **hints):
        """
        Attempts to write user models go to DB1.
        """
        if model._meta.app_label in ['app_db_routing','app_db_serializer','app_db_querysets','app_db_custom_sql']:
            return 'DB1'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the user app is involved.
        """
        if obj1._meta.app_label in ['app_db_routing','app_db_serializer','app_db_querysets','app_db_custom_sql'] or \
           obj2._meta.app_label in ['app_db_routing','app_db_serializer','app_db_querysets','app_db_custom_sql']:
           return True

        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth app only appears in the 'DB1'
        database.
        """
        if app_label in ['app_db_routing','app_db_serializer','app_db_querysets','app_db_custom_sql']:
            # return db == 'DB1'
            return 'DB1'
        return None