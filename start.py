# print('hello')

import simple_draw as sd

sd.set_screen_size(1200, 800)

# point = sd.get_point(300, 300)

#vector = sd.get_vector(point, angle=60, length=100)
#vector.draw()

def draw_flake(point, arm_len=50):
    delta_angle = sd.random_number(30, 90)
    factor_a = sd.random_number(30, 90) / 100
    for angle in range(0, 360, 60):
        arm = sd.get_vector(point, angle=angle, length=arm_len)
        arm.draw(color=sd.COLOR_WHITE)
        arm_2 = sd.get_vector(point, angle=angle, length=arm_len * .6)

        sub_arm_1 = sd.get_vector(
            start_point=arm_2.end_point,
            angle=angle + delta_angle, 
            length=arm_len * factor_a,
            )
        sub_arm_1.draw(color=sd.COLOR_WHITE)
        sub_arm_2 = sd.get_vector(
            arm_2.end_point, 
            angle=angle - delta_angle,
            length=arm_len * factor_a,
            )
        sub_arm_2.draw(color=sd.COLOR_WHITE)

for _ in range(150):
    point = sd.random_point()
    draw_flake(point=point)

sd.pause()