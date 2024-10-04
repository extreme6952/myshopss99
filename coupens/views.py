from django.shortcuts import render,redirect

from django.utils import timezone

from .forms import CouponeForm

from .models import Coupone

from django.views.decorators.http import require_POST



@require_POST
def coupone_field(request):

    now = timezone.now()

    forms = CouponeForm(request.POST)

    if forms.is_valid():

        code = forms.cleaned_data['code']

        try:

            coupone = Coupone.objects.get(
                code__iexact=code,
                valid_from__lte=now,
                valid_to__gte=now,
                active=True
            )

            request.session['coupone_id'] = coupone.id

        except Coupone.DoesNotExist:

            request.session['coupone_id'] = None


    return redirect('cart:cart_detail')

