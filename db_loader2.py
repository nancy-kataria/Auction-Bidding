import argparse
import datetime
import datetime, time
import mysql.connector as conn
import config

from confluent_kafka import Consumer
from confluent_kafka.serialization import SerializationContext, MessageField
from confluent_kafka.schema_registry.json_schema import JSONDeserializer
from confluent_kafka.schema_registry import SchemaRegistryClient

API_KEY, ENDPOINT_SCHEMA_URL, API_SECRET_KEY, BOOTSTRAP_SERVER, SECURITY_PROTOCOL, SSL_MECHANISM, SCHEMA_REGISTRY_API_KEY, SCHEMA_REGISTRY_API_SECRET, GOOGLE_MAP_API_KEY = config.config_values()

# This function returns a dictionary with SASL (Simple Authentication and Security Layer) configuration settings required for connecting to Kafka.
def sasl_conf():
    sasl_conf = {'sasl.mechanism': SSL_MECHANISM,
                 # Set to SASL_SSL to enable TLS support.
                 #  'security.protocol': 'SASL_PLAINTEXT'}
                 'bootstrap.servers': BOOTSTRAP_SERVER,
                 'security.protocol': SECURITY_PROTOCOL,
                 'sasl.username': API_KEY,
                 'sasl.password': API_SECRET_KEY
                 }
    return sasl_conf

# This function returns a dictionary with configuration settings for connecting to the Schema Registry, which stores the schemas for the Kafka topics.
# configurations for the Schema registry
def schema_config():
    return {'url': ENDPOINT_SCHEMA_URL,
            'basic.auth.user.info': f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

            }

def main(topic):
    schema_registry_conf = schema_config()
    schema_registry_client = SchemaRegistryClient(schema_registry_conf)

    my_schema = schema_registry_client.get_latest_version(topic+'-value').schema.schema_str

    json_deserializer = JSONDeserializer(my_schema,
                                         from_dict=None)
    consumer_conf = sasl_conf()

    consumer_conf.update({
        'group.id': 'group1',
        'auto.offset.reset': "earliest"}) # or earliest, latest

    # Initializes the Kafka consumer with the specified configuration.
    consumer = Consumer(consumer_conf)
    # Subscribes the consumer to the given Kafka topic.
    consumer.subscribe([topic])

    counter = 0
    while True:
        try:
            # SIGINT can't be handled when polling, limit timeout to 1 second.
            # Polls the Kafka topic for new messages with a timeout of 1 second.
            msg = consumer.poll(1.0)
            if msg is None:
                continue

            # de-serialize the message
            # Deserializes the message value from JSON into a Python dictionary.
            bid = json_deserializer(msg.value(), SerializationContext(msg.topic(), MessageField.VALUE))

            if bid is not None:
                # Increments a counter to keep track of the number of messages processed.
                counter += 1
                print('Current timestamp:', datetime.datetime.now())
                print("User record {}: bid: {}"
                      .format(msg.key(), bid))
                print('Total messages fetched till now:', counter)

            name = bid['name']
            price = bid['price']
            city = bid['city']
            state = bid['state']
            lat = bid['lat']
            lng = bid['lng']
            bid_ts = bid['bid_ts']

            # Captures the current time to measure how long it takes to insert the record into the database.
            sql_ts = time.time()

            # Create DB connection and insert records
            try:
                # some process
                # time.sleep(3)

                # Connects to the MySQL database
                cnx = conn.connect(host="localhost", user="root",
                                   passwd="radhaSwami123", database="bidding_data")
                # Creates a cursor object to execute SQL commands
                cur = cnx.cursor()
                query = "insert into bids (name, price, city, state, lat, lng, bid_ts) values ( %s, %s, %s, %s, %s, %s, %s)"
                data = (name, price, city, state, lat, lng, bid_ts)

                # Executes the SQL command with the bid data
                cur.execute(query, data)

                # Commits the transaction, making the insertion permanent
                cnx.commit()
                print(cur.rowcount, " record is successfully added")

                # Closes the cursor and database connection
                cur.close()
                cnx.close()
                print('seconds spent to insert record:', time.time() - sql_ts)
                print('seconds spent from web page to table:',
                      time.time() - time.mktime(time.strptime(bid_ts, '%Y-%m-%d %H:%M:%S')))
                print('-------------------------------')

            # Handles any errors that occur during the database operations.
            except conn.Error as err:
                # Handles errors related to incorrect database credentials
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Something is wrong with your user name or password")
                # Handles errors related to a non-existent database
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Database does not Exist")
                else:
                    print(err)
                err.error()


        # Allows the program to exit gracefully when interrupted by the user
        # eg: Ctrl+C
        except KeyboardInterrupt:
            break

    # Closes the Kafka consumer, ensuring that all resources are properly released
    consumer.close()

main("auction")