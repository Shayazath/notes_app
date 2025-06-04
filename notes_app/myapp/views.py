from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Note
from .serializer import SignupSerializer, NoteSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import MyTokenObtainPairSerializer

class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created!"}, status=201)
        return Response(serializer.errors, status=400)

class NotesView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        notes = Note.objects.filter(user=request.user)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    def delete(self, request, note_id=None):
        if not note_id:
            return Response({"detail": "Note ID required"}, status=400)

        try:
            note = Note.objects.get(note_id=note_id, user=request.user)
            note.delete()
            return Response({"detail": "Deleted"}, status=204)
        except Note.DoesNotExist:
            return Response({"detail": "Note not found"}, status=404)
class MyLoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


def signup_page(request):
    return render(request, 'signup.html')

def login_page(request):
    return render(request, 'login.html')

def notes_page(request):
    return render(request, 'notes.html')
