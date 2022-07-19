from .models import ThresholdSettings

def threshold_settings(request):
    return {
        "threshold_settings": ThresholdSettings.load()
    }