import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# define your draw functions

def draw_cloud(x, y, size):
    arcade.draw_circle_filled(x, y, size, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 50, y + 50, size, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 75, y, size, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 100, y + 50, size, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 150, y, size, arcade.color.WHITE)

def draw_rollinghills(w, z, sizes):
    arcade.draw_circle_filled(w, z, sizes, arcade.color.GREEN)
    arcade.draw_circle_filled(w + 400, z, sizes, arcade.color.GREEN)

def draw_tree(trunkx, trunky, width, height, circlex, circley, circlesize):
    arcade.draw_rectangle_filled(trunkx, trunky, width, height, arcade.color.BROWN)
    arcade.draw_circle_filled(circlex, circley, circlesize, arcade.color.DARK_PASTEL_GREEN)
    arcade.draw_circle_filled(circlex + 25, circley + 25, circlesize, arcade.color.DARK_PASTEL_GREEN)
    arcade.draw_circle_filled(circlex + 25, circley + 50, circlesize, arcade.color.DARK_PASTEL_GREEN)
    arcade.draw_circle_filled(circlex + 75, circley + 100, circlesize, arcade.color.DARK_PASTEL_GREEN)
    arcade.draw_circle_filled(circlex + 125, circley + 50, circlesize, arcade.color.DARK_PASTEL_GREEN)
    arcade.draw_circle_filled(circlex + 125, circley + 25, circlesize, arcade.color.DARK_PASTEL_GREEN)
    arcade.draw_circle_filled(circlex + 150, circley, circlesize, arcade.color.DARK_PASTEL_GREEN)
    arcade.draw_circle_filled(circlex + 75, circley - 25, circlesize, arcade.color.DARK_PASTEL_GREEN)




def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.LIGHT_BLUE)
    arcade.start_render()

   # call your draw functions
    draw_cloud(100, 450, 50)
    draw_rollinghills(200, 0, 300)
    draw_tree(600, 200, 100, 300, 525, 400, 75)
    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()