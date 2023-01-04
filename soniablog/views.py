

from django.shortcuts import render, redirect 
from django.views import generic
from .models import Post
from django.views.generic.detail import DetailView
from .form import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import SubscribedUsers
from django.contrib import messages
from django.core.mail import EmailMessage
from .form import NewsletterForm
from django.views.decorators.csrf import csrf_exempt
import uuid
from django.urls import reverse
from django import forms
from .form import subscribersform




from django.contrib import messages
from django.conf import settings

from paypal.standard.forms import PayPalPaymentsForm

#from .decorators import user_is_superuser








class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'soniablog/index.html'  # a list of all posts will be displayed on index.html


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'soniablog/post_detail.html'  # detail about each blog post will be on post_detail.

def contact_form(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f'Message from {form.cleaned_data["name"]}'
            message = form.cleaned_data["message"]
            sender = form.cleaned_data["email"]
            recipients = ['saahndongransom@gmail.com']
            try:
                send_mail(subject, message, sender, recipients, fail_silently=True)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return HttpResponse('Success...Your email has been sent')
    return render(request, 'soniablog/contact.html', {'form': form})
    return redirect('/')

def policy(request):
    return render(request , 'soniablog/policy.html',{'policy': policy} )
def site(request):
    return render(request, 'soniablog/site.html',{'site': site})
def aboutme(request):
    return render(request,'soniablog/aboutme.html',{'aboutme':aboutme})
def footer(request):
    return render(request,'soniablog/footer.html',{'footer':footer})




#subscribe functionality
def subscribe(request):
 
    if request.method == 'POST':
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)

        if not name or not email:
            messages.error(request, "You must type legit name and email to subscribe to a Newsletter")
            return redirect("/")

        if get_user_model().objects.filter(email=email).first():
            messages.error(request, f"Found registered user with associated {email} email. You must login to subscribe or unsubscribe.")
            return redirect(request.META.get("HTTP_REFERER", "/")) 

        subscribe_user = SubscribedUsers.objects.filter(email=email).first()
        if subscribe_user:
            messages.error(request, f"{email} email address is already subscriber.")
            return redirect(request.META.get("HTTP_REFERER", "/"))  

        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("/")

        subscribe_model_instance = SubscribedUsers()
        subscribe_model_instance.name = name
        subscribe_model_instance.email = email
        subscribe_model_instance.save()
        messages.success(request, f'{email} email was successfully subscribed to our newsletter!')
        return redirect(request.META.get("HTTP_REFERER", "/"))



 


 

 #paypal
def feli(request):
    host = request.get_host()
    paypal_dict = {
            'business':settings.PAYPAL_RECEIVER_EMAIL,
            'amount': '%.20.0f',
            'item_name': "product 1",
            'invoice': "str(uuid.uuid4())",
            'currency_code': 'USD',
            'notify_url':f'http://{host}{reverse("paypal-ipn")}',
            'return_url':f'http://{host}{reverse("paypal-return")}',
            'cancel_return':f'http://{host}{reverse("paypal-cancel")}',
        
          
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    contact = {'form':form}
    return render(request,'soniablog/feli.html',contact)
 
def paypal_return(request):
    messages.success(request="you/ succefully make payment")
    return redirect('home')

def paypal_cancel(request):
    messages.error(request="you/ succefully make payment")
    return redirect('home')





def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            receivers = form.cleaned_data.get('receivers').split(',')
            email_message = form.cleaned_data.get('message')

            mail = EmailMessage(subject, email_message, f"soniablog <{request.user.email}>", bcc=receivers)
            mail.content_subtype = 'html'

            if mail.send():
                messages.success(request, "Email sent succesfully")
            else:
                messages.error(request, "There was an error sending email")

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

        return redirect('/')

    form = NewsletterForm()
    form.fields['receivers'].initial = ','.join([active.email for active in SubscribedUsers.objects.all()])
    return render(request=request, template_name='soniablog/newsletter.html', context={'form': form})

def get_context_data(self, **kwargs):
        similar_posts = self.object.tags.similar_objects()[:3]
        post_comments_count = Comment.objects.all().filter(post=self.object.id).count()
        post_comments = Comment.objects.all().filter(post=self.object.id)
        context = super().get_context_data(**kwargs)
        context.update({
            "similar_posts":similar_posts,
            'form': self.form,
            'post_comments': post_comments,
            'post_comments_count': post_comments_count,
        })


        return context

def home1(request):
   return render(request,'soniablog/home1.html',{'home1':home1})


#new
def habiba(request):
    if request.method == 'POST':
        form = subscribersform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'subscription successful')
            return redirect('/')
    else:
        form = subscribersform()
    context= {
        'form':form,

    }
    return render(request,'soniablog/habiba.html', context)
    