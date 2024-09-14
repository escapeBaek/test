from django.shortcuts import render, get_object_or_404
from .models import Exam, Question, ExamResult
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from accounts.decorators import user_is_specially_approved
import json

# Only approved users can access the exam landing page
@login_required
@user_is_specially_approved
def exam_landing_page(request):
    return render(request, 'exam/landing_page.html')

# Exam list view (only specially approved users can view the exam list)
@login_required
@user_is_specially_approved
def exam_list(request):
    exams = Exam.objects.all()
    return render(request, 'exam/exam_list.html', {'exams': exams})

# Exam detail view (only specially approved users can view exam details)
@login_required
@user_is_specially_approved
def exam_detail(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    return render(request, 'exam/exam_detail.html', {'exam': exam})

# Question list for a specific exam (only specially approved users can view)
@login_required
@user_is_specially_approved
def question_list(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    questions = exam.questions.all().order_by('order')
    return render(request, 'exam/question_list.html', {'exam': exam, 'questions': questions})

# Save exam results (only logged-in users can save exam results)
@login_required
@user_is_specially_approved
def save_exam_results(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        exam_id = data.get('exam_id')
        num_correct = data.get('num_correct')
        num_incorrect = data.get('num_incorrect')
        num_unanswered = data.get('num_unanswered')
        num_noanswer = data.get('num_noanswer')
        detailed_results = data.get('detailed_results')

        exam = get_object_or_404(Exam, id=exam_id)
        user = request.user

        result = ExamResult.objects.create(
            user=user,
            exam=exam,
            num_correct=num_correct,
            num_incorrect=num_incorrect,
            num_unanswered=num_unanswered,
            num_noanswer=num_noanswer,
            detailed_results=detailed_results,
        )

        return JsonResponse({'status': 'ok', 'result_id': result.id})
    else:
        return JsonResponse({'status': 'error'}, status=400)

# View for exam results (only the user who took the exam can view their results)
@login_required
def exam_results(request):
    result_id = request.GET.get('result_id')
    result = get_object_or_404(ExamResult, id=result_id, user=request.user)
    return render(request, 'exam/exam_results.html', {'result': result})
