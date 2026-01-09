from django.core.management.base import BaseCommand
from pymongo import MongoClient
from datetime import datetime

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient()
        db = client['octofit_db']

        # Drop existing collections
        db.teams.drop()
        db.users.drop()
        db.activities.drop()
        db.workouts.drop()
        db.leaderboards.drop()

        # Create teams
        marvel_id = db.teams.insert_one({'name': 'Marvel'}).inserted_id
        dc_id = db.teams.insert_one({'name': 'DC'}).inserted_id

        # Create users
        users_data = [
            {'email': 'ironman@marvel.com', 'name': 'Tony Stark', 'team': marvel_id},
            {'email': 'captain@marvel.com', 'name': 'Steve Rogers', 'team': marvel_id},
            {'email': 'thor@marvel.com', 'name': 'Thor Odinson', 'team': marvel_id},
            {'email': 'hulk@marvel.com', 'name': 'Bruce Banner', 'team': marvel_id},
            {'email': 'blackwidow@marvel.com', 'name': 'Natasha Romanoff', 'team': marvel_id},
            {'email': 'superman@dc.com', 'name': 'Clark Kent', 'team': dc_id},
            {'email': 'batman@dc.com', 'name': 'Bruce Wayne', 'team': dc_id},
            {'email': 'wonderwoman@dc.com', 'name': 'Diana Prince', 'team': dc_id},
            {'email': 'flash@dc.com', 'name': 'Barry Allen', 'team': dc_id},
            {'email': 'aquaman@dc.com', 'name': 'Arthur Curry', 'team': dc_id},
        ]

        user_ids = []
        for user_data in users_data:
            user_id = db.users.insert_one(user_data).inserted_id
            user_ids.append(user_id)

        # Create workouts
        workouts_data = [
            {'name': 'Cardio Blast', 'description': 'High-intensity cardio workout', 'team': marvel_id},
            {'name': 'Strength Training', 'description': 'Build muscle with weights', 'team': marvel_id},
            {'name': 'Yoga Session', 'description': 'Relaxing yoga poses', 'team': dc_id},
            {'name': 'HIIT Workout', 'description': 'High-intensity interval training', 'team': dc_id},
            {'name': 'Pilates', 'description': 'Core strengthening exercises'},
        ]

        for workout_data in workouts_data:
            db.workouts.insert_one(workout_data)

        # Create activities
        activities_data = [
            {'user': user_ids[0], 'type': 'Running', 'duration': 30, 'calories': 300, 'date': datetime.now()},
            {'user': user_ids[1], 'type': 'Cycling', 'duration': 45, 'calories': 400, 'date': datetime.now()},
            {'user': user_ids[2], 'type': 'Swimming', 'duration': 60, 'calories': 500, 'date': datetime.now()},
            {'user': user_ids[3], 'type': 'Weightlifting', 'duration': 50, 'calories': 350, 'date': datetime.now()},
            {'user': user_ids[4], 'type': 'Yoga', 'duration': 40, 'calories': 200, 'date': datetime.now()},
            {'user': user_ids[5], 'type': 'Running', 'duration': 35, 'calories': 320, 'date': datetime.now()},
            {'user': user_ids[6], 'type': 'Martial Arts', 'duration': 55, 'calories': 450, 'date': datetime.now()},
            {'user': user_ids[7], 'type': 'Boxing', 'duration': 25, 'calories': 280, 'date': datetime.now()},
            {'user': user_ids[8], 'type': 'Sprint', 'duration': 20, 'calories': 250, 'date': datetime.now()},
            {'user': user_ids[9], 'type': 'Diving', 'duration': 30, 'calories': 300, 'date': datetime.now()},
        ]

        for activity_data in activities_data:
            db.activities.insert_one(activity_data)

        # Create leaderboard
        leaderboard_data = [
            {'user': user_ids[0], 'score': 1500},
            {'user': user_ids[1], 'score': 1400},
            {'user': user_ids[2], 'score': 1300},
            {'user': user_ids[3], 'score': 1200},
            {'user': user_ids[4], 'score': 1100},
            {'user': user_ids[5], 'score': 1000},
            {'user': user_ids[6], 'score': 900},
            {'user': user_ids[7], 'score': 800},
            {'user': user_ids[8], 'score': 700},
            {'user': user_ids[9], 'score': 600},
        ]

        for lb_data in leaderboard_data:
            db.leaderboards.insert_one(lb_data)

        # Create unique index on email
        db.users.create_index([('email', 1)], unique=True)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))