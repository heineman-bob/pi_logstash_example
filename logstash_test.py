import logging
import logstash
import sys
import psutil
import os
import time

host = '192.168.0.113'
port = 5000
delay = os.environ.get('DELAY')
if delay == None:
    delay = 15

test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.TCPLogstashHandler(host, port, version=1))

while(True):
    # add extra field to logstash message
    additional_info = {
        'cpu_usage': psutil.cpu_percent(),
        'memory_usage': psutil.virtual_memory().percent,
        'memory_free': psutil.virtual_memory().free,
        'memory_swap': psutil.swap_memory().percent,
        'disk_space_used': psutil.disk_usage('/').percent,
        'network_connections': len(psutil.net_connections()),
        'network_connection_details': psutil.net_connections()
    }

    test_logger.info('pi_stats', extra=additional_info)
    time.sleep(delay)
