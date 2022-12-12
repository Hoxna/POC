from django.shortcuts import render

from .import cargo as cli


def index(request):
    if request.method == "POST":
        user_folder = request.POST.get('bucket_path')
        if cli.aws_truck.folder_exists(user_folder):
            message = f'Folder name: "{user_folder}"'
            cli.aws_truck.bucket_to_ns(user_folder)
            #  printing output  for test on local server
            print('Command Bucket to NS')
            print('--------')
            cli.process_data(user_folder)
            print('Command process data')
            print('--------')
            cli.ns_train(user_folder)
            print('Command train')
            return render(request, 'core/index.html', {'message': message})

        else:
            message = f'There are no folder with name: "{user_folder}"'
            return render(request, 'core/index.html', {'message': message})
    return render(request, 'core/index.html')

