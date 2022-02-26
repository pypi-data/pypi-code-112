#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# queue.py: adapted from uasyncio V2
# https://github.com/peterhinch/micropython-async/blob/a87bda1b716090da27fd288cc8b19b20525ea20c/v3/primitives/queue.py

# Copyright (c) 2018-2020 Peter Hinch
# Released under the MIT License (MIT) - see LICENSE file

# Code is based on Paul Sokolovsky's work.
# This is a temporary solution until uasyncio V3 gets an efficient official version

import uasyncio as asyncio


# Exception raised by get_nowait().
class QueueEmpty(Exception):
    pass


# Exception raised by put_nowait().
class QueueFull(Exception):
    pass


class Queue(object):
    def __init__(self, maxsize: int = 0):
        self.maxsize = maxsize
        self._queue = []
        self._evput = asyncio.Event()  # Triggered by put, tested by get
        self._evget = asyncio.Event()  # Triggered by get, tested by put

    def _get(self):
        self._evget.set()  # Schedule all tasks waiting on get
        self._evget.clear()
        return self._queue.pop(0)

    async def get(self):
        # Usage: item = await queue.get()
        while self.empty():  # May be multiple tasks waiting on get()
            # Queue is empty, suspend task until a put occurs
            # 1st of N tasks gets, the rest loop again
            await self._evput.wait()
        return self._get()

    def get_nowait(self):
        # Remove and return an item from the queue.
        # Return an item if one is immediately available, else raise QueueEmpty
        if self.empty():
            raise QueueEmpty()
        return self._get()

    def _put(self, val):
        # Schedule tasks waiting on put
        self._evput.set()
        self._evput.clear()
        self._queue.append(val)

    async def put(self, val):
        # Usage: await queue.put(item)
        while self.full():
            # Queue full
            await self._evget.wait()
            # Task(s) waiting to get from queue, schedule first Task
        self._put(val)

    def put_nowait(self, val):
        # Put an item into the queue without blocking.
        if self.full():
            raise QueueFull()
        self._put(val)

    def qsize(self):
        # Number of items in the queue.
        return len(self._queue)

    def empty(self):
        # Return True if the queue is empty, False otherwise.
        return len(self._queue) == 0

    def full(self):
        # Return True if there are maxsize items in the queue.
        # Note: if the Queue was initialized with maxsize=0 (the default) or
        # any negative number, then full() is never True.
        return self.maxsize > 0 and self.qsize() >= self.maxsize
