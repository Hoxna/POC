# Access to AWS cloud machine with SSH key
You need SSH - key.pem

### commands:
#
for help:
## ns-render --help
#

Go to folder with SSH key.pem on your PC and input in CLI to get access to server:

## ssh -i "key.pem" user_name@server_address_here.compute-1.amazonaws.com
#

activate your project enviroment:
## conda activate project_name
#

Copy file "111.txt" from local machine to server in home/ubuntu folder, -r flag needed for folders:
## scp -i "key.pem" 111.txt user_name@server_address_here.compute-1.amazonaws.com:/home/ubuntu
#
Move files in linux:
## mv from to




#
SCP command for secure file transfer----------  [SCP command link](https://linuxize.com/post/how-to-use-scp-command-to-securely-transfer-files/)