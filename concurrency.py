import threading as th
import time


def count(name: str, duration: int) -> None:
    """Function to be run in a thread."""
    print(f"Thread {name}: starting")
    time.sleep(duration)
    print(f"Thread {name}: finishing after {duration}s")


if __name__ == "__main__":
    # Create threads
    t1 = th.Thread(target=count, args=("A", 2))
    t2 = th.Thread(target=count, args=("B", 1))

    # Start threads
    t1.start()
    t2.start()

    # Wait for threads to complete (join)
    t1.join()
    t2.join()

    print("Both threads completed")

    # Demonstrate threading with return values using a shared list
    results = []

    def compute_square(name: str, number: int, results: list) -> None:
        result = number ** 2
        results.append((name, result))
        print(f"Thread {name}: {number}² = {result}")

    t3 = th.Thread(target=compute_square, args=("X", 7, results))
    t4 = th.Thread(target=compute_square, args=("Y", 9, results))

    t3.start()
    t4.start()
    t3.join()
    t4.join()

    print(f"\nResults: {results}")

    # Demonstrate daemon thread
    def background_task() -> None:
        print("Daemon thread: running in background")
        time.sleep(1)
        print("Daemon thread: done")

    d = th.Thread(target=background_task, daemon=True)
    d.start()
    print("Main thread continuing...")