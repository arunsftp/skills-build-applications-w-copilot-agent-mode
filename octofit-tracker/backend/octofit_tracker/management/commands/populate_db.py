from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Clearing existing data...')
        # Delete existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        
        self.stdout.write('Creating teams...')
        # Create teams - Marvel and DC themed
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Heroes from the Marvel Universe'
        )
        team_dc = Team.objects.create(
            name='Team DC',
            description='Heroes from the DC Universe'
        )
        
        self.stdout.write('Creating users...')
        # Create Marvel users
        marvel_users = [
            User.objects.create(name='Tony Stark', email='ironman@marvel.com', team=team_marvel),
            User.objects.create(name='Steve Rogers', email='captain@marvel.com', team=team_marvel),
            User.objects.create(name='Thor Odinson', email='thor@marvel.com', team=team_marvel),
            User.objects.create(name='Natasha Romanoff', email='blackwidow@marvel.com', team=team_marvel),
            User.objects.create(name='Bruce Banner', email='hulk@marvel.com', team=team_marvel),
        ]
        
        # Create DC users
        dc_users = [
            User.objects.create(name='Clark Kent', email='superman@dc.com', team=team_dc),
            User.objects.create(name='Bruce Wayne', email='batman@dc.com', team=team_dc),
            User.objects.create(name='Diana Prince', email='wonderwoman@dc.com', team=team_dc),
            User.objects.create(name='Barry Allen', email='flash@dc.com', team=team_dc),
            User.objects.create(name='Arthur Curry', email='aquaman@dc.com', team=team_dc),
        ]
        
        all_users = marvel_users + dc_users
        
        self.stdout.write('Creating activities...')
        # Create activities for the past 30 days
        activity_types = ['running', 'walking', 'cycling', 'swimming', 'strength']
        for user in all_users:
            for i in range(random.randint(5, 15)):
                activity_date = date.today() - timedelta(days=random.randint(0, 30))
                activity_type = random.choice(activity_types)
                duration = random.randint(20, 90)
                distance = random.uniform(1, 15) if activity_type in ['running', 'walking', 'cycling'] else None
                calories = duration * random.randint(5, 10)
                
                Activity.objects.create(
                    user=user,
                    activity_type=activity_type,
                    duration_minutes=duration,
                    distance_km=distance,
                    calories_burned=calories,
                    date=activity_date
                )
        
        self.stdout.write('Creating leaderboard entries...')
        # Create leaderboard entries
        for user in all_users:
            activities = Activity.objects.filter(user=user)
            total_points = sum(act.calories_burned for act in activities)
            total_activities = activities.count()
            
            Leaderboard.objects.create(
                user=user,
                team=user.team,
                total_points=total_points,
                total_activities=total_activities,
                rank=0  # Will be updated with actual ranks
            )
        
        # Update ranks
        leaderboard_entries = Leaderboard.objects.all().order_by('-total_points')
        for rank, entry in enumerate(leaderboard_entries, start=1):
            entry.rank = rank
            entry.save()
        
        self.stdout.write('Creating workout suggestions...')
        # Create workout suggestions
        workouts = [
            {
                'title': 'Morning Run',
                'description': 'Start your day with a refreshing 5K run',
                'difficulty': 'beginner',
                'duration_minutes': 30,
                'activity_type': 'running'
            },
            {
                'title': 'Power Cycling',
                'description': 'High-intensity cycling workout',
                'difficulty': 'intermediate',
                'duration_minutes': 45,
                'activity_type': 'cycling'
            },
            {
                'title': 'Strength Training',
                'description': 'Full body strength workout',
                'difficulty': 'advanced',
                'duration_minutes': 60,
                'activity_type': 'strength'
            },
            {
                'title': 'Evening Walk',
                'description': 'Relaxing evening walk',
                'difficulty': 'beginner',
                'duration_minutes': 20,
                'activity_type': 'walking'
            },
            {
                'title': 'Swimming Endurance',
                'description': 'Build swimming endurance',
                'difficulty': 'intermediate',
                'duration_minutes': 40,
                'activity_type': 'swimming'
            },
        ]
        
        for workout_data in workouts:
            Workout.objects.create(**workout_data)
        
        self.stdout.write(self.style.SUCCESS('Successfully populated the database!'))
        self.stdout.write(f'Created {Team.objects.count()} teams')
        self.stdout.write(f'Created {User.objects.count()} users')
        self.stdout.write(f'Created {Activity.objects.count()} activities')
        self.stdout.write(f'Created {Leaderboard.objects.count()} leaderboard entries')
        self.stdout.write(f'Created {Workout.objects.count()} workouts')
