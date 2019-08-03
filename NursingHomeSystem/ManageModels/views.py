from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,HttpResponse
def upload(request):
  if request.method == 'POST':
    name = request.POST.get('username')
    avatar = request.FILES.get('avatar')
    with open(avatar.name,'wb') as f:
      for line in avatar:
        f.write(line)
    return HttpResponse('ok')
  return render(request,'customer/info_add/upload.html')

def img(request):
  if request.method == 'POST':

   print(request.POST)
   return HttpResponse('ok')
