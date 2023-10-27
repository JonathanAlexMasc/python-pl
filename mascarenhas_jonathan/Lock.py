from abc import ABC, abstractmethod

class Lock:
    def __init__(self, behavior=None):
        self._locked = False
        self._depth = 0
        self._behavior = behavior

    @property
    def depth(self):
        return self._depth

    def lock(self):
        if not self._locked:
            self._locked = True
            self._depth += 1
            if self._behavior:
                self._behavior.lock()

    def unlock(self):
        if self._locked and self._depth > 0:
            self._depth -= 1
            if self._depth == 0:
                self._locked = False
            if self._behavior:
                self._behavior.unlock()


# Example usage:

# lock = Lock()
#
# print(f"Lock is initially at depth {lock.depth}")
#
# lock.lock()
# print(f"Lock is now at depth {lock.depth}")
#
# lock.lock()
# print(f"Lock is now at depth {lock.depth}")
#
# lock.unlock()
# print(f"Lock is now at depth {lock.depth}")
#
# lock.unlock()
# print(f"Lock is now at depth {lock.depth}")
#
# lock.unlock()
# print(f"Lock is now at depth {lock.depth}")
