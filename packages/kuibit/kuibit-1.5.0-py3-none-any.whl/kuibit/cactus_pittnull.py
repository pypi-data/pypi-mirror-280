#!/usr/bin/env python3

# Copyright (C) 2022-2024 Gabriele Bozzola
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, see <https://www.gnu.org/licenses/>.

from __future__ import annotations

import os
import re

import h5py

from kuibit.simdir import SimDir


class PittNullOne:
    def __init__(self, files: list[str]) -> None:
        ...

        # We read off all the metadata to ensure that they are consistent. To do
        # so, we put them in sets and see how many elements they end up having
        Rin: set[float] = set()
        Rout: set[float] = set()
        dim: set[tuple[int, int]] = set()
        spin: set[int] = set()

        for f in files:
            with h5py.File(f) as h5f:
                # We unpack the metadata because they are saved as arrays
                Rin.add(*h5f["metadata"].attrs["Rin"])
                Rout.add(*h5f["metadata"].attrs["Rout"])

                # We make the array hashable so that we can add it to the set
                dim.add(tuple(h5f["metadata"].attrs["dim"]))

                spin.add(*h5f["metadata"].attrs["spin"])

        if len(Rin) != 1:
            raise RuntimeError(f"Multiple/no values of Rin found: {Rin}")
        if len(Rout) != 1:
            raise RuntimeError(f"Multiple/no values of Rout found: {Rout}")
        if len(dim) != 1:
            raise RuntimeError(f"Multiple/no values of dim found: {dim}")
        if len(spin) != 1:
            raise RuntimeError(f"Multiple/no values of dim found: {spin}")

        # We are clear. Now we set the metadata with set unpacking
        (self.Rin,) = Rin
        (self.Rout,) = Rout
        (self.dim,) = dim
        (self.spin,) = spin


class PittNullDir:
    def __init__(self, sd: SimDir) -> None:
        """Constructor.

        :param sd:  SimDir object providing access to data directory.
        :type sd:   SimDir

        """
        # First, we organize all the metric_obs_D_Decomp.h5 files
        #
        # _pitt_files is a dictionary whose keys are the radius indices (0, 1,
        # ...) and values the list of the files associated to that index.
        self._pitt_files: dict[int, list[str]] = {}

        rx_filename = re.compile(r"^metric_obs_(\d+)_Decomp.h5$")
        for path in sd.allfiles:
            filename = os.path.split(path)[-1]
            matched = rx_filename.search(filename)
            if matched is not None:
                rad_index = int(matched.group(1))
                self._pitt_files.setdefault(rad_index, []).append(path)

        # We cache what we have already read
        self._pitt_ones: dict[int, PittNullOne] = {}

    def __getitem__(self, rad_index: int) -> PittNullOne:
        return PittNullOne(self._pitt_files[rad_index])
