from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader 
from django.urls import reverse
from django.views import generic 

from .models import Review, Tip
from .forms import ReviewForm


class IndexView(generic.ListView): 
	template_name = 'dev/review_list.html'
	context_object_name = 'latest_review_list'

	def get_queryset(self): 
		return Review.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Review
    template_name = 'dev/review_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['choice_form'] = ChoiceCreateForm()
        return context

    def post(self, request, pk):
        tip = get_object_or_404(Tip, pk=pk)
        form = ReviewForm(request.POST)

        if form.is_valid():
            rating = form.cleaned_data['rating']
            comment = form.cleaned_data['comment']
            user_name = form.cleaned_data['user_name']
            review = Review()
            review.tip = tip
            review.user_name = user_name
            review.rating = rating
            review.comment = comment
            review.pub_date = datetime.datetime.now()
            review.save()
            return HttpResponseRedirect(reverse('polls:detail', args=[pk]))

        # else if form is not valid
        return render(request, 'dev/tip_detail.html', {'tip': tip, 'form': form})


def tip_list(request):
    wine_list = Wine.objects.order_by('-name')
    context = {'tip_list':tip_list}
    return render(request, 'dev/tip_list.html', context)


def tip_detail(request, pk):
    wine = get_object_or_404(Tip, pk=pk)
    form = ReviewForm()

    return render(request, 'dev/tip_detail.html', {'tip': tip, 'form': form})

def add_review(request, pk):
    tip = get_object_or_404(Tip, pk=pk)
    form = ReviewForm(request.POST)

    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        user_name = form.cleaned_data['user_name']
        review = Review()
        review.tip = tip
        review.user_name = user_name
        review.rating = rating
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        review.save()
    
        return HttpResponseRedirect(reverse('dev:tip_detail', args=(tip.id,)))

    return render(request, 'dev/tip_detail.html', {'tip': tip, 'form': form})


