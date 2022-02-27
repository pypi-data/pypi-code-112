# -*- coding: utf-8 -*-
# MinIO Python Library for Amazon S3 Compatible Cloud Storage,
# (C) 2016-2020 MinIO, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import datetime, timezone

from minio import Minio
from minio.commonconfig import REPLACE, CopySource

client = Minio(
    "play.min.io",
    access_key="Q3AM3UQ867SPQQA43P2F",
    secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
)

# copy an object from a bucket to another.
result = client.copy_object(
    "my-bucket",
    "my-object",
    CopySource("my-sourcebucket", "my-sourceobject"),
)
print(result.object_name, result.version_id)

# copy an object with condition.
result = client.copy_object(
    "my-bucket",
    "my-object",
    CopySource(
        "my-sourcebucket",
        "my-sourceobject",
        modified_since=datetime(2014, 4, 1, tzinfo=timezone.utc),
    ),
)
print(result.object_name, result.version_id)

# copy an object from a bucket with replacing metadata.
metadata = {"test_meta_key": "test_meta_value"}
result = client.copy_object(
    "my-bucket",
    "my-object",
    CopySource("my-sourcebucket", "my-sourceobject"),
    metadata=metadata,
    metadata_directive=REPLACE,
)
print(result.object_name, result.version_id)
