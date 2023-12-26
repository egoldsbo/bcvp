import subprocess

def open_terminal_and_run_commands():
    # Directory and script you want to run
    directory = "bcvp"
    script = "script.py"

    # Command to open a new terminal window and run the commands
    # Using bash -c allows for running multiple commands in sequence
    terminal_command = ["lxterminal", "-e", f"bash -c 'cd {directory}; python3 {script}; exec bash'"]

    # Open a new terminal window and run the commands
    try:
        subprocess.Popen(terminal_command)
        print("Terminal opened and commands executed successfully.")
    except Exception as e:
        print(f"Error opening terminal or executing commands: {e}")

if __name__ == "__main__":
    open_terminal_and_run_commands()
