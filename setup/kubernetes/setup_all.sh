#!/bin/bash

set -x
set -e

openssl rand -hex 32

read -p "Did you set the secretToken in config.yaml (y/n)? " answer
case ${answer:0:1} in
    y|Y )
        echo Yes
    ;;
    * )
        exit 1
    ;;
esac


./setup_cluster.sh

sleep 1

./setup_helm.sh

sleep 1

./setup_jupyterhub.sh passthru

while True; do

	kubectl get pods

	kubectl get service --namespace jhub

	sleep 1
done
