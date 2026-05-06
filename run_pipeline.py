import subprocess

def run():
    print("Running extract...")
    subprocess.run(["py", "extract.py"])

    print("Running load...")
    subprocess.run(["py", "load.py"])

    print("Running transform...")
    subprocess.run(["py", "transform.py"])

    print("Pipeline completed!")

if __name__ == "__main__":
    run()
