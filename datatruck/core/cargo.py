# from .\
import aws_credentials
import boto3
import subprocess


class Truck:
    def __init__(self, key_id: str, secret_acc_key: str, bucket: str):
        self.key_id = key_id
        self.secret_acc_key = secret_acc_key
        self.bucket = bucket

    @property
    def folder_list(self):
        s3_resource = boto3.resource('s3',
                                     aws_access_key_id=self.key_id,
                                     aws_secret_access_key=self.secret_acc_key
                                     )

        my_bucket = s3_resource.Bucket(self.bucket)
        # full path list
        path_list = [i.key for i in my_bucket.objects.all()]
        # list of all folders in the bucket
        folders_list = [i.split('/')[-2] for i in path_list]
        return set(folders_list)

    def folder_exists(self, folder: str):
        return True if folder in self.folder_list else False

    def bucket_to_ns(self, user_folder):
        subprocess.run(('aws',
                        's3',
                        'cp',
                        f's3://{self.bucket}/uploaded_images/{user_folder}',  # from
                        f'/home/ubuntu/images_from_bucket/{user_folder}',  # to
                        '--recursive'
                        ))
        # for test on local server

        # just_print = ('aws',
        #               's3',
        #               'cp',
        #               f's3://{self.bucket}/uploaded_images/{user_folder}',  # from
        #               f'/home/ubuntu/images_from_bucket/{user_folder}',  # to
        #               '--recursive')
        # return just_print

    def ns_to_bucket(self, user_folder):
        subprocess.run(('aws',
                        's3',
                        'cp',
                        f'/home/ubuntu/trained_models/{user_folder}',  # from
                        f's3://{self.bucket}/models_from_ns/{user_folder}',  # to
                        '--recursive'
                        ))


# --------------------------------------


def process_data(user_folder):
    """Now works only with images"""
    subprocess.run(('ns-process-data',
                    'images',
                    '--data',
                    f'/home/ubuntu/images_from_bucket/{user_folder}',
                    '--output-dir',
                    f'/home/ubuntu/processed_data/{user_folder}'
                    ))

    # result = ('ns-process-data',
    #           'images',
    #           '--data',
    #           f'/home/ubuntu/images_from_bucket/{user_folder}',
    #           '--output-dir',
    #           f'/home/ubuntu/processed_data/{user_folder}')
    # return result


def ns_train(user_folder):
    subprocess.run(('ns-train',
                    'nerfacto',
                    '--data',
                    f'/home/ubuntu/processed_data/{user_folder}',
                    '--output-dir',
                    f'/home/ubuntu/trained_models/{user_folder}'
                    ))

    # result = ('ns-train',
    #           'nerfacto',
    #           '--data',
    #           f'/home/ubuntu/processed_data/{user_folder}',
    #           '--output-dir',
    #           f'/home/ubuntu/trained_models/{user_folder}'
    #           )
    # return result


aws_truck = Truck(aws_credentials.AWSAccessKeyId, aws_credentials.AWSSecretKey, aws_credentials.AWSbucket)

if __name__ == '__main__':
    # print(aws_truck.folder_exists('teft'))
    # print(aws_truck.folder_exists('test'))
    #    print(aws_truck.folder_exists('test'))
    # print(type(aws_truck.folder_list))
    pass
