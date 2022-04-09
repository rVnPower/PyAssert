import sys


from .colors import bcolors

def wrapper(mainFunction, *testsFunction):
    if len(sys.argv) == 2 and sys.argv[1] == "test":
        failed = 0
        passed = 0

        # Iterate through the test and run them
        print(f"Running {len(testsFunction)} tests...")

        for test in testsFunction:
            try:
                test()
            except KeyboardInterrupt:
                print(f"\n{bcolors.WARNING}[INTERRUPTED]{bcolors.ENDC} {test.__name__}")
                continue
            except Exception:
                failed += 1
                print(f"{bcolors.FAIL}[FAILED]{bcolors.ENDC} {test.__name__}")
                continue

            passed += 1
            print(f"{bcolors.OKGREEN}[PASSED]{bcolors.ENDC} {test.__name__}")

    else:
        mainFunction()
