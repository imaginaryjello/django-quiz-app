from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Question(models.Model):
    """
    Represents a quiz question with multiple-choice options.

    Attributes:
        TOPIC_CHOICES (list): Available topic choices (currently only French)
        topic (CharField): The question's topic/category
        text (TextField): The question content
        option1-4 (CharField): The four multiple-choice options
        correct_option (IntegerField): Index (1-4) of the correct answer

    Methods:
        __str__: String representation of the question
    """
    TOPIC_CHOICES = [
        ('FR', 'French Language'),  # Can be extended with more topics
    ]

    topic = models.CharField(
        max_length=2,
        choices=TOPIC_CHOICES,
        default='FR',
        help_text="Category/topic of the question"
    )

    text = models.TextField(
        help_text="The question text/content"
    )

    # Multiple choice options
    option1 = models.CharField(
        max_length=200,
        help_text="First answer option"
    )
    option2 = models.CharField(
        max_length=200,
        help_text="Second answer option"
    )
    option3 = models.CharField(
        max_length=200,
        help_text="Third answer option"
    )
    option4 = models.CharField(
        max_length=200,
        help_text="Fourth answer option"
    )

    correct_option = models.IntegerField(
        validators=[
            MinValueValidator(1, message="Value must be at least 1"),
            MaxValueValidator(4, message="Value must be at most 4")
        ],
        help_text="Correct option number (1-4)"
    )

    def __str__(self):
        """String representation showing question text."""
        return self.text[:50] + ('...' if len(self.text) > 50 else '')


class QuizResult(models.Model):
    """
    Tracks a user's quiz attempt and results.

    Attributes:
        user (ForeignKey): Reference to the User who took the quiz
        date_taken (DateTimeField): When the quiz was completed
        score (IntegerField): Number of correct answers
        total_questions (IntegerField): Total questions in the quiz

    Methods:
        percentage: Calculates score percentage
        feedback_message: Returns performance feedback
        __str__: String representation of the result
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='quiz_results',
        help_text="User who took the quiz"
    )

    date_taken = models.DateTimeField(
        auto_now_add=True,
        help_text="Date and time when quiz was taken"
    )

    score = models.IntegerField(
        help_text="Number of correct answers"
    )

    total_questions = models.IntegerField(
        default=5,
        help_text="Total number of questions in the quiz"
    )

    def percentage(self):
        """
        Calculates the percentage score.

        Returns:
            float: Percentage score (0-100)

        Example:
            >>> result = QuizResult(score=3, total_questions=5)
            >>> result.percentage()
            60.0
        """
        return (self.score / self.total_questions) * 100

    def feedback_message(self):
        """
        Generates performance feedback based on score percentage.

        Returns:
            str: Encouragement message based on performance tier
        """
        percentage = self.percentage()
        if percentage >= 80:
            return "You are a genius!"
        elif percentage >= 60:
            return "Excellent work!"
        elif percentage >= 40:
            return "Good job!"
        else:
            return "Please try again!"

    def __str__(self):
        """String representation showing user, date, and score."""
        return (
            f"{self.user.username} - "
            f"{self.date_taken.strftime('%Y-%m-%d %H:%M')} - "
            f"{self.score}/{self.total_questions}"
        )

    class Meta:
        """Metadata options for the QuizResult model."""
        ordering = ['-date_taken']  # Newest results first
        verbose_name = 'Quiz Result'
        verbose_name_plural = 'Quiz Results'