import subprocess

def test_main():
    result = subprocess.run(["python", "src/main.py", "--name", "Alice"], capture_output=True, text=True)
    assert "Hello, Alice!" in result.stdout
