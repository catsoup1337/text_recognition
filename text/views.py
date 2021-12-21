from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ImageForm, SearchForm
from django.shortcuts import get_object_or_404
from taggit.models import Tag
from .models import Image
from . import image_operator1 as operator

def image_upload_view(request, search = None):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        form_search = SearchForm(request.POST)
        if form_search.is_valid():
            search = form_search.cleaned_data['search']
            return HttpResponseRedirect(f'/tag/{search}/')
        if form.is_valid():
            form.save()
            img_obj = form.instance
            image = img_obj.image.url
            result = operator.main(image=image)
            for n in range(len(result)):
                img_obj.tags.add(result[n])
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj, 'result': result,})
    else:
        form_search = SearchForm()
        form = ImageForm()
    return render(request, 'index.html', {'form': form})


def tag(request, tag_slug=None):
    """Searching for upload images"""
    imgs = Image.objects.all()
    tag = None
    if tag_slug:
        try:
            tag = get_object_or_404(Tag, slug=tag_slug)
            object_list = imgs.filter(tags__in=[tag])
            return render(request, 'tag.html', {'imgs': object_list})
        except:
            return render(request, 'not_found.html')