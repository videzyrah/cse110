# Write a program to calculate the resources needed 
# to remodel a golf course hole.  
#     See assignment description for details.
# 
# The inputs should be:
#     Enter Course Length: 
#     Enter Course Width: 
# 
# The outputs should be:
#     Total square yards of rough sod:
#     Total square yards of smooth sod:
#     Tons of sand:
#     Number of retaining wall bricks:
#     Number of bushes:
#     Total Mowing Time (mins):


from math import ceil, floor

#low-level calculation functions
def compute_area_of_rectangle(length, width):
    area = length * width
    return (area)

def compute_area_of_circle(radius):
    area = 3.1415*radius**2
    return (area)

def compute_sand_trap_cubic_feet(radius_in_yards, depth_in_feet):
    area_in_yards = 3.1415 * radius_in_yards ** 2
    sand_trap_cubic_feet = area_in_yards*square_ft_per_square_yd*sand_trap_depth_feet
    return sand_trap_cubic_feet

def compute_half_circumference(radius):
    half_circumference = 3.1415 * radius
    return half_circumference

def compute_perimeter(length, width):
    perimeter = 2 * length + 2 * width
    return perimeter

#output functions
def compute_rough_sod_sq_yards(total_course_area_yards, tee_area_yards, hole_area_yards, sand_trap_area_yards):
    rough_sod_sq_yards = ceil(total_course_area_yards - tee_area_yards - hole_area_yards - sand_trap_area_yards)
    return (rough_sod_sq_yards)

def compute_smooth_sod_sq_yards(tee_area_yards, hole_area_yards):
    smooth_sod_sq_yards = ceil(tee_area_yards + hole_area_yards)
    return (smooth_sod_sq_yards)

def compute_sand_needed_US_tons(sand_pounds_per_cubic_foot, sand_trap_radius_yards, sand_trap_depth_feet):
    sand_needed = ceil(sand_pounds_per_cubic_foot * compute_sand_trap_cubic_feet(sand_trap_radius_yards, sand_trap_depth_feet )/2000)
    return sand_needed

def compute_bricks_needed(sand_trap_radius_yards, bricks_per_linear_yard):
    bricks_needed = ceil(compute_half_circumference(sand_trap_radius_yards) * bricks_per_linear_yard)
    return bricks_needed

def compute_bushes_needed(instance_course_length_yards, instance_course_width_yards, bushes_per_yard):
    bushes_needed = floor(compute_perimeter(instance_course_length_yards, instance_course_width_yards) - 2 * bushes_per_yard)
    return bushes_needed

def compute_mow_time(mow_time_seconds_per_square_yard_rough_sod, mow_time_seconds_per_square_yard_smooth_sod, rough_sod_sq_yards_total, smooth_sod_sq_yards_total):
    mow_time_seconds = (mow_time_seconds_per_square_yard_rough_sod  * rough_sod_sq_yards_total +
                        mow_time_seconds_per_square_yard_smooth_sod * smooth_sod_sq_yards_total)
    mow_time_minutes = ceil(mow_time_seconds/60)
    return mow_time_minutes
    
#constants
sand_trap_depth_feet = 1
sand_pounds_per_cubic_foot = 100
pounds_per_US_ton = 2000
square_ft_per_square_yd = 9
bricks_per_linear_yard = 9
bushes_per_yard = 1
mow_time_seconds_per_square_yard_rough_sod = 0.5
mow_time_seconds_per_square_yard_smooth_sod = 1

#inputs
instance_course_length_yards = float(input("Enter Course Length:"))
instance_course_width_yards = float(input("Enter Course width:"))


#intermediate variables/calculations
green_radius_yards = instance_course_width_yards/4
sand_trap_radius_yards = instance_course_width_yards/6

total_course_area_yards = compute_area_of_rectangle(instance_course_length_yards, instance_course_width_yards)
tee_area_yards = compute_area_of_circle(green_radius_yards)
hole_area_yards = tee_area_yards
sand_trap_area_yards = compute_area_of_circle(sand_trap_radius_yards)

#output calculation calls
rough_sod_sq_yards_total= compute_rough_sod_sq_yards(total_course_area_yards, tee_area_yards, hole_area_yards, sand_trap_area_yards)
smooth_sod_sq_yards_total = compute_smooth_sod_sq_yards(tee_area_yards, hole_area_yards)
tons_of_sand = compute_sand_needed_US_tons(sand_pounds_per_cubic_foot, sand_trap_radius_yards, sand_trap_depth_feet )
bricks_needed = compute_bricks_needed(sand_trap_radius_yards, bricks_per_linear_yard)
bushes_needed = compute_bushes_needed(instance_course_length_yards, instance_course_width_yards, bushes_per_yard)
mow_time_minutes = compute_mow_time(mow_time_seconds_per_square_yard_rough_sod, mow_time_seconds_per_square_yard_smooth_sod, rough_sod_sq_yards_total, smooth_sod_sq_yards_total)

#outputs
def report():
    print("Total square yards of rough sod:", rough_sod_sq_yards_total)
    print("Total square yards of smooth sod:", smooth_sod_sq_yards_total )
    print("Tons of sand:", tons_of_sand)
    print("Number of retaining wall bricks:", bricks_needed)
    print("Number of bushes:", bushes_needed)
    print("Total Mowing Time (mins):", mow_time_minutes)
report()