import subprocess
import sys

if __name__ == "__main__":

    subprocess.run([sys.executable,"nauqanscraper.py"])
    subprocess.run([sys.executable,"post.py"])