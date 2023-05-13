from django.urls import path
from .views import SendDataView, RequestListView, RequestAnswerDetailView, AcceptListView

urlpatterns = [
    path('', SendDataView.as_view(), name = 'send_data'),
    path('answers/', AcceptListView.as_view(), name = 'answers'),
    path('requests/', RequestListView.as_view(), name = 'requests'),
    path('requests/answer/detail/<str:num>', RequestAnswerDetailView.as_view(), name = 'request_answer_detail'),
]