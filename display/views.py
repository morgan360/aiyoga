from django.shortcuts import render
from .models import YogaImage
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


@login_required
def slideshow(request):
    images = YogaImage.objects.all()
    return render(request, 'display/slideshow.html', {'images': images})
