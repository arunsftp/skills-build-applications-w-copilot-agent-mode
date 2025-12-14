from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import (
    UserSerializer, TeamSerializer, ActivitySerializer,
    LeaderboardSerializer, WorkoutSerializer
)


@api_view(['GET'])
def api_root(request, format=None):
    """API root endpoint that lists all available endpoints"""
    import os
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        base_url = f"https://{codespace_name}-8000.app.github.dev"
    else:
        base_url = request.build_absolute_uri('/')[:-1]
    
    return Response({
        'users': f"{base_url}/api/users/",
        'teams': f"{base_url}/api/teams/",
        'activities': f"{base_url}/api/activities/",
        'leaderboard': f"{base_url}/api/leaderboard/",
        'workouts': f"{base_url}/api/workouts/",
    })


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint for users"""
    queryset = User.objects.all().order_by('-created_at')
    serializer_class = UserSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """API endpoint for teams"""
    queryset = Team.objects.all().order_by('-created_at')
    serializer_class = TeamSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """API endpoint for activities"""
    queryset = Activity.objects.all().order_by('-date', '-created_at')
    serializer_class = ActivitySerializer


class LeaderboardViewSet(viewsets.ModelViewSet):
    """API endpoint for leaderboard"""
    queryset = Leaderboard.objects.all().order_by('-total_points')
    serializer_class = LeaderboardSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    """API endpoint for workouts"""
    queryset = Workout.objects.all().order_by('-created_at')
    serializer_class = WorkoutSerializer
