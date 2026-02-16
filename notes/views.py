from django.db.models import Q
from rest_framework import generics, permissions
from .models import Note
from .serializers import NoteSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView



# Register API
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


# Notes APIs
class NoteListCreateView(generics.ListCreateAPIView):
    serializer_class = NoteSerializer

    

    def get_queryset(self):
        queryset = Note.objects.filter(owner=self.request.user)

        archived = self.request.query_params.get('archived')
        if archived == 'true':
            queryset = queryset.filter(is_archived=True)
        else:
            queryset = queryset.filter(is_archived=False)

        search = self.request.query_params.get('search')
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(content__icontains=search)
            )

        return queryset



    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)
