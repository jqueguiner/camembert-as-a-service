
API implementation for Image Super Resolution:
https://github.com/idealo/image-super-resolution

# Docker for API

You can build and run the docker using the following process:

Cloning
```console
git clone https://github.com/jqueguiner/super-resolution.git super-resolution
```

Building Docker
```console
cd super-resolution && docker build -t super-resolution -f Dockerfile .
```

Running Docker
```console
echo "http://$(curl ifconfig.io):5000" && docker run -p 5000:5000 -d super-resolution
```

Calling the API
```console
curl -X POST "http://MY_SUPER_API_IP:5000/process" -H "accept: image/jpg" -H "Content-Type: application/json" -d '{"url":""}' --output super_resolution.jpg
```
