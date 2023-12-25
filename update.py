import subprocess

def git_pull(repo_path):
    try:
        # Changing the current working directory to the repository's directory
        subprocess.check_call(['cd', repo_path], shell=True)
        
        # Running 'git pull' command
        subprocess.check_call(['git', 'pull'], shell=True)
        print("Successfully pulled the repository.")
    except subprocess.CalledProcessError as e:
        print("Failed to pull the repository. Error:", e)

if __name__ == "__main__":
    repo_path = "/bcvp"  # Replace with the path to your repository
    git_pull(repo_path)
