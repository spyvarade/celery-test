'''

==============================================================================================

What is Redis?
	Redis is an open-source, advance key value data store and cache. It is also referred as a data structure server which keys not only contains strings, but also hashes, sets, lists, and sorted sets.

==============================================================================================
Celery:

	Celery is an asynchronous task queue/job queue based on distributed message passing. It is focused on real-time operations but supports scheduling as well. The execution units, called tasks, are executed concurrently on one or more worker servers using multiprocessing, Eventlet, or gevent. Tasks can execute asynchronously (in the background) or synchronously (wait until ready).

Where we use celery:
	Scenario 1 - Report generation and export

What is a Broker?
	In Celery broker is a mediator between clients and workers. The main task of the broker is to deliver the client messages to a worker.

What is Celery worker?
	Celery worker is a supervisor process that does not process any tasks itself rather than that Celery spawns child processes (or threads) and deals with all the book keeping stuff.

What is Celery backend?
	Celery backend is a storage place that is used for storing the task results.Currently Celery supports only AMQP, database, cache, Couchbase, and Redis backends.

What is Celerybeat?		
	Celerybeat is a task scheduler that sends predefined tasks to a celery worker at a given time.

What is Pub-Sub in Celery?
	Pub-Sub expended as publish-subscribe or producer-consumer is a distributed messaging pattern where publishers broadcast messages over a message broker, and subscribers listen for the messages.

'''