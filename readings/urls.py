from django.urls import include, path
from .views import (
    GetCurrentReadings,
    NoteListView,
    PostDataReadings,
    ReadingDataListView,
    UsersListView,
)
from .views import dashboard_page, line_chart, line_chart_json, create_notepad_view
from django.contrib.auth.decorators import login_required
from django.views.generic.base import RedirectView


urlpatterns = [
    path("api/data-readings/", PostDataReadings.as_view(), name="post_data_readings"),
    path(
        "current-readings/", GetCurrentReadings.as_view(), name="get_current_readings"
    ),
    path("dashboard/", login_required(dashboard_page), name="dashboard"),
    path("chart/", line_chart, name="line_chart"),
    path("chartJSON/", line_chart_json, name="line_chart_json"),
    path(
        "table-readings/",
        login_required(ReadingDataListView.as_view()),
        name="table-readings",
    ),
    path("users/", login_required(UsersListView.as_view()), name="users"),
    path("notes/", login_required(NoteListView.as_view()), name="note-list"),
    path("notes/new/", login_required(create_notepad_view), name="create-note"),
]
