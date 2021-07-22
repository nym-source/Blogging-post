from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, reverse
from .forms import SignUpForm, postFORMS
from .models import Post
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

def postVIEW(request):
  if request.method == 'POST':
    form = postFORMS(request.POST, request.FILES)
    if form.is_valid():
      new_req = Post(User_Name = request.user, Title=request.POST['title'], Summary=request.POST['summary'], Content=request.POST['content'],Category=request.POST['category'], Image=request.FILES['image'],)
      new_req.save()
      return HttpResponseRedirect(reverse('draft'))

  else:
    form = postFORMS()
  
  htmlcode = True
  context = {'form': form}
  return render(request,'post.html', context)


def draftVIEW(request):
  All_POSTS = Post.objects.all().filter(User_Name=request.user).order_by('-id')
  return render(request, 'draft.html', {'post': All_POSTS})


def mypostSVIEW(request):
  All_POST = Post.objects.all().filter(User_Name=request.user).order_by('-id')
  return render(request, 'accountPOST.html', {'posts': All_POST})


def listVIEW(request):
  All_POSTS = Post.objects.all().order_by('-id')
  return render(request, 'list.html', {'post': All_POSTS})


def detailsVIEW(request,id):
  POSTs_key = Post.objects.filter(id=id)
  return render(request, 'details.html', {'post': POSTs_key})


class updateVIEW(UpdateView):
  model = Post
  template_name = 'draftdetails.html'
  fields = ['Publised']
  success_url = reverse_lazy('list')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
          user = form.save()
          user.refresh_from_db()  # load the profile instance created by the signal request.FILES['Images']
          user.profile.profile_PIC = request.FILES['profile_PIC']
          user.profile.Full_Address = form.cleaned_data.get('address')
          user.profile.Category = form.cleaned_data.get('Category')
          user.profile.city = form.cleaned_data.get('city')
          user.profile.state = form.cleaned_data.get('state')
          user.profile.pincode = form.cleaned_data.get('pincode')
          user.save()
          raw_password = form.cleaned_data.get('password1')
          user = authenticate(username=user.username, password=raw_password)
          login(request, user)
          return HttpResponseRedirect(reverse('list'))
    else:
      form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
