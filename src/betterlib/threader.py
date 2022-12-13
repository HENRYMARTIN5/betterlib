"""
This module provides a simple way to create threads in Python. It is a wrapper for the threading module.
"""

import threading

class Threader:
    """
    A simple wrapper for the threading module.
    """

    def __init__(self, target, args=(), kwargs={}, numThreads=1):
        """
        Creates a new thread or set of threads. Parameters:

        target: The function to run in the thread.
        args: A list of arguments to pass to the function. Defaults to None.
        kwargs: A dictionary of keyword arguments to pass to the function. Defaults to None.
        num_threads: The number of threads to create. Defaults to 1.
        """

        if numThreads == 1:
            self.multithread = False
            self.thread = BetterThread(target=target, args=args, kwargs=kwargs)
            self.thread.start()
            return

        self.multithread = True
        self.threads = []
        for i in range(numThreads):
            self.threads.append(BetterThread(target=target, args=args, kwargs=kwargs))
            self.threads[i].start()


    def join(self):
        """
        Joins the thread or threads without returning any data passed.
        """

        if self.multithread:
            for thread in self.threads:
                thread.join()
        else:
            self.thread.join()
    
    def isAlive(self):
        """
        Returns whether or not the thread is alive. If there are more than one thread, this will return True if any of them are alive.
        """

        if self.multithread:
            for thread in self.threads:
                if thread.is_alive():
                    return True
            return False
        else:
            return self.thread.is_alive()

    def joinAndReturn(self):
        """
        Joins all threads and returns the data returned by the thread. If there is more than one thread, this will return a list of the returned data from each thread.
        """

        if self.multithread:
            returned_data = []
            for thread in self.threads:
                returned_data.append(thread.join())
            return returned_data
        else:
            return self.thread.join()

class BetterThread(threading.Thread):
    """
    A better thread class that allows you to get the return value of the function called.
    """

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}):
        """
        Constructor, just like threading.Thread.__init__().
        """

        threading.Thread.__init__(self, group, target, name, args, kwargs)

    def run(self):
        """
        Run the thread, just like threading.Thread.run().
        """

        if self._target != None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self, *args):
        """
        Join the thread, just like threading.Thread.join(), except it returns the return value of the function called.
        """

        threading.Thread.join(self, *args)
        return self._return
    

if __name__ == '__main__':
    print("This module is not meant to be run directly.")
    exit(1)