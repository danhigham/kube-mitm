kubectl delete -f mitm-config-map.yml
kubectl delete -f mitm-deployment.yml
kubectl create -f mitm-config-map.yml
kubectl create -f mitm-deployment.yml
