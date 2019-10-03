# Docker/K8s geojson validation service
Simple python/flask server to validate geojson data

## docker deployment

### build Docker image
`docker build . -t geojson`

### run Docker Image locally
`docker-compose -f docker-compose.yml up -d`

### test server
`curl -X POST -H "Content-Type: application/json" -d @examples/aoi.geojson http://localhost:8080/`

### stop Docker deployment
`docker-compose down`

## K8s deployment

### When using minikube do the following extra steps

####  load minikube docker env
`eval $(minikube docker-env)`

#### build the container image
`docker build . -t geojson`

#### enable ingress controller
`minikube addons enable ingress`

#### determine minikube external ip
`minikube ip`

#### add following line to /etc/hosts file
`$(minikuke ip) geojson.local`

### apply K8s objects to Kubernetes
`kubectl apply -f k8s/`

### test server
`curl --header "Content-Type: application/json" --data @examples/aoi.geojson.broken http://geojson.local`

### scale the deployment
`kubectl scale deployment geojson --replicas=2`
