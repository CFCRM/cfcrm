from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import VerificationView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('ajax/cities/',views.load_cities,name = "ajax_load_cities"),
    path('ajax/addapplicant',views.add_applicants,name = "ajax_add_applicant"),
    path('ajax/subproducts/',views.load_subproducts,name = "ajax_load_subproducts"),
    path('', views.base_dashboard, name="base_dashboard"),
    path('homeloan/',include('HomeLoan.urls')),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('deleteapplicant/<int:id>',views.delapplicant,name = "deleteapplicant"),
    path('editapplicant',views.editapplicant,name = "edit_applicant"),

     path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="account/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name="account/password_reset_sent.html"),
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="account/password_reset_form.html"),
     name="password_reset_confirm"),

    path('reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name="account/password_reset_done.html"),
        name="password_reset_complete"),

    path('forgot_uname', views.forgot_uname, name="forgot_uname"),
    path('emailverificationmsg', views.email_ver_msg, name="email_ver_msg"),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name="activate"),
    path('uname_pw_gen', views.uname_pw_gen, name="uname_pw_gen"),

    path('add_leads', views.add_leads, name="add_leads"),
    path('create_mem', views.create_mem, name="create_mem"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('base', views.base, name="base"),
    path('list_leads', views.list_leads, name="list_leads"),
    path('terms.pdf', views.terms, name="termsandcondition"),
    path('additionaldetails/<int:id>', views.additionaldetails, name="additionaldetails"),
    path('housewife/<int:id>', views.housewife, name="housewife"),
    path('property_details/<int:id>', views.property_details, name="property_details"),
    path('property_type_1/<int:id>', views.property_type_1, name="property_type_1"),
    path('property_type_2/<int:id>', views.property_type_2, name="property_type_2"),
    path('property_type_3/<int:id>', views.property_type_3, name="property_type_3"),
    path('property_type_4/<int:id>', views.property_type_4, name="property_type_4"),
    path('add_applicant_additional_details/<int:id>',views.add_applicant_additional_details,name="add_applicant_additional_details"),
    path('add_individual_details/<int:id>',views.add_individual_details,name="individual_details"),
    path('retired/<int:id>', views.retired, name="retired"),
    path('salaried/<int:id>', views.salaried, name="salaried"),
    path('selfemployed', views.selfemployed, name="selfemployed"),
    path('student/<int:id>', views.student, name="student"),
    path('sidebar', views.sidebar, name="sidebar"),
    path('whatsapp', views.whatsapp, name="whatsapp"),
    path('email', views.email, name="email"),
    path('codes', views.codes, name="codes"),
    path('approved', views.approved, name="approved"),

    path('register2', views.register2, name="register2"),
    path('list_lead_edit/<int:id>', views.list_lead_edit, name="list_lead_edit"),
    path('list_lead_view/<int:id>', views.list_lead_view, name="list_lead_view"),
    path('list_lead_del/<int:id>', views.list_lead_del, name="list_lead_del"),
    path('customer_details', views.customer_details, name="customer_details"),
    path('partner_list', views.partner_list, name="partner_list"),
    path('partner_detailed_view/<int:id>', views.partner_detailed_view, name="partner_detailed_view"),
    path('partner_detail_edit/<int:id>', views.partner_detail_edit, name="partner_detail_edit"),
    path('training', views.training, name="training"),
    path('support', views.support, name="support"),

    path('bank_download', views.bank_download, name='bank_download'),
    path('calculator', views.calculator, name="calculator"),


]
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
