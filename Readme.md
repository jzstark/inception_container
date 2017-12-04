# Inception Container

This repo provides scripts for building a containers that provides simple RESTful API for image recognition.

## Usage

Pull and start docker container:

```
docker run --name inception -d -p 5000:5000 -v /tmp/inception_img:/tmp/inception_img matrixanger/inception_container
```

The service is hosted on port 5000. For test, run `curl 127.0.0.1:5000`, and the expected response is a string "Hello, World!".

## API Description

Accept image as a base64-encoded string. The image is decoded and temporarily saved in `/tmp/inception_img`.

```
URL: /image
Method: GET

Parameters:
<content>: a base64-encoded image string
<type>: a string that represents image type, such as "jpeg" and "png".

{
    "image":{
      "content": "/9j/7QBEUGhvdG9zaG9...image contents...fXNWzvDEeYxxxzj/Coa6Bax//Z",
      "type": "png"
    }
}
```

An example in Python can be seen in [request_example.py](https://github.com/jzstark/inception_container/blob/master/request_example.py).

## Response

Response: json string that contains the top-5 classification result ("class") and probability ("prop"). Example:

```
[
  {
    "class": "giant panda,
     panda,
     panda bear,
     coon bear,
     Ailuropoda melanoleuca",
    "prop":  0.961965441704
  },
  {
    "class": "lesser panda,
     red panda,
     panda,
     bear cat,
     cat bear,
     Ailurus fulgens",
    "prop":  0.00117377145216
  },
  {
    "class": "space shuttle",
    "prop":  0.000592212367337
  },
  {
    "class": "soccer ball",
    "prop":  0.000403530168114
  },
  {
    "class": "indri,
     indris,
     Indri indri,
     Indri brevicaudatus",
    "prop":  0.000263019668637
  }
]
```
