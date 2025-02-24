from . import views
from django.urls import path, re_path

urlpatterns = [
    path("", views.HomeView.as_view(), name='home_url'),
    path("aboutus/", views.AboutUsView.as_view(), name='about_us_url'),
    path("help/", views.HelpView.as_view(), name='help_url'),
    path("faq/", views.FAQView.as_view(), name='faq_url'),
    path("help/identify/", views.identify_guides, name='identify_guides_url'),
    path("help/explore/", views.explore_guides, name='explore_guides_url'),
    path("help/support/", views.support_guides, name='support_guides_url'),
    path("help/blog/", views.blog_guides, name='blog_guides_url'),
    path("help/medicinal/", views.medicine_guides, name='medicine_guides_url'),
    path("help/growth/", views.growth_guides, name='growth_guides_url'),
    path("Oops/", views.updating_error, name='updating_err_url'),
    path("Soon/", views.implement_soon_error, name='soon_err'),
    path("404/", views.not_found_error, name='404_err'),
    re_path("users/*", views.DashboardView.as_view(), name='dashboard_url'),

]
