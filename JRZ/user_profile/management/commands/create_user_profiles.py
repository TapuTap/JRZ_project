from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from user_profile.models import Profile
from hr_system.models import Employee

User = get_user_model()

class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> str | None:
        empl_obj_without_profile = Employee.objects.filter(employee_profile__isnull=True)
        user_without_profile = User.objects.filter(profile__isnull=True)
        empl_obj_with_profile = Employee.objects.all()
        created_profile_count = 0
        try:
            for empl_obj in empl_obj_without_profile:
                user = User.objects.create(
                    username=empl_obj.f_name[0] + empl_obj.l_name,
                    email=empl_obj.email,
                    first_name=empl_obj.f_name,
                    last_name=empl_obj.l_name
                    )
                user.set_password(empl_obj.l_name)
                user.save()

                profile = Profile(user=user, employee=empl_obj)
                profile.save()
                
                created_profile_count += 1
        except Exception as e:
            raise CommandError(e)
        else:
            self.stdout.write(
                self.style.SUCCESS('%d user profiles created' % created_profile_count)
            )