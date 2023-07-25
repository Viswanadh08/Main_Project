from django.shortcuts import render,
redirect from django.contrib import messages
from sentimentapp.models import UserModel
from django.core.paginator import Paginator

# Create your views here.

def admin_login(request):

  if request.method == &#39;POST&#39;:
    name = request.POST.get(&#39;name&#39;)
    password = request.POST.get(&#39;password&#39;)
    print(name,password)

  if name == &#39;admin&#39; and password == &#39;admin&#39;:
    print(name, &#39;rrrrrrrrrrrrr&#39;,password)
    messages.success(request,&#39;Admin login successfully&#39;)
    return redirect(&#39;dashboard&#39;)

  else:
    messages.error(request,&#39;Wrong name and
    password&#39;) return redirect(&#39;admin_login&#39;)

return render(request, &#39;admin/login.html&#39;)

def dashboard(request):
  pending =  UserModel.objects.filter(status=&#39;pending&#39;).count() all = UserModel.objects.all().count()
  context={
  &#39;pending&#39;:pending,
  &#39;all&#39;:all

  }
return render(request, &#39;admin/index.html&#39;, context)

def accept_user(request,id):
  users = UserModel.objects.get(user_id=id)
  users.status = &#39;Accept&#39;
  users.save(update_fields=[&#39;status&#39;])
  users.save()
  messages.success(request,&#39;New user add successfully&#39;)
  return redirect(&#39;pending-users&#39;)

def reject_user(request,id):
  user = UserModel.objects.get(user_id=id)
  user.delete()
  messages.success(request,&#39;user rejected successfully &#39;)
  return redirect(&#39;pending-users&#39;)
def all_users(request):

  all_users =
  UserModel.objects.filter(status=&#39;Accept&#39;)
  paginater = Paginator(all_users,4)
  page_number = request.GET.get(&#39;page&#39;)
  number_of_pages = paginater.get_page(page_number)
  
  context = {
  &#39;users&#39;:number_of_pages
  }
  return render(request, &#39;admin/all-users.html&#39;, context)

def delete(request,id):
  user = UserModel.objects.get(user_id=id)
  user.delete()
  messages.success(request,&#39;user delete successfully&#39;)
  return redirect(&#39;all-users&#39;)

def logout(request):
  messages.success(request,&#39;Admin logout successfully&#39;)
  return redirect(&#39;home&#39;)
