from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from ninja import Router
from rest_framework.authtoken.models import Token

from .schemas import UserCreateSchema, UserSchema
from .serializers import UserProfileSerializer

User = get_user_model()
auth_router = Router()

@auth_router.post("/signup")
def signup(request, payload: UserCreateSchema):
    if User.objects.filter(email=payload.email).exists():
        return {"error": "User with this email already exists"}
    user = User.objects.create_user(
        email=payload.email,
        name=payload.name,
        password=payload.password,
        phone_number=payload.phone_number,
        date_of_birth=payload.date_of_birth,
        address=payload.address,
        gender=payload.gender,
    )
    return {"message": "User created successfully"}

@auth_router.post("/login")
def login(request, email: str, password: str):
    user = authenticate(email=email, password=password)
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return {"token": token.key}
    else:
        return {"error": "Invalid credentials"}

@auth_router.get("/profile", auth=True)
def profile(request):
    user = request.auth
    profile_data = UserProfileSerializer(user).data
    return profile_data
