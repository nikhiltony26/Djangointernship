from django.shortcuts import render
from django.shortcuts import render
from faker import Faker
def task_page(request):
    dynamic_data = "Hello, dynamic world!"
    return render(request, 'task.html', {'dynamic_data': dynamic_data})


def task_page(request):
    fake = Faker()
    fake_data = {
        'name': fake.name(),
        'email': fake.email(),
        'sentence': fake.sentence(),
    }
    return render(request, 'task.html', {'fake_data': fake_data})




