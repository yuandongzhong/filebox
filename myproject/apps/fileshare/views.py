from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.static import serve

from .forms import TeamFileForm
from .models import TeamFile


@method_decorator(login_required, name='dispatch')
class HomeView(View):
    def get(self, request):
        files_list = TeamFile.objects.all()
        return render(self.request, 'fileshare/index.html', {'team_files': files_list})

    def post(self, request):
        form = TeamFileForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            team_file = form.save()
            # upload_date = timezone.localtime(
            #     team_file.uploaded_at).strftime('%y%m%d%H%M')
            data = {'is_valid': True,
                    'name': team_file.filename(),
                    'url': team_file.file.url,
                    'uploaded_at': team_file.uploaded_at.strftime('%Y年%-m月%d日 %H:%M')}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


@login_required
def clear_database(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'please log in'})
    for team_file in TeamFile.objects.all():
        team_file.file.delete()
        team_file.delete()
    return redirect(request.POST.get('next'))


@login_required
def protected_serve(request, path, document_root=None, show_indexes=False):
    return serve(request, path, document_root, show_indexes)
