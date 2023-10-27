from abc import ABC, abstractmethod
from Lock import Lock

# Define the abstract base class BehaviorLock
class BehaviorLock(ABC):
    @abstractmethod
    def lock(self):
        pass

    @abstractmethod
    def unlock(self):
        pass

# Concrete implementations of BehaviorLock

class PassThrough(BehaviorLock):
    def lock(self):
        print("PassThrough Locking")

    def unlock(self):
        print("PassThrough Unlocking")

class Basic(BehaviorLock):
    def lock(self):
        print("Basic Locking")

    def unlock(self):
        print("Basic Unlocking")

class FastEmpty(BehaviorLock):
    def lock(self):
        print("FastEmpty Locking")

    def unlock(self):
        print("FastEmpty Unlocking")


# Create Lock instances with different behaviors
pass_through_lock = Lock(PassThrough())
basic_lock = Lock(Basic())
fast_empty_lock = Lock(FastEmpty())

# Use the locks
pass_through_lock.lock()  # Output: PassThrough Locking
pass_through_lock.unlock()  # Output: PassThrough Unlocking

basic_lock.lock()  # Output: Basic Locking

fast_empty_lock.lock()  # Output: FastEmpty Locking

