from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet
from conversations.views import ConversationViewSet

router = DefaultRouter()
router.register(r"clients", ClientViewSet, basename="client")

conversation_router = DefaultRouter()
conversation_router.register(r"clients", ConversationViewSet, basename="conversation")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(conversation_router.urls)),
]
