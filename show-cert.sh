#!/bin/bash
podname=$(kubectl get po -o json | jq -r '.items[0].metadata.name')
kubectl exec -it $podname -- cat /home/mitmproxy/.mitmproxy/mitmproxy-ca-cert.cer
