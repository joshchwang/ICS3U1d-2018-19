import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# define your draw functions
def draw_cloud():
    arcade.draw_circle_filled(100, 450, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(150, 500, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(175, 450, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(200, 500, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(250, 450, 50, arcade.color.WHITE)

def draw_rollinghills():
    arcade.draw_circle_filled(200, 0, 300, arcade.color.GREEN)
    arcade.draw_circle_filled(600, 0, 300, arcade.color.GREEN)

def draw_tree():
    arcade.draw_rectangle_filled(600, 200, 100, 300, arcade.color.BROWN)
    arcade.draw_circle_filled(525, 400, 75, arcade.color.DARK_PASTEL_GREEN)
    arcade.draw_circle_filled(550, 425, 75, arcade.color.DARK_PASTEL_GREEN)
    arcade.draw_circle_filled(550, 450, 75, arcade.color.DARK_PASTEL_GREEN)
    arcade.draw_circle_filled(600, 500, 75, arcade.color.DARK_PASTEL_GREEN)
    arcade.draw_circle_filled(650, 450, 75, arcade.color.DARK_PASTEL_GREEN)
    arcade.draw_circle_filled(650, 425, 75, arcade.color.DARK_PASTEL_GREEN)
    arcade.draw_circle_filled(675, 400, 75, arcade.color.DARK_PASTEL_GREEN)
    arcade.draw_circle_filled(600, 375, 75, arcade.color.DARK_PASTEL_GREEN)



def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.LIGHT_BLUE)
    arcade.start_render()

   # call your draw functions
    draw_cloud()
    draw_rollinghills()
    draw_tree()
    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()