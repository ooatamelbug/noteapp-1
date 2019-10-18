from rest_framework import routers
# from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    Userview,
    NoteCreateview,
    NoteDeleteview,
    NoteListview,
    NoteUpdateview,
    NoteRetriveview,
    UserCreateview
    # createuser
    )
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
router = routers.DefaultRouter()

router.register(r'user', Userview, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('reg/', UserCreateview.as_view(), name='reg-user'),
    path('note/show/', NoteListview.as_view(), name='list-note'),
    path('note/create/', NoteCreateview.as_view(), name='create-note'),
    path('note/<int:pk>/edit/', NoteUpdateview.as_view(), name='update-note'),
    path('note/<int:pk>/delete/', NoteDeleteview.as_view(), name='delete-note'),
    path('note/<int:pk>/', NoteRetriveview.as_view(), name='one-note'),
    path('auth/', obtain_auth_token, name='auth'),
]


# urlpatterns = format_suffix_patterns(urlpatterns)
