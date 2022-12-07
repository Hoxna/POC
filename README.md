# POC

## Diagram

![image](https://user-images.githubusercontent.com/2309907/206215878-a8fc6f85-7645-4c54-b36f-6a4056b40a32.png)

```
Mobile App
S3
NerfStudio

simulated with webpage:note --> Mobile App
django:note --> NerfStudio

Mobile App-upload images->S3
Mobile App-convert request->NerfStudio
NerfStudio-download images->S3
NerfStudio-convert->NerfStudio
NerfStudio-upload 3d->S3
Mobile App-get 3D->S3
```
