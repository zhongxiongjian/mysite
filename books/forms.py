from django import forms
TOPIC_CHOICES = (
    ('general', 'General enquiry'),
    ('bug1', 'Bug report'),
    ('suggestion', 'Suggestion'),
)

class ContactForm(forms.Form):
    topic = forms.ChoiceField(choices=TOPIC_CHOICES)
    message = forms.CharField(widget=forms.Textarea(),initial='Replace with your feedback')
    sender = forms.EmailField(required=False,initial='user@example.com')
