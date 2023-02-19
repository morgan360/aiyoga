# views.py
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Poses
from .forms import PoseForm, PoseSelectForm, PoseSelectForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


@login_required
def pose_list(request):
    poses = Poses.objects.all()
    paginator = Paginator(poses, 10)  # paginate the data with 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    count = Poses.objects.count()
    return render(request, 'poses/pose_list.html', {'page_obj': page_obj, 'count': count})


@login_required
def pose_edit(request, pk):
    pose = get_object_or_404(Poses, pk=pk)
    if request.method == 'POST':
        form = PoseForm(request.POST, instance=pose)
        if form.is_valid():
            form.save()
            return redirect('pose_list')
    else:
        form = PoseForm(instance=pose)
    return render(request, 'poses/pose_edit.html', {'form': form})


@login_required
def pose_new(request):
    if request.method == 'POST':
        form = PoseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pose_list')
    else:
        form = PoseForm()
    return render(request, 'poses/pose_edit.html', {'form': form})


def pose_select(request):
    if request.method == 'POST':
        form = PoseSelectForm(request.POST)
        if form.is_valid():
            pose = form.cleaned_data['pose_data']
            context = {'pose_data': pose}
            return render(request, 'poses/pose_select_form.html', context)
    else:
        form = PoseSelectForm()
    return render(request, 'poses/pose_select_form.html', {'form': form})