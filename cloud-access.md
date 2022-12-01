# Access to AWS cloud machine with SSH key
You need SSH - key.pem

### commands:

## ns-render --help
for help



## ssh -i "key.pem" user_name@server_address_here.compute-1.amazonaws.com
Go to folder with SSH key.pem on your PC and input in CLI to get access to server

## conda activate project_name
activate your project enviroment


## scp -i "key.pem" 111.txt user_name@server_address_here.compute-1.amazonaws.com:/home/ubuntu

Copy file "111.txt" from local machine to server in home/ubuntu folder, -r flag needed for folders

#
SCP command for secure file transfer----------  [SCP command link](https://linuxize.com/post/how-to-use-scp-command-to-securely-transfer-files/)