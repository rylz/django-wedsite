from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.urls import set_script_prefix
from wedsite.conf import settings

class Command(BaseCommand):
    help = 'Sends a summary email to all users'

    def get_rsvp_persons(self, user):
        """
        Gets the RSVP for a user
        """
        try:
            rsvp = user.profile.rsvp
        except:
            print ("Error getting RSVP for {} {}".format(user.first_name, user.last_name))
            return []

        return rsvp.rsvp_person.all()

    def get_attending_rehearsal(self, user):
        result = []

        people = self.get_rsvp_persons(user)
        for person in people:
            if person.is_attending_rehearsal:
                result.append(person)

        return result

    def get_attending_wedding(self, user):
        result = []

        people = self.get_rsvp_persons(user)
        for person in people:
            if person.is_attending_wedding:
                result.append(person)

        return result

    def handle(self, *args, **options):
        '''send email via mailgun'''

        # Need a fake request to help us set up all the links in the email to work
        #fake_request = FakeHttpRequest()

        subject = "{} and {}'s Wedding: Update".format(settings.WEDSITE_JSON['gride']['first_name'], settings.WEDSITE_JSON['broom']['first_name'])
        from_email = "{} and {}'s Wedding<wedding@mg.wedsite.io>".format(settings.WEDSITE_JSON['gride']['first_name', settings.WEDSITE_JSON['broom']['first_name']])

        for user in User.objects.all():

            # Figure out if they're attending rehearsal/wedding
            attending_rehearsal = self.get_attending_rehearsal(user)
            attending_wedding = self.get_attending_wedding(user)
            text_template = get_template("email/email.txt")
            html_template = get_template("email/email.html")

            # Only send the message if they're attending the wedding
            if attending_wedding:

                template_info = {
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "attending_rehearsal": self.get_attending_rehearsal(user),
                    "attending_wedding": self.get_attending_wedding(user),
                }

                text_content = text_template.render(template_info)
                html_content = html_template.render(template_info)
                print ("{} {}".format(user.first_name, user.last_name))
                msg = EmailMultiAlternatives(subject, text_content, from_email, [user.email])
                msg.attach_alternative(html_content, "text/html")
                msg.send()