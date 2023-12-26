import subprocess

def open_terminal():
    # Command to open a new terminal window
    terminal_command = "lxterminal"

    # Open a new terminal window
    try:
        subprocess.Popen(terminal_command)
        print("Terminal opened successfully.")
    except Exception as e:
        print(f"Error opening terminal: {e}")

if __name__ == "__main__":
    open_terminal()
