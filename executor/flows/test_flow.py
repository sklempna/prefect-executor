from prefect import flow


@flow(log_prints=True)
def test_function():
    print("test")


if __name__ == "__main__":
    test_function.serve(name="test-function")
