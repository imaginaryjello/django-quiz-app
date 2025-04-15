from django.core.management.base import BaseCommand
from quiz.models import Question


class Command(BaseCommand):
    help = 'Loads French language questions into the database'

    def handle(self, *args, **kwargs):
        questions = [
            {
                'text': 'What is the French word for "hello"?',
                'option1': 'Bonjour',
                'option2': 'Au revoir',
                'option3': 'Merci',
                'option4': 'S\'il vous plaît',
                'correct_option': 1,
            },
            {
                'text': 'How do you say "goodbye" in French?',
                'option1': 'Bonjour',
                'option2': 'Au revoir',
                'option3': 'Merci',
                'option4': 'Excusez-moi',
                'correct_option': 2,
            },
            {
                'text': 'What does "merci" mean in English?',
                'option1': 'Please',
                'option2': 'Thank you',
                'option3': 'Hello',
                'option4': 'Goodbye',
                'correct_option': 2,
            },
            {
                'text': 'How do you say "please" in French?',
                'option1': 'Pardon',
                'option2': 'Merci',
                'option3': 'S\'il vous plaît',
                'option4': 'Excusez-moi',
                'correct_option': 3,
            },
            {
                'text': 'What is the French word for "water"?',
                'option1': 'Pain',
                'option2': 'Fromage',
                'option3': 'Eau',
                'option4': 'Vin',
                'correct_option': 3,
            },
            {
                'text': 'How do you say "bread" in French?',
                'option1': 'Fromage',
                'option2': 'Pain',
                'option3': 'Beurre',
                'option4': 'Lait',
                'correct_option': 2,
            },
            {
                'text': 'What does "je m\'appelle" mean in English?',
                'option1': 'I am happy',
                'option2': 'My name is',
                'option3': 'I am hungry',
                'option4': 'I don\'t know',
                'correct_option': 2,
            },
            {
                'text': 'How do you say "I don\'t understand" in French?',
                'option1': 'Je ne sais pas',
                'option2': 'Je ne comprends pas',
                'option3': 'Je ne parle pas français',
                'option4': 'Je suis désolé',
                'correct_option': 2,
            },
            {
                'text': 'What is the French word for "cat"?',
                'option1': 'Chien',
                'option2': 'Oiseau',
                'option3': 'Chat',
                'option4': 'Poisson',
                'correct_option': 3,
            },
            {
                'text': 'How do you say "dog" in French?',
                'option1': 'Chat',
                'option2': 'Cheval',
                'option3': 'Chien',
                'option4': 'Lapin',
                'correct_option': 3,
            },
            {
                'text': 'What does "aujourd\'hui" mean in English?',
                'option1': 'Yesterday',
                'option2': 'Tomorrow',
                'option3': 'Today',
                'option4': 'Now',
                'correct_option': 3,
            },
            {
                'text': 'How do you say "tomorrow" in French?',
                'option1': 'Hier',
                'option2': 'Aujourd\'hui',
                'option3': 'Demain',
                'option4': 'Maintenant',
                'correct_option': 3,
            },
            {
                'text': 'What is the French word for "book"?',
                'option1': 'Crayon',
                'option2': 'Livre',
                'option3': 'Papier',
                'option4': 'Stylo',
                'correct_option': 2,
            },
            {
                'text': 'How do you say "pen" in French?',
                'option1': 'Crayon',
                'option2': 'Gomme',
                'option3': 'Stylo',
                'option4': 'Livre',
                'correct_option': 3,
            },
            {
                'text': 'What does "école" mean in English?',
                'option1': 'School',
                'option2': 'House',
                'option3': 'Park',
                'option4': 'Office',
                'correct_option': 1,
            },
            {
                'text': 'How do you say "house" in French?',
                'option1': 'Appartement',
                'option2': 'Maison',
                'option3': 'Bâtiment',
                'option4': 'Château',
                'correct_option': 2,
            },
            {
                'text': 'What is the French word for "car"?',
                'option1': 'Vélo',
                'option2': 'Bus',
                'option3': 'Voiture',
                'option4': 'Train',
                'correct_option': 3,
            },
            {
                'text': 'How do you say "bicycle" in French?',
                'option1': 'Moto',
                'option2': 'Vélo',
                'option3': 'Scooter',
                'option4': 'Voiture',
                'correct_option': 2,
            },
            {
                'text': 'What does "l\'hôtel" mean in English?',
                'option1': 'Hospital',
                'option2': 'Restaurant',
                'option3': 'Hotel',
                'option4': 'Airport',
                'correct_option': 3,
            },
            {
                'text': 'How do you say "airport" in French?',
                'option1': 'Gare',
                'option2': 'Aéroport',
                'option3': 'Port',
                'option4': 'Station de métro',
                'correct_option': 2,
            },
        ]

        for q_data in questions:
            Question.objects.create(
                topic='FR',
                text=q_data['text'],
                option1=q_data['option1'],
                option2=q_data['option2'],
                option3=q_data['option3'],
                option4=q_data['option4'],
                correct_option=q_data['correct_option']
            )

        self.stdout.write(self.style.SUCCESS('Successfully loaded French language questions'))