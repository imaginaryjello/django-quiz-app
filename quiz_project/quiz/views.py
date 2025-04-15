from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Max, Min
import random
from .models import Question, QuizResult
from .forms import SignUpForm, LoginForm, QuizForm


def home(request):
    """
    Renders the home page of the quiz application.

    Args:
        request (HttpRequest): The incoming request object

    Returns:
        HttpResponse: Rendered home.html template
    """
    return render(request, 'quiz/home.html')


def signup(request):
    """
    Handles user registration.

    Behavior:
        - On GET: Displays empty registration form
        - On POST: Validates and processes form data
        - Successful registration logs user in automatically

    Args:
        request (HttpRequest): The incoming request object

    Returns:
        HttpResponse: Rendered signup form or quiz redirect
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            return redirect('quiz:quiz')
    else:
        form = SignUpForm()
    return render(request, 'quiz/signup.html', {'form': form})


def user_login(request):
    """
    Handles user authentication.

    Behavior:
        - On GET: Displays empty login form
        - On POST: Validates credentials and authenticates user

    Args:
        request (HttpRequest): The incoming request object

    Returns:
        HttpResponse: Rendered login form or quiz redirect
    """
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('quiz:quiz')
    else:
        form = LoginForm()
    return render(request, 'quiz/login.html', {'form': form})


@login_required
def user_logout(request):
    """
    Handles user logout.

    Behavior:
        - Terminates the user session
        - Redirects to home page
    Args:
        request (HttpRequest): The incoming request object
    Returns:
        HttpResponseRedirect: Redirect to home page
    """
    logout(request)
    return redirect('quiz:home')


@login_required
def quiz(request):
    """
    Handles quiz taking process.

    Behavior:
        - GET: Generates new quiz with 5 random questions
        - POST: Processes submitted answers and calculates score
        - Stores question IDs in session for validation

    Args:
        request (HttpRequest): The incoming request object

    Returns:
        HttpResponse: Quiz form, results redirect, or error page
    """
    if request.method == 'POST':
        # Retrieve questions from session to prevent tampering
        questions = Question.objects.filter(id__in=request.session.get('quiz_questions', []))
        form = QuizForm(questions, request.POST)

        if form.is_valid():
            score = 0
            # Calculate score by comparing answers
            for question in questions:
                user_answer = form.cleaned_data.get(f'question_{question.id}')
                if user_answer and int(user_answer) == question.correct_option:
                    score += 1

            # Store results
            result = QuizResult.objects.create(
                user=request.user,
                score=score,
                total_questions=len(questions))

            return redirect('quiz:results', result_id=result.id)

    # GET request - initialize new quiz
    questions = list(Question.objects.filter(topic='FR'))
    if len(questions) < 5:
        return render(request, 'quiz/not_enough_questions.html')

    # Select 5 random questions and store IDs in session
    selected_questions = random.sample(questions, 5)
    request.session['quiz_questions'] = [q.id for q in selected_questions]
    form = QuizForm(selected_questions)
    return render(request, 'quiz/quiz.html', {'form': form})


@login_required
def results(request, result_id):
    """
    Displays quiz results.

    Args:
        request (HttpRequest): The incoming request object
        result_id (int): ID of the QuizResult to display

    Returns:
        HttpResponse: Rendered results page

    Raises:
        Http404: If result doesn't exist or doesn't belong to user
    """
    result = get_object_or_404(QuizResult, id=result_id, user=request.user)
    return render(request, 'quiz/results.html', {'result': result})


@login_required
def results_history(request):
    """
    Displays user's quiz history and statistics.

    Calculates:
        - Average score across all attempts
        - Highest and lowest scores
        - Total number of attempts

    Args:
        request (HttpRequest): The incoming request object

    Returns:
        HttpResponse: Rendered history page with stats
    """
    results = QuizResult.objects.filter(user=request.user)

    stats = {
        'average': results.aggregate(Avg('score'))['score__avg'],
        'highest': results.aggregate(Max('score'))['score__max'],
        'lowest': results.aggregate(Min('score'))['score__min'],
        'total_attempts': results.count(),
    }

    return render(request, 'quiz/history.html', {
        'results': results,
        'stats': stats,
    })
#
# @login_required
# def quiz(request):
#     # Get 5 random questions
#     questions = list(Question.objects.filter(topic='FR'))  # French questions
#     if len(questions) < 5:
#         # Handle case where there aren't enough questions
#         return render(request, 'quiz/not_enough_questions.html')
#
#     selected_questions = random.sample(questions, 5)
#
#     if request.method == 'POST':
#         form = QuizForm(selected_questions, request.POST)
#         if form.is_valid():
#             score = 0
#             for question in selected_questions:
#                 user_answer = form.cleaned_data.get(f'question_{question.id}')
#                 if int(user_answer) == question.correct_option:
#                     score += 1
#
#             # Save result
#             result = QuizResult.objects.create(
#                 user=request.user,
#                 score=score,
#                 total_questions=5
#             )
#
#             # Prepare context for results page
#             context = {
#                 'score': score,
#                 'total': 5,
#                 'result': result,
#                 'feedback': result.feedback_message(),
#                 'percentage': result.percentage(),
#             }
#             return render(request, 'quiz/results.html', context)
#     else:
#         form = QuizForm(selected_questions)
#
#     return render(request, 'quiz/quiz.html', {'form': form, 'questions': selected_questions})
#
#
# @login_required
# def results_history(request):
#     results = QuizResult.objects.filter(user=request.user).order_by('-date_taken')
#
#     if results.exists():
#         stats = {
#             'average': results.aggregate(Avg('score'))['score__avg'],
#             'highest': results.aggregate(Max('score'))['score__max'],
#             'lowest': results.aggregate(Min('score'))['score__min'],
#         }
#     else:
#         stats = None
#
#     return render(request, 'quiz/history.html', {'results': results, 'stats': stats})