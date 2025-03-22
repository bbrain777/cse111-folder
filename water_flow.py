# Constants
EARTH_ACCELERATION_OF_GRAVITY = 9.8066500  # m/s²
WATER_DENSITY = 998.2000000  # kg/m³
WATER_DYNAMIC_VISCOSITY = 0.0010016  # Pa·s
PVC_SCHED80_INNER_DIAMETER = 0.28687  # meters
PVC_SCHED80_FRICTION_FACTOR = 0.013  # unitless
SUPPLY_VELOCITY = 1.65  # m/s
HDPE_SDR11_INNER_DIAMETER = 0.048692  # meters
HDPE_SDR11_FRICTION_FACTOR = 0.018  # unitless
HOUSEHOLD_VELOCITY = 1.75  # m/s

# Function to calculate the height of the water column
def water_column_height(tower_height, tank_height):
    """Calculates the height of the water column."""
    return tower_height - tank_height

# Function to calculate the pressure gained from the water height
def pressure_gain_from_water_height(water_height):
    """Calculates the pressure gained from the height of the water column."""
    return (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * water_height) / 1000  # Pressure in kPa

# Function to calculate pressure loss from the pipe due to friction
def pressure_loss_from_pipe(diameter, length, friction_factor, velocity):
    """Calculates the pressure loss due to friction in the pipe."""
    k = friction_factor * (length / diameter)
    loss = -k * (WATER_DENSITY * velocity ** 2) / 2000
    return loss

# Function to calculate pressure loss from fittings
def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """Calculates the pressure loss due to fittings like 90-degree bends."""
    loss = (-0.04 * WATER_DENSITY * fluid_velocity ** 2 * quantity_fittings) / 2000
    return loss

# Function to calculate the Reynolds number
def reynolds_number(hydraulic_diameter, fluid_velocity):
    """Calculates the Reynolds number for the flow in the pipe."""
    return (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY

# Function to calculate pressure loss from pipe reduction
def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """Calculates pressure loss when water moves from a larger pipe to a smaller pipe."""
    k = 0.1 + (50 / reynolds_number) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    loss = -k * (WATER_DENSITY * fluid_velocity ** 2) / 2000
    return loss

# Function to convert kPa to psi
def kPa_to_psi(kPa):
    """Converts pressure from kilopascals to pounds per square inch."""
    return kPa * 0.145038

# Main function to calculate the pressure at the house
def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    
    # Water column height and pressure gain from water height
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    # Pressure loss calculations for the supply pipe
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    # Pressure loss due to fittings (90° angles)
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    # Pressure loss due to pipe reduction
    loss = pressure_loss_from_pipe_reduction(diameter, velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    # Pressure loss for the pipe from supply to house
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    # Convert pressure to psi and print both kPa and psi
    pressure_in_psi = kPa_to_psi(pressure)
    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print(f"Pressure at house: {pressure_in_psi:.1f} pounds per square inch")

if __name__ == "__main__":
    main()
