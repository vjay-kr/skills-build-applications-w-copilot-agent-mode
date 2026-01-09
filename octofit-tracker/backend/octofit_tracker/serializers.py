from rest_framework import serializers
from .models import Team, User, Activity, Workout, Leaderboard

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    team_id = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'team', 'team_id']

    def create(self, validated_data):
        team_id = validated_data.pop('team_id')
        team = Team.objects.get(id=team_id)
        user = User.objects.create(team=team, **validated_data)
        return user

    def update(self, instance, validated_data):
        team_id = validated_data.pop('team_id', None)
        if team_id:
            instance.team = Team.objects.get(id=team_id)
        return super().update(instance, validated_data)

class ActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.CharField(write_only=True)

    class Meta:
        model = Activity
        fields = ['id', 'user', 'user_id', 'type', 'duration', 'calories', 'date']

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        user = User.objects.get(id=user_id)
        activity = Activity.objects.create(user=user, **validated_data)
        return activity

    def update(self, instance, validated_data):
        user_id = validated_data.pop('user_id', None)
        if user_id:
            instance.user = User.objects.get(id=user_id)
        return super().update(instance, validated_data)

class WorkoutSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    team_id = serializers.CharField(write_only=True, required=False, allow_null=True)

    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'team', 'team_id']

    def create(self, validated_data):
        team_id = validated_data.pop('team_id', None)
        if team_id:
            team = Team.objects.get(id=team_id)
            workout = Workout.objects.create(team=team, **validated_data)
        else:
            workout = Workout.objects.create(**validated_data)
        return workout

    def update(self, instance, validated_data):
        team_id = validated_data.pop('team_id', None)
        if team_id:
            instance.team = Team.objects.get(id=team_id)
        elif 'team_id' in validated_data:
            instance.team = None
        return super().update(instance, validated_data)

class LeaderboardSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.CharField(write_only=True)

    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'user_id', 'score', 'rank']

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        user = User.objects.get(id=user_id)
        leaderboard = Leaderboard.objects.create(user=user, **validated_data)
        return leaderboard

    def update(self, instance, validated_data):
        user_id = validated_data.pop('user_id', None)
        if user_id:
            instance.user = User.objects.get(id=user_id)
        return super().update(instance, validated_data)