from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm
from .models import Tweet,Comment,Profile
from .forms import TweetForm



def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request,'webpages/tweet_list.html',{'tweets':tweets})

@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'webpages/tweet_form.html', {'form': form})

@login_required
def tweet_edit(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'webpages/tweet_form.html', {'form': form})

@login_required
def tweet_delete(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk, user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'webpages/tweet_confirm_delete.html', {'tweet': tweet})

# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password1']) #imp method 
#             user.save()
#             login(request, user)
#             return redirect('login')
#     else:
#         form = UserRegistrationForm()
#     return render(request,'registration/register.html',{"form":form})

def contact(request):
    return render(request,'webpages/contactus.html')

def search(request):
    query = request.GET.get('q')
    results = Tweet.objects.filter(text__icontains=query) if query else None
    return render(request, 'webpages/search_results.html', {'results': results, 'query': query})

def tweet_details(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    comments = Comment.objects.filter(tweet=tweet)  # Fetch comments related to the tweet
    return render(request, "webpages/tweet_details.html", {'tweet': tweet, 'comments': comments})


@login_required
def add_comment(request, pk):
    if request.method == "POST":
        tweet = get_object_or_404(Tweet, pk=pk)
        Comment.objects.create(
            tweet=tweet,
            user=request.user,
            text=request.POST.get('comment')
        )
    return redirect('tweet_details', pk=pk)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'webpages/profile.html', {'profile': profile})