from django.urls import path
from .views import TransactionCreateView, TransactionListView, TransactionDetailView

urlpatterns = [
    # POST /api/transactions/
    path('api/transactions/create/', TransactionCreateView.as_view(), name='transaction-create'),

    # GET /api/transactions/?user_id=<user_id>
    path('api/transactions/', TransactionListView.as_view(), name='transaction-list'),

    # GET /api/transactions/<transaction_id>/
    # PUT /api/transactions/<transaction_id>/
    path('api/transactions/<int:transaction_id>/', TransactionDetailView.as_view(), name='transaction-detail'),
]
