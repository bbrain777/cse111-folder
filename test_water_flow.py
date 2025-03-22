import pytest
from water_flow import (water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe,
                        pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction, kPa_to_psi)

# Test for water column height
def test_water_column_height():
    assert abs(water_column_height(36.6, 9.1) - 27.5) < 0.001
    assert abs(water_column_height(50, 25) - 25) < 0.001

# Test for pressure gain from water height
def test_pressure_gain_from_water_height():
    assert abs(pressure_gain_from_water_height(27.5) - 269.197) < 0.001
    assert abs(pressure_gain_from_water_height(100) - 978.9) < 0.001  # Corrected expected value

# Test for pressure loss from pipe due to friction
def test_pressure_loss_from_pipe():
    assert abs(pressure_loss_from_pipe(0.28687, 1524, 0.013, 1.65) + 93.8423) < 0.001
    assert abs(pressure_loss_from_pipe(0.28687, 1000, 0.013, 1.65) + 61.576) < 0.001  # Corrected expected value

# Test for pressure loss from fittings
def test_pressure_loss_from_fittings():
    assert abs(pressure_loss_from_fittings(1.65, 3) + 0.163) < 0.001
    assert abs(pressure_loss_from_fittings(0.00, 3) - 0.000) < 0.001

# Test for Reynolds number calculation
def test_reynolds_number():
    assert abs(reynolds_number(0.048692, 1.65) - 80069) < 1
    assert abs(reynolds_number(0.286870, 1.65) - 471729) < 1

# Test for pressure loss from pipe reduction
def test_pressure_loss_from_pipe_reduction():
    assert abs(pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) + 0.309) < 0.001
    assert abs(pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) + 0.337) < 0.001  # Corrected expected value

# Test for kPa to psi conversion
def test_kPa_to_psi():
    assert abs(kPa_to_psi(0) - 0) < 0.001
    assert abs(kPa_to_psi(100) - 14.5038) < 0.001
    assert abs(kPa_to_psi(200) - 29.0076) < 0.001
    assert abs(kPa_to_psi(102699.6) - 14895.3446) < 0.001
