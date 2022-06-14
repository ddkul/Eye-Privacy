#!/usr/bin/env bash

docker exec -it model_server bash

docker cp model_server:/code/model/eyesave1.png /path/eye_privacy/images

docker cp model_server:/code/model/eyesave2.png /path/eye_privacy/images
