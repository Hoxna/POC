from .import aws_credentials
import boto3
import subprocess


class Truck:
    def __init__(self, key_id: str, secret_acc_key: str, bucket: str):
        self.key_id = key_id
        self.secret_acc_key = secret_acc_key
        self.bucket = bucket

    @property
    def folder_list(self):
        """Return path"""
        s3_resource = boto3.resource('s3',
                                     aws_access_key_id=self.key_id,
                                     aws_secret_access_key=self.secret_acc_key)
        images_folder_list = []
        trained_list = []
        my_bucket = s3_resource.Bucket(self.bucket)
        # full path list
        path_list = [obj.key for obj in my_bucket.objects.all()]

        for item in path_list:
            if item.endswith('.png'):
                images_folder_list.append(item.split('/')[-2])
            elif item.endswith('.ply'):
                trained_list.append(item)
        return {'folders': set(images_folder_list),  # separated folders with user images in bucket
                'models': trained_list,  # paths to 3D models for streamlit downloader
                'path_list': set(path_list),
                }

    def folder_exists(self, folder: str):
        """Check if folder with images exist in AWS bucket"""
        return True if folder in self.folder_list['folders'] else False

    def bucket_to_ns(self, user_folder):
        """Copy images from bucket to ns machine"""
        subprocess.run(('aws',
                        's3',
                        'cp',
                        f's3://{self.bucket}/uploaded_images/{user_folder}',     # from
                        f'/home/ubuntu/files/images_from_bucket/{user_folder}',  # to
                        '--recursive'
                        ))

    def ns_to_bucket(self, user_folder):
        subprocess.run(('aws', 's3', 'cp',
                        f'/home/ubuntu/files/pointcloud/{user_folder}/point_cloud.ply',  # from
                        f's3://{self.bucket}/pointcloud/{user_folder}/',                   # to
                        ))


# --------------------------------------


def process_data(user_folder):
    """Now works only with images. Process images to ns format. Preparation for train model"""
    subprocess.run(('ns-process-data',
                    'images',
                    '--sfm-tool', 'hloc',
                    '--feature-type', 'superpoint',
                    '--data', f'/home/ubuntu/files/images_from_bucket/{user_folder}',
                    '--output-dir', f'/home/ubuntu/files/processed_data/{user_folder}'
                    ))


def ns_train(user_folder):
    """Start train process"""
    subprocess.run(['ns-train',
                    'nerfacto',
                    '--data', f'/home/ubuntu/files/processed_data/{user_folder}',
                    '--output-dir', f'/home/ubuntu/files/trained_models/{user_folder}'])


# def ns_train_simulation(user_folder):
#     """Use it on slow computers instead def ns_train. Allows you to simulate train proces in fast mode"""
#     subprocess.run(('ns-train', 'nerfacto',
#                     '--data', f'/home/ubuntu/files/processed_data/{user_folder}',
#                     '--output-dir', f'/home/ubuntu/files/trained_models/simulation/{user_folder}'
#                     '--pipeline.datamanager.train-num-rays-per-batch', '1000',
#                     '--pipeline.model.eval-num-rays-per-chunk', '1000',
#                     '--pipeline.datamanager.eval-num-rays-per-batch', '500',
#                     '--trainer.max-num-iterations', '70'))


def ns_export(user_folder):
    with open(r'/home/ubuntu/files/path.txt', 'r') as path:
        yaml_path = path.read()

    subprocess.run(['ns-export',
                    'pointcloud',
                    '--load-config', f'{yaml_path}',
                    '--output-dir', f'/home/ubuntu/files/pointcloud/{user_folder}/'])


aws_truck = Truck(aws_credentials.AWSAccessKeyId, aws_credentials.AWSSecretKey, aws_credentials.AWSbucket)


if __name__ == '__main__':
    pass
