import json

from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from authentication.models import Preference
from dbutils.optional import Optional
from schedule.models import User, UserSchoolActivity, SchoolActivity


# Create your views here.


class RegisterView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        uid = -1
        if request.method == "POST":
            uid = _process_register(request.body)
        ret = {"id": uid}
        return JsonResponse(ret)


class PreferencesView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, username):
        username = username + "@gmail.com"
        pid = -1
        if request.method == "POST":
            pid = _process_preferences(request.body, username)
        ret = {"id": pid}
        return JsonResponse(ret)


class OptionalsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, username):
        username = username + "@gmail.com"
        rid = -1
        if request.method == "POST":
            rid = _process_optionals(request.body, username)
        ret = {"id": rid}
        return JsonResponse(ret)


def _process_preferences(post_body, username):
    post = json.loads(post_body)
    user = User.objects.get(email=username)
    # print(post["preference1"])
    preference = Preference(
        user=user,
        preference1=post["preference1"],
        preference2=post["preference2"],
        preference3=post["preference3"],
        preference1_prio=post["pref1_prio"],
        preference2_prio=post["pref2_prio"],
        preference3_prio=post["pref3_prio"]
    )
    # print(preference)
    preference.save()
    return user.id


def _process_optionals(post_body, username):
    post = json.loads(post_body)
    user = User.objects.get(email=username)
    optionale = []
    for optional in post:
        optionale.append(optional)
    school_activities = SchoolActivity.objects.filter(group=user.group)
    for activity in school_activities:
        if activity.title not in Optional.optional:
            user_activity = UserSchoolActivity(
                user=user,
                school_activity=activity
            )
            user_activity.save()
    for optional in optionale:
        s_activity = SchoolActivity.objects.filter(title=optional, group=user.group)
        for activity in s_activity:
            user_activity = UserSchoolActivity(
                user=user,
                school_activity=activity
            )
            user_activity.save()
    return 1


def _process_register(post_body):
    post = json.loads(post_body)
    print(post)
    # User.objects.all().delete()
    user = User(
        uid=post["uid"],
        name=post["name"],
        group=post["group"],
        email=post["email"],
        photo_url=post["photo"]
    )
    user.save()
    pref = Preference(
        user=user,
        preference1=False,
        preference2=False,
        preference3=False,
        preference1_prio='LOW',
        preference2_prio='LOW',
        preference3_prio='LOW'
    )
    pref.save()
    return user.uid
