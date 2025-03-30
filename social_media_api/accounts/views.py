from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import CustomUser
from .serializers import UserRegistrationSerializer, UserProfileSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.create(user=user)
        return Response({
            "user": serializer.data,
            "token": token.key
        }, status=201)

class UserListView(generics.ListAPIView):  # New view for listing users
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()  # Explicit queryset declaration

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()  # Added explicit queryset

    def get_object(self):
        return self.request.user
    
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()
    lookup_url_kwarg = 'user_id'

    def post(self, request, *args, **kwargs):
        user_to_follow = self.get_object()
        current_user = request.user

        if current_user == user_to_follow:
            return Response(
                {"error": "You cannot follow yourself"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if current_user.following.filter(id=user_to_follow.id).exists():
            return Response(
                {"error": "You are already following this user"},
                status=status.HTTP_400_BAD_REQUEST
            )

        current_user.following.add(user_to_follow)
        return Response(
            {"status": f"Successfully followed {user_to_follow.username}"},
            status=status.HTTP_200_OK
        )

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()
    lookup_url_kwarg = 'user_id'

    def delete(self, request, *args, **kwargs):
        user_to_unfollow = self.get_object()
        current_user = request.user

        if current_user == user_to_unfollow:
            return Response(
                {"error": "You cannot unfollow yourself"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not current_user.following.filter(id=user_to_unfollow.id).exists():
            return Response(
                {"error": "You are not following this user"},
                status=status.HTTP_400_BAD_REQUEST
            )

        current_user.following.remove(user_to_unfollow)
        return Response(
            {"status": f"Successfully unfollowed {user_to_unfollow.username}"},
            status=status.HTTP_200_OK
        )