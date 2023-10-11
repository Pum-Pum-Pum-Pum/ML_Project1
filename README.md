# ML_Project1
Machine Learning journey has begun!
'''
docker build -t <image_name>:<tagname>
'''
>note: Image name for the docker must always be lowercase

to list docker image
'''
docker images
'''

to run docker image, p is port number while running pass 5000 as port. Image ID get from docket images command 


docker run -p <port>:<port> -e PORT=<port> <IMAGE ID from docker images>
'''
docker run -p 5000:5000 -e PORT=5000 d1ca34f8ff9d
'''
to check running containers in dockers
'''
docker ps
'''
to stop image, get container id using docker ps
'''
docker stop <Container_ID>
'''

This needs to be cleaned up later.

Install ipykernel

'''
pip install ipykernel
'''