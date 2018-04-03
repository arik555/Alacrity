import string
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
# import requests
from django.core.mail import send_mail
from django.conf import settings
from .forms import MyUserForm, MyEventForm, MyGroupForm, MyContactForm
from .models import Event, MyUser, MyGroup
# Create your views here.

def index_page(request):
    my_dict = {}
    return render(request, 'index.html', context=my_dict)


def ala_index_page(request):
    form = MyContactForm()

    if request.method == 'POST':
        form = MyContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['c_name']
            email = form.cleaned_data['c_email']
            print(email)
            msg = form.cleaned_data['c_message']
            # send_mail(subject, message, from_email, to_list_emails)
            subject = name +" - tried to contact you."
            message = msg
            from_email = email
            to_list_emails = [settings.EMAIL_HOST_USER, ]
            send_mail(subject, message, from_email, to_list_emails, fail_silently=False)
            return HttpResponse("<script>alert('Thank You for contacting us. We'll get in touch soon.'); window.location.assign('/main_page/');</script>")

    my_dict = {'form': form, }
    return render(request, 'alacrity.html', context=my_dict)



'''
def index_page(request):
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
    response = requests.get('http://freegeoip.net/json/%s' %ip_address)
    geodata = response.json()
    userdata = MyUser.objects.all()
    evedata = Event.objects.all()
    my_dict = {'temp1': userdata, 'temp2': evedata,'ip': geodata['ip'],
    'country': geodata['country_name'],
    'lat': geodata['latitude'],
    'long': geodata['longitude'],
    'api_key': 'BIzaSyAgtwFB4G-1_Nq_oiurPlRBz00O9_jBk6Q',
    'address': geodata['region_name'] + ', ' + geodata['city'] + ' - ' + geodata['zip_code'] + ', ',
    }
    return render(request, 'index.html', context=my_dict)
'''

############################################################################
'''
from django.conf import settings
from django.core.mail import send_mail

send_mail('Subject here', 'Here is the message.', settings.EMAIL_HOST_USER,
         ['to@example.com'], fail_silently=False)


Unlock Captcha: https://accounts.google.com/DisplayUnlockCaptcha
'''
############################################################################

def registration_data(request):
    if not request.user.is_staff and not request.user.is_superuser:
        print(request.user.is_staff)
        print(request.user.is_superuser)
        print(not request.user.is_staff or not request.user.is_superuser)
        return HttpResponse("Page not found.")
    soloevents = Event.objects.all().prefetch_related('u_events')
    grpevents = Event.objects.all().prefetch_related('g_events')
    my_dict = {'solo_events': soloevents, 'group_events': grpevents}
    return render(request, 'r_data.html', context=my_dict)


def user_registry(request):
    # if selected == None:
    form = MyUserForm()

    if request.method == "POST":
        form = MyUserForm(request.POST)

        if form.is_valid():
            unique_email = form.cleaned_data['email']
            name = form.cleaned_data['first_name'] +" "+ form.cleaned_data['last_name']
            ins_type = form.cleaned_data['institute_type']
            ins_name = form.cleaned_data['institute_name']
            mobile = form.cleaned_data['mobile']
            form.save(commit=True)
            qs = MyUser.objects.filter(email=unique_email)
            for i in qs:
                identity = i.id
                date = i.date
            s = ""
            tot = 0.00
            for i in form.cleaned_data['registered_events']:
                s = s + i.event_name + "; "
                tot += float(i.event_cost)
            subject = "Thank you for registration."
            msg = "Ticket ID: U_ALA261{0}\nParticipant Name: {1}\nInstitute: {2}\nMobile No. {3}\nDate of Registration: {4}\nYou have been successfully registered for the following events: \n{5}\nParticipation fees (if any): Rs. {6}/-\n#Note: Please print and carry this ticket during the event.\n".format(str(identity), name, ins_name, mobile, str(date), s, tot)
            from_email = settings.EMAIL_HOST_USER
            to_list_emails = [unique_email, ]
            send_mail(subject, msg, from_email, to_list_emails, fail_silently=False)
            return HttpResponse("<script>alert('Thank You for registration check your Email.'); window.location.assign('/main_page/');</script>")        

    my_dict = {'form': form}
    return render(request, "registry_user.html", context=my_dict)


def add_event(request):
    if not request.user.is_staff or not request.user.is_superuser:
        return HttpResponse("Page not found.")
    form = MyEventForm()

    if request.method == "POST":
        form = MyEventForm(request.POST)

    if form.is_valid():
        form.save(commit=True)

    my_dict = {'form': form}
    return render(request, "add_events.html", context=my_dict)


def show_events(request):
    if not request.user.is_staff or not request.user.is_superuser:
        return HttpResponse("Page not found.")
    queryset = Event.objects.all()
    my_dict = {'queryset': queryset}
    return render(request, "show_events.html", context=my_dict)


def group_registry(request):
    form = MyGroupForm()

    if request.method == "POST":
        form = MyGroupForm(request.POST)

        if form.is_valid():
            p = request.POST.get('persons')
            title = form.cleaned_data['title']
            leader_name = form.cleaned_data['leader_name']
            ins_name = form.cleaned_data['institute_name']
            unique_email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile'] 
            instance = form.save(commit=False)
            instance.persons = p # way to manipulate data before saving into the database
            instance.save()
            form.save_m2m() # way to save the many-many form data.
            qs = MyGroup.objects.filter(email=unique_email)
            for i in qs:
                identity = i.id
                date = i.date
            s = ""
            tot = 0.00
            for i in form.cleaned_data['registered_events']:
                s = s + i.event_name + "; "
                tot += float(i.event_cost)
            subject = "Thank You for Registration."
            msg = "Ticket ID: G_ALA261{0}\nTitle: {1}\nLeader Name: {2}\nInstitute: {3}\nMobile No. {4}\nDate of Registration: {5}\nMembers in your team: {6}\nYou have been successfully registered for the following events: \n{7}\nParticipation fee (if any): Rs. {8}/-\n#Note: Please print and carry this ticket during the event.\n".format(str(identity), title, leader_name, ins_name, mobile, str(date), p, s, tot)
            from_email = settings.EMAIL_HOST_USER
            to_list_emails = [unique_email, ]
            send_mail(subject, msg, from_email, to_list_emails, fail_silently=False)
            return HttpResponse("<script>alert('Thank You for registration check your Email.'); window.location.assign('/main_page/');</script>")        

    my_dict = {'form': form}
    return render(request, "registry_group.html", context=my_dict)

def del_user(request, id=None):
    instance = get_object_or_404(MyUser, id=id)
    instance.delete()
    return HttpResponse("<script>alert('Deletion Successful.'); window.location.assign('/registry/data/');</script>")

def del_grp(request, id=None):
    instance = get_object_or_404(MyGroup, id=id)
    instance.delete()
    return HttpResponse("<script>alert('Deletion Successful.'); window.location.assign('/registry/data/');</script>")

def del_eve(request, id=None):
    instance = get_object_or_404(Event, id=id)
    instance.delete()
    return HttpResponse("<script>alert('Deletion Successful.'); window.location.assign('/show_events/');</script>")

