import boto3
import streamlit as st


# use your AWS bucket keys
s3 = boto3.client('s3', 
                  aws_access_key_id='AKIIAVN4OGAPCIY3XYJHM',
                  aws_secret_access_key='7szzYHWKVNxX7YEsJTO+6cQvC7O6QBPLswkyALM00')

# use your AWS bucket name
bucket_name = 'dmytrobuck'

st.title('Upload Your photos')

local_path = st.text_input('Enter Your local path with images',
                           help="path folder on your PC",
                           placeholder=r'C:\Users\Adrian\Pictures')
cloud_path = st.text_input('Enter new folder name', help="Example:  my_vacation", placeholder='vacation')

uploaded_files = st.file_uploader('Choose images to upload',
                                  accept_multiple_files=True,
                                  type=['png', 'jpg', 'jpeg']  # add more types ?
                                  )

def files_to_bucket(uploaded_files, local_path: str, bucket_name: str):
    """Upload files via streamlit to AWS S3 bucket"""
    for image in uploaded_files:
        file_path = local_path + '\\' + image.name
        s3.upload_file(file_path, bucket_name, f'uploaded_images/{cloud_path}/{image.name}')
        print(f'File was uploaded :{image.name}')


if uploaded_files != None:
    files_to_bucket(uploaded_files, local_path, bucket_name)
