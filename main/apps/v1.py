from django.urls import include, path


urlpatterns = [
    path(
        "user/",
        include(
            ("main.apps.user.urls", "main.apps.user.urls"),
            namespace="user",
        ),
    ),
    path(
        "field/",
        include(
            ("main.apps.field.urls", "main.apps.field.urls"),
            namespace="field",
        ),
    ),
    path(
        "booking/",
        include(
            ("main.apps.booking.urls", "main.apps.booking.urls"),
            namespace="booking",
        ),
    ),
]