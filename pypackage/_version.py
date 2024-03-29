# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Reads in version information.
Note: This file will be overwritten by the packaging process."""
import os

directory_of_this_file = os.path.dirname(os.path.abspath(__file__))

with open(f"{directory_of_this_file}/../VERSION.txt", "r") as f:
    __version__ = f.read().strip()
