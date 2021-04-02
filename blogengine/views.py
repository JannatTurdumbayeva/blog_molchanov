from django.http import HttpResponse

def redirect_blog(request):
    return redirect('posts_list_url', permanent=True)