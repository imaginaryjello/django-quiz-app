from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    """
    Extends Django's UserCreationForm to handle user registration with email.

    Attributes:
        email (EmailField): Required email field for user registration.

    Meta:
        model (User): The Django User model.
        fields (tuple): Fields to include in the form - username, email, and passwords.
    """
    email = forms.EmailField(
        max_length=254,
        required=True,
        help_text="Required. Enter a valid email address."
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    """
    Custom authentication form extending Django's built-in AuthenticationForm.

    Meta:
        model (User): The Django User model.
        fields (tuple): Fields to include - username and password.
    """

    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        """Initialize the form with custom HTML attributes."""
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})


class QuizForm(forms.Form):
    def __init__(self, questions, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for question in questions:
            choices = [
                (1, question.option1),
                (2, question.option2),
                (3, question.option3),
                (4, question.option4),
            ]
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                label=question.text,
                choices=choices,
                widget=forms.RadioSelect(attrs={
                    'class': 'radio-input'
                })
            )
    def clean(self):
        """
        Validate that all questions have been answered.

        Returns:
            dict: Cleaned form data.

        Raises:
            forms.ValidationError: If any question is unanswered.
        """
        cleaned_data = super().clean()
        for field_name, value in cleaned_data.items():
            if field_name.startswith('question_') and not value:
                raise forms.ValidationError("Please answer all questions.")
        return cleaned_data