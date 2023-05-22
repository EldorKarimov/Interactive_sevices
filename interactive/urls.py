from django.urls import path
from .views import SendDataView, RequestListView, RequestAnswerDetailView, AcceptListView, AnswerDeleteView, RequestDeleteView

urlpatterns = [
    path('', SendDataView.as_view(), name = 'send_data'),
    path('answers/', AcceptListView.as_view(), name = 'answers'),
    path('answers/<int:id>/delete/', AnswerDeleteView.as_view(), name = 'answer_delete'),
    path('requests/', RequestListView.as_view(), name = 'requests'),
    path('requests/answer/detail/<str:num>', RequestAnswerDetailView.as_view(), name = 'request_answer_detail'),
    path('requests/delete/<str:num>/', RequestDeleteView.as_view(), name = 'request_delete')
]