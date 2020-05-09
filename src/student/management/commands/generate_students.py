from django.core.management.base import BaseCommand, CommandError
from student.models import Student as student


class Command(BaseCommand):
    help = 'Generates N fake students'

    def add_arguments(self, parser):
        parser.add_argument('num_students', default = 100, nargs='+', type=int)

    def handle(self, *args, **options):
        num_students = options['num_students']
        print((num_students))
        for i in range(num_students[0]):
            student.generate_student()
        self.stdout.write(self.style.SUCCESS('Successfully generated  "%s" students' % num_students[0]))
