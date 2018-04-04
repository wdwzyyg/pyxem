# -*- coding: utf-8 -*-
# Copyright 2018 The pyXem developers
#
# This file is part of pyXem.
#
# pyXem is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyXem is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyXem.  If not, see <http://www.gnu.org/licenses/>.

import numpy as np
import pytest
from pyxem.signals.crystallographic_map  import CrystallographicMap

@pytest.fixture()
def sp_cryst_map():
    #sp for single phase
    base = np.zeros((4,6))
    base[0] = [0,5,17,6,3e-17,0.5]
    base[1] = [0,6,17,6,2e-17,0.4]
    base[2] = [0,12,3,6,4e-17,0.3]
    base[3] = [0,12,3,5,8e-16,0.2]
    crystal_map = CrystallographicMap(base.reshape((2,2,6)))
    return crystal_map

def test_get_phase_map(sp_cryst_map):
    pmap = sp_cryst_map.get_phase_map()
    assert pmap.inav[0,0] == 0

def test_get_correlation_map(sp_cryst_map):
    cmap = sp_cryst_map.get_correlation_map()
    assert cmap.inav[0,0] == 3e-17

def test_get_reliability_map_orientation(sp_cryst_map):
    rmap = sp_cryst_map.get_reliabilty_map_orientation()
    assert rmap.inav[0,0] == 0.5
