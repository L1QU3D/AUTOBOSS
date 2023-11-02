import time


def animated_console_presentation():
    tool_name = "AutoBoss"
    description = "AUTOMATED WEBSITE LOGGER BY L1QU3D."
    colors = ["\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m",
              "\033[36m"]  # ANSI escape codes for different colors

    print("Loading", end="")
    for i in range(6):  # 6 dots for a complete cycle
        color = colors[i % len(colors)]  # Cycle through the list of colors
        print(f"{color}.", end="", flush=True)
        time.sleep(0.5)

    # Reset the text color to default
    print("\033[0m")

    print("\n")

    # Create a systematically changing color effect for the tool name
    tool_name_3d = """
   ______      ______  __        __        ________  ________  
  /  __  \\    /  __  \\/  |      /  |      /  __   /  /  __   /  
 /  /_/ / /  /  /_/  /  |      /  |     /  /_/  /  /  /_/  /  
/    ____/  /  ___   /   |    /   |    /  /__/  /  /  /__/  
/  /          /  /   /     |  /    |  /   __  /  /   __  /  
/  /          /  /   /      | /     | /  /_/  /  /  /_/  /  
/__/          /__/  /______/  /______/  /__/    /  /__/    
"""
    colored_tool_name_3d = ""
    for line in tool_name_3d.split('\n'):
        color = colors[len(colored_tool_name_3d) % len(colors)]
        colored_tool_name_3d += color + line + '\n'
    print(colored_tool_name_3d)

    print(description)


if __name__ == "__main__":
    animated_console_presentation()
