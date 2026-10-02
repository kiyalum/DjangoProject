import logging
from datetime import datetime


logger = logging.getLogger(__name__)


class ActionLoggingMixin:
    """Custom Action logging mixin..."""

    log_message = "User ..."

    def dispatch(self, request, *args, **kwargs):
        user = request.user if request.user.is_authenticated else "Anonymous"
        print(f"[Logging Mixin]: {user} turned to {self.__class__.__name__} ({request.method})")
        return super().dispatch(request, *args, **kwargs)


class NightOwlMixin:
    """Mixin to check for night time (from 22:00 to 07:00)"""

    def check_is_night_time(self) -> bool:
        """Checks if the current time is between 22:00 and 07:00"""
        current_hour = datetime.now().hour
        return current_hour >= 22 or current_hour < 7

    def dispatch(self, request, *args, **kwargs):
        if self.check_is_night_time():
            print("[NIGHT OWL]: Someone is browsing the site at night!")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """Add the is_night_time variable to the template context"""
        context = super().get_context_data(**kwargs)
        context['is_night_time'] = self.check_is_night_time()
        return context