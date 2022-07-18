Errors detected during execution are called exceptions and are not unconditionally fatal: you will soon learn how to handle them in Python programs. Most exceptions are not handled by programs, however, and result in error messages
It is possible to write programs that handle selected exceptions. Look at the following example, which asks the user forinput until a valid integer has been entered, but allows the user to interrupt the program (using Control-C or whateverthe operating system supports); note that a user-generated interruption is signalled by raising the KeyboardInterrupt exception.