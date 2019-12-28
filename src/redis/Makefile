zrob:
    docker build . -t redis1
    docker run --rm -v $(pwd)/volume:/data/:rw -d -p 6379:6379 --name redisd redis1