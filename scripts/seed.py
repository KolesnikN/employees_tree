from django_seed import Seed
from faker import Faker
import random
from tree.models import Employees

def first_rec():
    e = Employees(
        name='',
        position='Генеральный директор',
        emp_date='2012-04-11',
        salary='4000'
    )
    e.save()

def fill_emp(count, pos, year, salary, parent_min, parent_max):
    seeder = Seed.seeder()
    fake = Faker('ru_RU')
    with Employees.objects.disable_mptt_updates():
        seeder.add_entity(Employees, count, {
            'name': lambda x: fake.name(),
            'position': pos,
            'emp_date': '{}-{}-{}'.format(year, random.randint(1, 12), random.randint(1, 28)),
            'salary': lambda x: random.randint(salary+800, salary+4000),
            'parent': lambda x: Employees.objects.get(id=random.randint(parent_min, parent_max)),
        })
        seeder.execute()

def del_obj():
    with Employees.objects.disable_mptt_updates():
        objs = Employees.objects.all()
        objs.delete()
    Employees.objects.rebuild()

def run():
    first_rec()
    fill_emp(10, 'Топ менеджер', 2011, 3400, 1, 1)
    fill_emp(100, 'Продакт менеджер', 2013, 2400, 2, 11)
    fill_emp(1000, 'Синьёр', 2015, 1600, 12, 111)
    fill_emp(40000, 'Миддл', 2019, 1200, 112, 1111)
    fill_emp(10000, 'Джун', 2020, 1000, 1112, 41111)
    Employees.objects.rebuild()
    pass
