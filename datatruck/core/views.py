from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from .import cargo as cli


@csrf_exempt
def index(request):
    if request.method == "POST":
        user_folder = request.POST.get('project_name')
        if cli.aws_truck.folder_exists(user_folder):
            message = f'Folder name: "{user_folder}"'

            cli.aws_truck.bucket_to_ns(user_folder)
            cli.process_data(user_folder)
            cli.ns_train(user_folder)
            cli.ns_export(user_folder)
            cli.aws_truck.ns_to_bucket(user_folder)
            return render(request, 'core/index.html', {'message': message})

        else:
            message = f'There are no folder with name: "{user_folder}"'
            return render(request, 'core/index.html', {'message': message})
    return render(request, 'core/index.html')

