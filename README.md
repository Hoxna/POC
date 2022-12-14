# About

The project makes it possible to use the nerfstudio by using web UI.
It is intended for using on AWS cloud servers.

In addition to this repository you need use also Streamlit with QStash, https://github.com/Mrhetsko/streamlit 

# Quickstart

## 1. Installation: 
Tested with nerfstudio==0.1.14 version
Install nerfstudio 0.1.14 on cloud server, https://github.com/nerfstudio-project/nerfstudio
```bash
python -m pip install nerfstudio==0.1.14
````
After nerfstudio installed you need to make two changes in nerfstudio code:
 - navigate to 
```cd nerfstudio/nerfstudio/configs```
   - change file ```experiment_config.py```,- after "config_yaml_path = base_dir / "config_yml" (line 121) add next:
   - ```with open('/home/ubuntu/files/path.txt', 'w') as file:```
   ```file.write(f'{config_yaml_path}')```
and second:
   - in base_config.py
   - quit_on_train_completion: bool = False CHANGE to True

### requirements:
```python -m pip install -r requirements.txt```

CUDA must be installed on the system. Has been tested with version 11.7. Installing CUDA [here](https://docs.nvidia.com/cuda/cuda-quick-start-guide/index.html)

## 2. nginx
To be able to access django app with ip address you need install nginx server
https://ubuntu.com/tutorials/install-and-configure-nginx#4-setting-up-virtual-host
```sudo apt update```,
```sudo apt install nginx```
change server_name:

```sudo nano /etc/nginx/sites-available/default```, change "servet_name" to your ip address
and restart nginx ```sudo service nginx restart```

## 3. Streamlit and QStash


We use the QStash as a part of Streamlit app to create a queue of model training in case we have many machines
At the same time Streamlit upload users images and creates a task (message) for QStash application, after that QStash 
send request to free training machine.
  Go to Qstash https://console.upstash.com/qstash, SignIn, open QStash tab. Create your Topic and set the endpoint/s.
On the details tab you can generate your own cURL command and convert it to Python code here https://www.scrapingbee.com/curl-converter/python/


## Run
activate your conda environment, navigate to datatruck folder, run
```python manage.py runserver```
now django app will be able on cloud server ip address






## Diagram

![image](https://user-images.githubusercontent.com/2309907/209835984-00d70920-20b9-4fc8-8f8e-9847731bd9b2.png)


```
Mobile App
S3
Upstash Queue
NerfStudio

simulated with webpage:note --> Mobile App
django:note --> NerfStudio

Mobile App-upload images->S3
Mobile App-convert request->Upstash Queue
NerfStudio-pull job->Upstash Queue
NerfStudio-download images->S3
NerfStudio-convert->NerfStudio
NerfStudio-upload 3d->S3
Mobile App-get 3D->S3

```

## Connection between Unity application and backend

![gleek-cUiIFGU1GzozjlUtyXxJOg (2)](https://user-images.githubusercontent.com/2309907/210619536-e267c969-1a14-409e-a8e6-3b9581dac4e4.png)

```
Unity
S3
Backend
Queue
Training

Unity-create project->Backend
Backend-S3 url to upload images->Unity

Unity-upload images/video->S3
Unity-training->Backend

Backend-training->Queue
Queue-tarining->Training
Training-upload 3D->S3

Unity-get project details->Backend
Backend-S3 url to 3d model->Unity
Unity-download 3d model->S3
```

