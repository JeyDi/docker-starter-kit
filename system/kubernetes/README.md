# Kind

Kind è uno strumento che consente di creare un semplice cluster di test in locale per imparare a smanettare o per sviluppare con Kubernetes.

È molto veloce e semplice da usare.

Attenzione: Ricordarsi sempre di installare kubectl
- https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/


## Comandi utili:
```bash

# create cluster with yml config
kind create cluster --name test --config kind-ha.yaml

#delete cluster 
kind destroy cluster --name test



```
