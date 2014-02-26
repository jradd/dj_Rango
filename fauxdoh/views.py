from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse

from .forms import UploadPhotoForm
from .models import Photo, Profile


def list(request):
    """ File upload handler."""
    if request.method == "POST":
        form = UploadPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            newphoto = Photo(photofile = request.FILES['photofile'])
            newphoto.save()

            # Redirect the image list after `POST'.
            return HttpResponseRedirect(reverse('dj_Rango_blog.fauxdoh.views.list'))
    else:
        form = UploadPhotoForm() # A empty--unbound form.

    # Load photos for the list page.
    photos = Photo.objects.all()

    # Render list page with the photos and the form
    return render_to_response(request,
        '/fauxdoh/list.html',
        {"photo": photos, 'form': form},
        )

def index(request):
    if request.method == 'POST':
        form = UploadPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Photo(image_field=request.FILES['file'])
            instance.save()
            handle_uploaded_photo(request.FILES['file'])
            return HttpResponseRedirect('/success/url')
    else:
        form = UploadPhotoForm()
    return render(request, 'upload.html', {'form': form})
