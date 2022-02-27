#!/usr/bin/env python
#
# Python-bindings handle type test script
#
# Copyright (C) 2015-2022, Joachim Metz <joachim.metz@gmail.com>
#
# Refer to AUTHORS for acknowledgements.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import argparse
import os
import random
import sys
import unittest

import pyphdi


class HandleTypeTests(unittest.TestCase):
  """Tests the handle type."""

  def test_signal_abort(self):
    """Tests the signal_abort function."""
    phdi_handle = pyphdi.handle()

    phdi_handle.signal_abort()

  def test_open(self):
    """Tests the open function."""
    test_source = unittest.source
    if not test_source:
      raise unittest.SkipTest("missing source")

    phdi_handle = pyphdi.handle()

    phdi_handle.open(test_source)

    with self.assertRaises(IOError):
      phdi_handle.open(test_source)

    phdi_handle.close()

    with self.assertRaises(TypeError):
      phdi_handle.open(None)

    with self.assertRaises(ValueError):
      phdi_handle.open(test_source, mode="w")

  def test_open_file_object(self):
    """Tests the open_file_object function."""
    test_source = unittest.source
    if not test_source:
      raise unittest.SkipTest("missing source")

    if not os.path.isfile(test_source):
      raise unittest.SkipTest("source not a regular file")

    phdi_handle = pyphdi.handle()

    with open(test_source, "rb") as file_object:

      phdi_handle.open_file_object(file_object)

      with self.assertRaises(IOError):
        phdi_handle.open_file_object(file_object)

      phdi_handle.close()

      with self.assertRaises(TypeError):
        phdi_handle.open_file_object(None)

      with self.assertRaises(ValueError):
        phdi_handle.open_file_object(file_object, mode="w")

  def test_close(self):
    """Tests the close function."""
    test_source = unittest.source
    if not test_source:
      raise unittest.SkipTest("missing source")

    phdi_handle = pyphdi.handle()

    with self.assertRaises(IOError):
      phdi_handle.close()

  def test_open_close(self):
    """Tests the open and close functions."""
    test_source = unittest.source
    if not test_source:
      return

    phdi_handle = pyphdi.handle()

    # Test open and close.
    phdi_handle.open(test_source)
    phdi_handle.close()

    # Test open and close a second time to validate clean up on close.
    phdi_handle.open(test_source)
    phdi_handle.close()

    if os.path.isfile(test_source):
      with open(test_source, "rb") as file_object:

        # Test open_file_object and close.
        phdi_handle.open_file_object(file_object)
        phdi_handle.close()

        # Test open_file_object and close a second time to validate clean up on close.
        phdi_handle.open_file_object(file_object)
        phdi_handle.close()

        # Test open_file_object and close and dereferencing file_object.
        phdi_handle.open_file_object(file_object)
        del file_object
        phdi_handle.close()

  def test_read_buffer(self):
    """Tests the read_buffer function."""
    test_source = unittest.source
    if not test_source:
      raise unittest.SkipTest("missing source")

    phdi_handle = pyphdi.handle()

    phdi_handle.open(test_source)
    phdi_handle.open_extent_data_files()

    media_size = phdi_handle.get_media_size()

    if media_size < 4096:
      # Test read without maximum size.
      phdi_handle.seek_offset(0, os.SEEK_SET)

      data = phdi_handle.read_buffer()

      self.assertIsNotNone(data)
      self.assertEqual(len(data), media_size)

    # Test read with maximum size.
    phdi_handle.seek_offset(0, os.SEEK_SET)

    data = phdi_handle.read_buffer(size=4096)

    self.assertIsNotNone(data)
    self.assertEqual(len(data), min(media_size, 4096))

    if media_size > 8:
      phdi_handle.seek_offset(-8, os.SEEK_END)

      # Read buffer on media_size boundary.
      data = phdi_handle.read_buffer(size=4096)

      self.assertIsNotNone(data)
      self.assertEqual(len(data), 8)

      # Read buffer beyond media_size boundary.
      data = phdi_handle.read_buffer(size=4096)

      self.assertIsNotNone(data)
      self.assertEqual(len(data), 0)

    # Stress test read buffer.
    phdi_handle.seek_offset(0, os.SEEK_SET)

    remaining_media_size = media_size

    for _ in range(1024):
      read_size = int(random.random() * 4096)

      data = phdi_handle.read_buffer(size=read_size)

      self.assertIsNotNone(data)

      data_size = len(data)

      if read_size > remaining_media_size:
        read_size = remaining_media_size

      self.assertEqual(data_size, read_size)

      remaining_media_size -= data_size

      if not remaining_media_size:
        phdi_handle.seek_offset(0, os.SEEK_SET)

        remaining_media_size = media_size

    with self.assertRaises(ValueError):
      phdi_handle.read_buffer(size=-1)

    phdi_handle.close()

    # Test the read without open.
    with self.assertRaises(IOError):
      phdi_handle.read_buffer(size=4096)

  def test_read_buffer_file_object(self):
    """Tests the read_buffer function on a file-like object."""
    test_source = unittest.source
    if not test_source:
      raise unittest.SkipTest("missing source")

    if not os.path.isfile(test_source):
      raise unittest.SkipTest("source not a regular file")

    with open(test_source, "rb") as file_object:
      phdi_handle = pyphdi.handle()

      phdi_handle.open_file_object(file_object)

      extent_data_file_objects = []
      for extent_descriptor in phdi_handle.extent_descriptors:
        extend_data_file_path = os.path.join(
          os.path.dirname(test_source), extent_descriptor.filename)
        extend_data_file_object = open(extend_data_file_path, "rb")
        extent_data_file_objects.append(extend_data_file_object)

      phdi_handle.open_extent_data_files_as_file_objects(
          extent_data_file_objects)

      media_size = phdi_handle.get_media_size()

      # Test normal read.
      data = phdi_handle.read_buffer(size=4096)

      self.assertIsNotNone(data)
      self.assertEqual(len(data), min(media_size, 4096))

      phdi_handle.close()

      for extend_data_file_object in extent_data_file_objects:
        extend_data_file_object.close()

  def test_read_buffer_at_offset(self):
    """Tests the read_buffer_at_offset function."""
    test_source = unittest.source
    if not test_source:
      raise unittest.SkipTest("missing source")

    phdi_handle = pyphdi.handle()

    phdi_handle.open(test_source)
    phdi_handle.open_extent_data_files()

    media_size = phdi_handle.get_media_size()

    # Test normal read.
    data = phdi_handle.read_buffer_at_offset(4096, 0)

    self.assertIsNotNone(data)
    self.assertEqual(len(data), min(media_size, 4096))

    if media_size > 8:
      # Read buffer on media_size boundary.
      data = phdi_handle.read_buffer_at_offset(4096, media_size - 8)

      self.assertIsNotNone(data)
      self.assertEqual(len(data), 8)

      # Read buffer beyond media_size boundary.
      data = phdi_handle.read_buffer_at_offset(4096, media_size + 8)

      self.assertIsNotNone(data)
      self.assertEqual(len(data), 0)

    # Stress test read buffer.
    for _ in range(1024):
      random_number = random.random()

      media_offset = int(random_number * media_size)
      read_size = int(random_number * 4096)

      data = phdi_handle.read_buffer_at_offset(read_size, media_offset)

      self.assertIsNotNone(data)

      remaining_media_size = media_size - media_offset

      data_size = len(data)

      if read_size > remaining_media_size:
        read_size = remaining_media_size

      self.assertEqual(data_size, read_size)

      remaining_media_size -= data_size

      if not remaining_media_size:
        phdi_handle.seek_offset(0, os.SEEK_SET)

    with self.assertRaises(ValueError):
      phdi_handle.read_buffer_at_offset(-1, 0)

    with self.assertRaises(ValueError):
      phdi_handle.read_buffer_at_offset(4096, -1)

    phdi_handle.close()

    # Test the read without open.
    with self.assertRaises(IOError):
      phdi_handle.read_buffer_at_offset(4096, 0)

  def test_seek_offset(self):
    """Tests the seek_offset function."""
    test_source = unittest.source
    if not test_source:
      raise unittest.SkipTest("missing source")

    phdi_handle = pyphdi.handle()

    phdi_handle.open(test_source)
    phdi_handle.open_extent_data_files()

    media_size = phdi_handle.get_media_size()

    phdi_handle.seek_offset(16, os.SEEK_SET)

    offset = phdi_handle.get_offset()
    self.assertEqual(offset, 16)

    phdi_handle.seek_offset(16, os.SEEK_CUR)

    offset = phdi_handle.get_offset()
    self.assertEqual(offset, 32)

    phdi_handle.seek_offset(-16, os.SEEK_CUR)

    offset = phdi_handle.get_offset()
    self.assertEqual(offset, 16)

    if media_size > 16:
      phdi_handle.seek_offset(-16, os.SEEK_END)

      offset = phdi_handle.get_offset()
      self.assertEqual(offset, media_size - 16)

    phdi_handle.seek_offset(16, os.SEEK_END)

    offset = phdi_handle.get_offset()
    self.assertEqual(offset, media_size + 16)

    # TODO: change IOError into ValueError
    with self.assertRaises(IOError):
      phdi_handle.seek_offset(-1, os.SEEK_SET)

    # TODO: change IOError into ValueError
    with self.assertRaises(IOError):
      phdi_handle.seek_offset(-32 - media_size, os.SEEK_CUR)

    # TODO: change IOError into ValueError
    with self.assertRaises(IOError):
      phdi_handle.seek_offset(-32 - media_size, os.SEEK_END)

    # TODO: change IOError into ValueError
    with self.assertRaises(IOError):
      phdi_handle.seek_offset(0, -1)

    phdi_handle.close()

    # Test the seek without open.
    with self.assertRaises(IOError):
      phdi_handle.seek_offset(16, os.SEEK_SET)

  def test_get_offset(self):
    """Tests the get_offset function."""
    test_source = unittest.source
    if not test_source:
      raise unittest.SkipTest("missing source")

    phdi_handle = pyphdi.handle()

    phdi_handle.open(test_source)
    phdi_handle.open_extent_data_files()

    offset = phdi_handle.get_offset()
    self.assertIsNotNone(offset)

    phdi_handle.close()

  def test_get_media_size(self):
    """Tests the get_media_size function and media_size property."""
    test_source = unittest.source
    if not test_source:
      raise unittest.SkipTest("missing source")

    phdi_handle = pyphdi.handle()

    phdi_handle.open(test_source)

    media_size = phdi_handle.get_media_size()
    self.assertIsNotNone(media_size)

    self.assertIsNotNone(phdi_handle.media_size)

    phdi_handle.close()

  def test_get_number_of_extents(self):
    """Tests the get_number_of_extents function and number_of_extents property."""
    test_source = unittest.source
    if not test_source:
      raise unittest.SkipTest("missing source")

    phdi_handle = pyphdi.handle()

    phdi_handle.open(test_source)

    number_of_extents = phdi_handle.get_number_of_extents()
    self.assertIsNotNone(number_of_extents)

    self.assertIsNotNone(phdi_handle.number_of_extents)

    phdi_handle.close()


if __name__ == "__main__":
  argument_parser = argparse.ArgumentParser()

  argument_parser.add_argument(
      "source", nargs="?", action="store", metavar="PATH",
      default=None, help="path of the source file.")

  options, unknown_options = argument_parser.parse_known_args()
  unknown_options.insert(0, sys.argv[0])

  setattr(unittest, "source", options.source)

  unittest.main(argv=unknown_options, verbosity=2)
