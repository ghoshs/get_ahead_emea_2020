def evaluate(testcases):
    for testcase in testcases:
        try: 
            testcase()
        except AssertionError:
            print("Failed")
        except Exception as e:
            print(e)
        else:
            print('Passed')
        finally:
            pass