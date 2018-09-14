Title: Deploying on Kubernetes using CircleCI and Kubetpl
Date: 2018-08-21 22:00
Category: Kubernetes
Tags: kubernetes, circleci, kubetpl
Cover: https://github.com/MarcDufresne/m0rk-blog/raw/master/m0rk-theme/static/img/banners/circleci-kubetpl-deployment.png

In a [previous article]({filename}/kubernetes-templating.md) we saw how to turn our Kubernetes
resource files into configurable templates using `kubetpl`. This time we will be going a bit further
and integrating `kubetpl` templates into a CircleCI configuration. This is a good way to deploy new versions
of your app automatically when new code is pushed. A great start for a Continuous Delivery (CD) system.

First, you will have to use a Docker image with `kubetpl` and `kubectl` installed, I recommend you use
my own image, `marcdufresne/kubetpl-base` which has both those tools installed already and is based on Debian.
You can check the Dockerfile used to build it on the
[blog's examples repo](https://github.com/MarcDufresne/m0rk-blog-examples/tree/master/kubetpl-circleci-deploy).
Using this image is quite simple, just add the `docker` section in your job definition, like so:

```yaml
docker:
  - image: marcdufresne/kubetpl-base:0.7.1
```

Alternatively you can create your own image, or simply run the `kubectl` and `kubetpl` installation steps directly
from your CircleCI configuration.

Then, proceed with doing a code `checkout` and any other steps you might want to do before deployment.
For example, if your app's Docker image isn't built and pushed yet you could do this here.

Now we only have two more steps, the first one will be configuring your cluster info and endpoints for `kubectl`.
To do this I recommend you prepare your `config.yaml` file and store the Base64 encoded contents in a
CircleCI Environment Variable (CircleCI Project Settings > Build Settings > Environment Variables).
Here's how you can do this on your local machine:

```bash
$ cat my_kubernetes_config.yaml | base64
```

Then in your CircleCI configuration file add the following to your job steps, assuming your Kubernetes Cluster config
is under the `KUBE_CONFIG` environment variable.

```yaml
- run:
  name: Create Kube config file
  command: |
    mkdir -p ~/.kube/
    echo -n $KUBE_CONFIG | base64 -d >> ~/.kube/config
```

Lastly, now that `kubectl` is properly configured it's time to render your Kubernetes resource template and apply
it to your cluster. The example below does just that and assumes your app's Docker image tag is the commit's hash,
which is available under `CIRCLE_SHA1`.

```yaml
- run:
  name: Deploy to Kubernetes
  command: |
    kubetpl render -i base.env resources.yaml \
      -s DOCKER_TAG=$CIRCLE_SHA1
      | kubectl apply -f -
```

And that's it, your Kubernetes cluster is now updated and your app will be deployed. Additionally, you can repeat the
last step for any other template you may have, like Services and Ingresses.

You can find the full example of the above files on the
[blog's examples repo](https://github.com/MarcDufresne/m0rk-blog-examples/tree/master/kubetpl-circleci-deploy).
