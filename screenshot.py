import os

def capture_cli_screenshot(output_filename):
    # Run a command and capture its output to a file
    command = "ifconfig,whoami,ip a"  # Replace with the CLI command you want to run
    os.system(f"{command} > {output_filename}")

if __name__ == "__main__":
    output_filename = "screenshot.txt"  # Use double quotes around the filename
    capture_cli_screenshot(output_filename)
    print(f"CLI screenshot saved as {output_filename}")

