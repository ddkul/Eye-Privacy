# Eye-Privacy

This repository emulates a privacy-preserving framework for transferring images of an individual's eye to a remote model for gaze and emotion detection. This method combines the principles of the additive secret-sharing [[1]](#1) and Bluetooth transmission schemes [[2]](#2). In this strategy, the image to be transmitted is split into a fixed number of pieces, and these splits are sent to a random subset of intermediate servers, amongst a set of available servers. These intermediate servers then forward the received splits to the remote model server.

We use Docker Engine to simulate seven containers, each behaving as an independent server, connected to the same network. Out of the six servers, one was the application server, one was the remote model server, one was an adversarial server, while the remaining four functioned as the intermediate transmitting servers A, B, C, and D. The servers use APIs to communicate with each other built using FastAPI. To demonstrate the privacy scheme, we set up a replay attack scenario. The application server split and sent two images, one after another, according to the identification number and servers' sequence. A replay attacker captures the split that arrives at server A, and replays it when the second image is sent. It is assumed that an out-of-band channel is used to exchange the random number generator seed for identification numbers and corresponding sequences between the application server and remote model server.

To simulate -
```python
docker-compose build
docker-compose up
```
To retrieve images in the model server container (update path) -
```python
sh copy_images.sh
```
The endpoint to split images is available on http://0.0.0.0/splitimgs
The endpoint for replaying the first image's split once it has been received at the model server is http://0.0.0.0:90/replaysplit.

## References
<a id="1">[1]</a> 
Adi Shamir. “How to Share a Secret”. In: Commun. ACM 22.11 (1979), 612–613.

<a id="2">[2]</a> 
Jaap Haartsen. “Bluetooth-The universal radio interface for ad hoc, wireless connectivity”.
In: Ericsson review 3.1 (1998), pp. 110–117.
