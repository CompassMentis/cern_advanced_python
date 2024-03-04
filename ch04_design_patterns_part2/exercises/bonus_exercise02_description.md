# Bonus exercise

- Start with your code from the pizzeria exercise

The observers are now going to be a separate process - running in a separate terminal

This will be based on the Proxy Pattern

The proxy will consists of two parts:
1. main part: in the current code, in front of the current Observer abstract base class
instead of calling the observer's call back code (which then shows the result), it writes the data to a file, as follows:
[sequence number]message
2. new process: reads the file every 0.1 seconds. Process any new messages (based on the sequence number)
