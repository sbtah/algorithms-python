def hanoi(disk, source, middle, destination):

    # Base case
    # 0 is always a smallest plate.
    # We manipulate the smallets plate in the base case.
    if disk == 0:
        print(f"Disk {disk} from {source} to {destination}")
