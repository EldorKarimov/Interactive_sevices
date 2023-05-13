from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .models import SendData, AnswerData
from .forms import SendDataForm, AnswerDataForm

class SendDataView(LoginRequiredMixin, View):
    def get(self, request):
        form = SendDataForm()
        send_datas = SendData.objects.all().order_by('-created_at')[:1]
        context = {
            'form':form,
            'send_datas':send_datas
        }
        return render(request, 'main.html', context)
    def post(self, request):
        form = SendDataForm(request.POST, request.FILES)
        if form.is_valid():
            create_form = form.save(commit=False)
            create_form.user = request.user
            create_form.save()
            return redirect('send_data')
        else:
            return render(request, 'main.html', {'form':form})

# class AnswersView(LoginRequiredMixin, View):
#     def get(self, request):
#         search_answer = request.GET.get('search_answer', '')
#         if search_answer:
#             try:
#                 answer = AnswerData.objects.get(num = search_answer)
#                 x = True
#             except:
#                 x = False
#                 answer = 'No Information Found'
#         else:
#             answer = 'enter id to get reply'
#             x = False
#         return render(request, 'answer.html', {'answer':answer, 'x':x, 'search_answer':search_answer})

class RequestListView(View, LoginRequiredMixin):
    def get(self, request):
        send_data = SendData.objects.all().order_by('-created_at')
        context = {
            'send_data':send_data
        }
        return render(request, 'request_list.html', context)

class RequestAnswerDetailView(LoginRequiredMixin, View):
    def get(self, request, num):
        get_send_data = SendData.objects.get(num = num)
        context = {
            'get_send_data':get_send_data
        }
        return render(request, 'request_answer_detail.html', context)

    def post(self, request, num):
        send_data = SendData.objects.get(num = num)
        form = AnswerDataForm(data=request.POST)
        if form.is_valid():
            form_create = form.save(commit=False)
            form_create.username = send_data.user.username
            form_create.leader = send_data.leader
            form_create.save()
            return redirect('requests')
        else:
            return render(request, 'request_answer_detail.html', {'form':form})

class AcceptListView(LoginRequiredMixin, View):
    def get(self, request):
        answer_data = AnswerData.objects.filter(username = request.user.username).order_by('-id')
        context = {
            'answer_data':answer_data
        }
        return render(request, 'answer.html', context)
