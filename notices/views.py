from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context, loader, RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.utils import timezone

from notices.models import Notice

# the main view, just returns a list of all the notices
def notices(request):
    noticeList = Notice.objects.all().order_by('-pub_date')
    return render_to_response('index.html', {'noticeList': noticeList},
            context_instance = RequestContext(request))

def new(request):
    """ add a new notice to the board
    """
    notice = Notice(notice=request.POST['text_input'],
            pub_date=timezone.now())
    notice.save()
    return HttpResponseRedirect(reverse('notices.views.notices'))

def edit(request, notice_id):
    """ Edit an existing notice
    """
    notice = Notice.objects.get(pk=notice_id)
    notice.pub_date = timezone.now()
    notice.notice = request.POST['text_input']
    notice.save()
    return HttpResponseRedirect(reverse('notices.views.notices'))

def delete(request, notice_id):
    # attempt to find the notice that was passed, then delete it
    notice = Notice.objects.get(pk=notice_id)
    notice.delete()
    return HttpResponseRedirect(reverse('notices.views.notices'))
