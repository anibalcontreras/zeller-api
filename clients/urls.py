from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet
from conversations.views import ConversationViewSet
from debts.views import DebtViewSet

router = DefaultRouter()
router.register(r"clients", ClientViewSet, basename="client")

conversation_router = DefaultRouter()
conversation_router.register(r"clients", ConversationViewSet, basename="conversation")

debt_router = DefaultRouter()
debt_router.register(r"clients", DebtViewSet, basename="debt")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(conversation_router.urls)),
    path("", include(debt_router.urls)),
]
