# Cloud Scheduler Task Scheduling on Google Compute Engine
Container and Cloud Scheduler implementation based off of https://cloud.google.com/solutions/reliable-task-scheduling-compute-engine

Instead of using Google App Engine for the Cron service Cloud Scheduler will be used.

This example shows how to use Cloud Scheduler to send tasks to a GCE instance.

Setup Cloud Scheduler to use the Target Pub/Sub and give it a topic name.

Currently the payload only supports three types of tasks.

- Shell script. Example "shell_sample_task.sh Bob"
- Python script. Example "logger_sample_task.py"
- HTTP endpoint. The example will do a simple curl against it.

Make sure any scripts used are mounted to the contianer.

To extend to use different types of tasks modifiy the file exec_payload.py

### Docker Build

```bash
docker build -t gcp-cloud-scheduler-taskrunner .
```

### Docker Run

Run this on any GCE instances that you want to run tasks on

```bash
docker run --rm -ti -e TOPIC={YOUR_PUBSUB_TOPIC} -e PROJECT={YOUR_PROJECT_ID} thefoo/gcp-cloud-scheduler-taskrunner
```

### Environment variables
```
PROJECT      GCP project id

TOPIC        Pub/Sub Topic
```
