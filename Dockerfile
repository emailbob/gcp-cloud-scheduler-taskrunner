FROM python:2.7.15-alpine3.7
RUN pip install --upgrade google-api-python-client \
    && pip install --upgrade oauth2client \
    && pip install python-dateutil \
    && apk add --no-cache --virtual .build-deps curl \
    && curl -O http://storage.googleapis.com/aju-sd-traffic/unzipped/Freeways-5Minaa2010-01-01_to_2010-02-15_test2.csv

COPY entrypoint.sh /entrypoint.sh
COPY cloud_handler.py /cloud_handler.py
COPY cron_executor.py /cron_executor.py
COPY exec_payload.py /exec_payload.py
COPY logger_sample_task.py /logger_sample_task.py
COPY test_executor.py /test_executor.py
COPY shell_sample_task.sh /shell_sample_task.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]