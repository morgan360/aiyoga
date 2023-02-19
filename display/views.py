from django.shortcuts import render
from .models import YogaImage
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import ImageForm

@login_required
def slideshow(request):
    images = YogaImage.objects.all()
    return render(request, 'display/slideshow.html', {'images': images})


def image_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            yoga_image = form.cleaned_data['yoga_image']
            context = {'yoga_image': yoga_image}
            return render(request, 'display/image_form.html', context)
    else:
        form = ImageForm()
    return render(request, 'display/image_form.html', {'form': form})
