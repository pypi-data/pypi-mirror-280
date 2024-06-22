#
# Copyright (c) 2021 The GPflux Contributors.
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
#
"""
The library root. See :mod:`~gpflux.models.deep_gp.DeepGP` for the core Deep GP model,
which is built out of different GP :mod:`~gpflux.layers`.
"""
from gpflux import callbacks, encoders, helpers, layers, losses, models, optimization, sampling
from gpflux.version import __version__
