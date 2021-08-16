from health_lab.models import Dept, Doctor


def menu_links(request):
    links=Dept.objects.all()
    # list =Doctor.objects.all()
    return dict(links=links)


