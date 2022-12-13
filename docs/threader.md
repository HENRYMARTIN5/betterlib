# Betterlib Threader

This module contains the Threader class, which is a simple and easy to use thread manager that can also be used to get the output of a function in a thread.

This module consists of the following classes:

## Threader

The thread manager.

### Constructor

The constructor takes the following arguments:

- `target` - The function to run.
- `args` - The arguments to pass to the function.
- `kwargs` - The keyword arguments to pass to the function.
- `numThreads=1` - The number of threads to use.

### Methods

- `join()` - Waits for all threads to finish.
- `joinAndReturn()` - Waits for all threads to finish and returns the output of the function.
- `isAlive()` - Returns whether or not the thread is alive.

## BetterThread

The internal thread class.

### Constructor

The constructor takes the following arguments:

- `group=None` - The thread group.
- `target=None` - The function to run.
- `name=None` - The name of the thread.
- `args=()` - The arguments to pass to the function.
- `kwargs={}` - The keyword arguments to pass to the function.

### Methods

- `run()` - Runs the thread.
- `join()` - Waits for the thread to finish and returns the value outputted by the function.
