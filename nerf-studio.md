# Nerf-studio

Project use simple one page Django application available on http://52.206.155.58/.

Two important things has to be changed in nerfstudio package:
add 2 lines
boolean to true


On cloud machine activate virtual environment ```conda activate nerfstudio```, navigate to '/datatruck/' folder and run django app ```python manage.py runserver```.
Now web page is available on http://52.206.155.58/ or http://52.206.155.58:80, where you can input your folder name (preloaded with streamlit uploader) and press "Convert" button.
Your images will be converted to point_cloud.ply, file will be available with streamlit uploader.(Process take about 90-100 minutes)