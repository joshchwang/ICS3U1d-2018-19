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
    
def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.LIGHT_BLUE)
    arcade.start_render()

   # call your draw functions
    draw_cloud()
    draw_rollinghills()
    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()