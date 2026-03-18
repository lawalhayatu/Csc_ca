from collections import deque

def application_pipeline():
    # 1. Initialize
    application_inbox = deque()   # Queue (FIFO)
    processed_history = []        # Stack (LIFO)

    # 2. Ingest Data (messy startup names)
    messy_names = [" TechCorp ", "bio-gen", "  AlphaWorks", "FinSolve  "]

    # Clean and add to queue
    for name in messy_names:
        clean_name = name.strip().lower()
        application_inbox.append(clean_name)

    print("Cleaned Applications in Queue:")
    print(application_inbox)
    print()

    # 3. Process (FIFO)
    while application_inbox:
        current = application_inbox.popleft()
        print(f"Approving: {current}")

        # Push to stack
        processed_history.append(current)

    print("\nAll applications processed!")
    print("Processed History (Stack):")
    print(processed_history)

    # 4. Undo (LIFO)
    if processed_history:
        last = processed_history.pop()
        print(f"\nReverting approval for: {last}")


# Run program
if __name__ == "__main__":
    application_pipeline()