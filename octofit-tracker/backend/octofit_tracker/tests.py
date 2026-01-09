from django.test import TestCase
from .models import Team, User, Activity, Workout, Leaderboard

class TeamModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

class UserModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')

    def test_user_creation(self):
        user = User.objects.create(email='test@example.com', name='Test User', team=self.team)
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.name, 'Test User')
        self.assertEqual(user.team, self.team)

class ActivityModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(email='test@example.com', name='Test User', team=self.team)

    def test_activity_creation(self):
        activity = Activity.objects.create(user=self.user, type='Running', duration=30, calories=300)
        self.assertEqual(activity.user, self.user)
        self.assertEqual(activity.type, 'Running')
        self.assertEqual(activity.duration, 30)
        self.assertEqual(activity.calories, 300)

class WorkoutModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', description='A test workout', team=self.team)
        self.assertEqual(workout.name, 'Test Workout')
        self.assertEqual(workout.description, 'A test workout')
        self.assertEqual(workout.team, self.team)

class LeaderboardModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(email='test@example.com', name='Test User', team=self.team)

    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(user=self.user, score=1000)
        self.assertEqual(leaderboard.user, self.user)
        self.assertEqual(leaderboard.score, 1000)