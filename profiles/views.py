from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm


# Create your views here.
def profile(request):
    """ Display profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/profile.html'
    context = {
        
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)