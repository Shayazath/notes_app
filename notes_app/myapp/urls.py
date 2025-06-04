from django.urls import path
from .views import SignupView, NotesView, MyLoginView, login_page, signup_page, notes_page
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/notes/', NotesView.as_view(), name='notes'),
    path('', login_page, name='home'),
    path('signup-form/', signup_page, name='signup_form'),
    path('signin-form/', login_page, name='login_form'),
    path('notes-page/', notes_page, name='notes_page'),
    path('api/notes/<uuid:note_id>/', NotesView.as_view(), name='delete_note'),

]
