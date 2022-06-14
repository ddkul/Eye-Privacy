#!/usr/bin/env bash

docker exec -it model_server bash

docker cp model_server:/code/model/eyesave1.png /home/divya/Documents/fastapi-projects/eye_privacy/images

docker cp model_server:/code/model/eyesave2.png /home/divya/Documents/fastapi-projects/eye_privacy/images
