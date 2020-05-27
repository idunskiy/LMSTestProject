from django.core.management.base import BaseCommand, CommandError

from group.models import Group
from student.models import Student as student, Student


class Command(BaseCommand):
    help = 'Generates N fake students'

    def add_arguments(self, parser):
        parser.add_argument('num_students', default = 100, nargs='+', type=int)

    def handle(self, *args, **options):
        num_students = options['num_students']
        Student.objects.all().delete()
        groups = list(Group.objects.all())
        for i in range(num_students[0]):
            student.generate_student(groups)
        self.stdout.write(self.style.SUCCESS('Successfully generated  "%s" students' % num_students[0]))
