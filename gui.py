import dearpygui.dearpygui as dpg

width = 800
height = 600

# Create DearPyGui context and viewport
dpg.create_context()
dpg.create_viewport(title="Main", width=width, height=height)

# Load fonts
with dpg.font_registry():
    default_font = dpg.add_font("fonts/Rubik-Regular.ttf", 32)
    custom_font = dpg.add_font("fonts/Rubik-Bold.ttf", 84)


# Callbacks
def show_registry_viewer():
    dpg.configure_item(registry_viewer_window, show=True)
    dpg.configure_item(options_window, show=False)
    dpg.configure_item(main_menu_window, show=False)
    dpg.set_primary_window(registry_viewer_window, True)


def return_to_main_menu():
    dpg.configure_item(registry_viewer_window, show=False)
    dpg.configure_item(options_window, show=False)
    dpg.configure_item(main_menu_window, show=True)
    dpg.set_primary_window(main_menu_window, True)


def show_options():
    dpg.configure_item(options_window, show=True)
    dpg.configure_item(registry_viewer_window, show=False)
    dpg.configure_item(main_menu_window, show=False)
    dpg.set_primary_window(options_window, True)


# Main menu window
with dpg.window(no_collapse=True, no_resize=True, no_title_bar=True) as main_menu_window:
    with dpg.group(horizontal=True):
        title = dpg.add_text("Main Menu", pos=(width // 2 - 200, height // 2 - 200))
        dpg.bind_item_font(title, custom_font)
    with dpg.group(pos=(width // 2 - 100, height // 2 - 60), width=200):
        dpg.add_button(label="Start", callback=show_registry_viewer)
        dpg.add_button(label="Options", callback=show_options)
        dpg.add_button(label="Quit", callback=lambda: dpg.stop_dearpygui())

# Registry Viewer window
with dpg.window(label="Registry Viewer", pos=(width // 2 - 200, height // 2 - 200), width=400, height=400,
                show=False) as registry_viewer_window:
    dpg.add_text("Registry Viewer")
    dpg.add_button(label="Back", callback=return_to_main_menu)

# Options window
with dpg.window(label="Options", pos=(width // 2 - 200, height // 2 - 200), width=400, height=400,
                show=False) as options_window:
    dpg.add_text("Options")
    dpg.add_button(label="Back", callback=return_to_main_menu)

# Set up DearPyGui
dpg.bind_font(default_font)
dpg.set_primary_window(main_menu_window, True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
