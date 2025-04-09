from django.views.generic import ListView
from .models import News

# Create your views here.


class BlogListView(ListView):
    model = News
    template_name = "home.html"
