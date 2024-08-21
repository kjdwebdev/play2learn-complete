from django.views.generic import TemplateView

# Create your views here.
# Home Page
class HomePageView(TemplateView):
    template_name = 'pages/home.html'

# About Us
class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'
