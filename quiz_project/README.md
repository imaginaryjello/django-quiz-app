Author

    Nishan Sapkota C0911047
    Protsan Karki C0918275
    Sugan Subedi C0918634
    Apil Kumal

Description: Django application for quiz \
Date: 2025/04/15





Django Quiz Application Documentation
1. Overview\
This documentation explains the Django-based Quiz Application that tests users knowledge of the French language. The application allows users to:
        
        Sign up / Log in to track their progress.
        
        Take a quiz with 5 randomly selected questions.
        
        View results with scores, percentages, and feedback.
        
        Retake the quiz if they score below 60%.
        
        See their quiz history with statistics (average, highest, and lowest scores).

2. System Architecture
The application follows the Model-Template-View (MTV) pattern of Django:

A. Models (quiz/models.py)
Define the database structure:

    Question Model
    
    Stores quiz questions, options, and correct answers.
    
    Example:
        text = "What is 'hello' in French?"
        option1 = "Bonjour" (correct)
        option2 = "Au revoir"
        option3 = "Merci"
        option4 = "S'il vous plaît"
        correct_option = 1

    QuizResult Model 

    Tracks user attempts, scores, and feedback.
    Methods:
    percentage() → Calculates score percentage.
    feedback_message() → Returns feedback based on score.


B. Views (quiz/views.py)
Handle user requests and business logic:
    
    quiz()
    GET: Displays 5 random questions.
    POST: Calculates score, saves results, and redirects to results page.
    results()
    Shows score, percentage, and feedback.
    results_history() 
    Displays all past attempts with statistics.

C. Templates (quiz/templates/quiz/)
Render HTML pages:
    
    quiz.html → Displays the quiz form.
    
    results.html → Shows score and feedback.
    
    history.html → Lists all past attempts with stats.

D. URLs (quiz/urls.py)
Maps URLs to views:
    
    path('quiz/', views.quiz, name='quiz'),
    path('quiz/results/<int:result_id>/', views.results, name='results'),
    path('history/', views.results_history, name='history'),

3. Key Features & Logic

A. Quiz Functionality

    Random Question Selection
    
    Every quiz loads 5 random questions from the database.
    
    Ensures no repetition in a single session.
    
    Automatic Scoring
    
    Each correct answer increments the score.

    Calculates percentage:

        python
        Copy
        percentage = (score / total_questions) * 100
            Feedback Messages
    
    Based on score:
    
    0-2/5 → "Please try again!"
    
    3/5 → "Good job!"
    
    4/5 → "Excellent work!"
    
    5/5 → "You are a genius!"
    
    Retake Option
    
    If score < 60%, users see a "Retake Quiz" button.

B. History & Statistics:
    All attempts are stored in the database.
    
    Statistics shown:
    
    Average score → QuizResult.objects.aggregate(Avg('score'))
    
    Highest score → Max('score')
    
    Lowest score → Min('score')


4. Setup and deployement :

    Since this code wont be for github and will be included with django library installed the prior installation process wont be necesary
    1. Run Development Server
        
            python manage.py runserver

5Conclusion
    This Django quiz application provides:

    //User authentication (Signup/Login)
    //Randomized quizzes with scoring
    //Feedback & retake options
    //History tracking & statistics

It is scalable and can be extended with new features easily.