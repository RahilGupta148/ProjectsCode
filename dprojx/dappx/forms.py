from django import forms
from django.contrib.auth.models import User
from dappx.models import UserProfileInfo,Document,NewProject

class DocumentForm(forms.ModelForm):
    class Meta():
        model=Document
        fields=('description','vidimage','project_video','docname','proj_price')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    contact = forms.IntegerField()
    class Meta():
        model = User
        fields = ('username','email','password','contact')

    def as_myp(self):
        "Returns this form rendered as HTML <p>s."
        return self._html_output(
            normal_row = '<p%(html_class_attr)s>%(label)s</p> <p>%(field)s%(help_text)s</p>',
            error_row = '%s',
            row_ender = '</p>',
            help_text_html = ' <span class="helptext">%s</span>',
            errors_on_separate_row = True)

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields =('portfolio_site','profile_pic')

class NewProjectForm(forms.ModelForm):
    class Meta():
        model = NewProject
        fields=('project_name','project_details','technology_preferred','days_available','proj_status','quotation_fixed')

    def as_myp(self):
        "Returns this form rendered as HTML <p>s."
        return self._html_output(
            normal_row = '<p%(html_class_attr)s>%(label)s</p> <p>%(field)s%(help_text)s</p>',
            error_row = '%s',
            row_ender = '</p>',
            help_text_html = ' <span class="helptext">%s</span>',
            errors_on_separate_row = True)
