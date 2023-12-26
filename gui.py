import dearpygui.dearpygui as dpg

width = 800
height = 600

# Create DearPyGui context and viewport
dpg.create_context()
dpg.create_viewport(title="Main Menu", width=width, height=height)

# Load fonts
with dpg.font_registry():
    default_font = dpg.add_font("fonts/Rubik-Regular.ttf", 32)
    custom_font = dpg.add_font("fonts/Rubik-Bold.ttf", 84)

# Main menu window
with dpg.window(no_collapse=True, no_resize=True, no_title_bar=True) as main_menu_window:
    with dpg.group(horizontal=True):
        title = dpg.add_text("Main Menu", pos=(width // 2 - 200, height // 2 - 100))
        dpg.bind_item_font(title, custom_font)

# Set up DearPyGui
dpg.bind_font(default_font)
dpg.set_primary_window(main_menu_window, True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
