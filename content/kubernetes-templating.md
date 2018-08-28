Title: Templating Kubernetes Resource Files
Date: 2018-08-20 22:00
Category: Kubernetes
Tags: kubernetes, kubetpl


When deploying web applications, or any other type of application, it is
often needed or at least very useful to have different versions (or stages)
of it deployed. Those usually are Dev, Staging, Production and so on. However,
it becomes quite a pain to manage different versions of each of your
[Kubernetes](https://kubernetes.io/) resource files.

Enter [`kubetpl`](https://github.com/shyiko/kubetpl), a templating engine purpose
built for Kubernetes resource files. It works across all major OSes and is super easy
to install and use. Here are some of its features:

- Multiple choice of template flavors. Choose from Bash, Go or Template style.
- Support for loading `.env` files.
- Fail fast in case of undefined variable(s).

Let's go through the initial setup and example usage below.

First, you will need to download `kubetpl` and add it to your `$PATH`. To download on
macOS or Linux you can use the following command, and on Windows you can get the
executable [here](https://github.com/shyiko/kubetpl/releases).

```bash
$ curl -o kubetpl \
    -sSL https://github.com/shyiko/kubetpl/releases/download/0.7.1/kubetpl-0.7.1-$(
      bash -c '[[ $OSTYPE == darwin* ]] && echo darwin || echo linux'
    )-amd64
$ chmod a+x kubetpl
```

Once you're done with the steps above you can move `kubetpl` to a directory that's
on your `$PATH`. One possible location is `/usr/local/bin`, here's how we can move
the program there:

```bash
$ mv kubetpl /usr/local/bin/
```

_On Linux you'll most likely need to use `sudo` to move the file_

You should now be able to use `kubetpl` directly from anywhere.

Now, let's get to the main event, writing our templates and rendering them with `kubetpl`.

You will want to start by creating your template file(s), let's look at the example below. It defines a Deployment
of one [`redis`](https://redis.io/) container, exposed to the cluster via a Service. We will be using the Bash style
templating (note the `# kubetpl:syntax:$` line at the beginning).

**`resources.yaml`**
```yaml
# kubetpl:syntax:$
---
kind: Deployment
apiVersion: apps/v1
metadata:
  name: $DEPLOYMENT_NAME
  namespace: $STAGE
spec:
  replicas: 1
  selector:
    matchLabels:
      app: $APP_LABEL
  template:
    spec:
      containers:
        - name: $CONTAINER_NAME
          image: redis:$DOCKER_TAG
          ports:
            containerPort: 6379
            protocol: TCP
            name: $PORT_NAME
    metadata:
      labels:
        app: $APP_LABEL

---
kind: Service
apiVersion: v1
metadata:
  name: $SERVICE_NAME
  namespace: $STAGE
spec:
  type: NodePort
  ports:
    - port: $SERVICE_PORT
      targetPort: 6379
      protocol: TCP
  selector: $APP_LABEL
```

As you can see we can use variables for any value inside the file. Now let's render this template. `kubetpl` provides
the `render` command to, you guessed it, render a template, we can also pass values for our variables using the `-s`
argument, let's try it:

```bash
$ kubetpl render resources.yaml \
    -s DEPLOYMENT_NAME="redis-deployment" \
    -s SERVICE_NAME="redis-service" \
    -s STAGE="staging" \
    -s APP_LABEL="app-redis" \
    -s CONTAINER_NAME="container-redis" \
    -s DOCKER_TAG="5.0-rc" \
    -s PORT_NAME="redis-port" \
    -s SERVICE_PORT=7777

```

This will output the rendered template to your console, you can use this to validate that your result makes sense.
Now, as you can see it becomes quite tedious to enter all those values in the command line every time we have to
render a template. A better option is to use the `-i` argument, which allows you to load a `.env` file containing
your values. It can also be combined with `-s` for convenience, which allows you to set or override values.

Here's an example of `.env` file:

**`base.env`**
```dotenv
DEPLOYMENT_NAME="redis-deployment"
SERVICE_NAME="redis-service"
STAGE="staging"
APP_LABEL="app-redis"
CONTAINER_NAME="container-redis"
DOCKER_TAG="5.0-rc"
PORT_NAME="redis-port"
SERVICE_PORT=7777
```

With this we can simply run the command below to achieve the same result as earlier.

```bash
$ kubetpl render -i base.env resources.yaml
```

Or maybe we want to change the `SERVICE_PORT` and `DOCKER_TAG`.

```bash
$ kubetpl render -i base.env resources.yaml \
    -s SERVICE_PORT=8888 \
    -s DOCKER_TAG="4.0.11"
```

And then, once you are satisfied with your templates you can pipe the output tu `kubectl` to apply your changes
directly on your cluster.

```bash
$ kubetpl render -i base.env resources.yaml | kubectl apply -f -
```

So that was the introduction to `kubetpl` basics. Here are some things you might want to try next:

- Overriding the number of replicas for each stage.
- Trying different tags for your images.
- Setting up your container's environment variables.
- Configuring your domain names per stage.
- Etc.

You can find the full example of the above files on the
[blog's examples repo](https://github.com/MarcDufresne/m0rk-blog-examples/tree/master/kubetpl-templates).
