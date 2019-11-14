from schedule.models import ExtraActivity


class ExtraFacActivity:

    def __init__(self, activity: ExtraActivity):
        self.id = activity.id
        self.title = activity.title
        self.priority = activity.priority
        self.day = activity.day
        self.frequency = activity.frequency
        self.duration = activity.duration
        self.location = activity.location
        self.start_time = activity.start_time
        self.description = activity.description
