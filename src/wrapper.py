import sys

def wrapper(mainFunction, *testsFunction):
    if len(sys.argv) == 2 and sys.argv[1] == "test":
        failed = 0
        passed = 0

        # Iterate through the test and run them
        print(f"Running {len(testsFunction)} tests...")

        for test in testsFunction:
            test()

    else:
        mainFunction()
