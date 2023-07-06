# 1. Review the code and document your initial findings.
- gets only the ".json" data file as test data in a file path which is written in the _init_.py file
- gets the name of the CSV report file to test with which is specified in the CSV_REPORTS_DICT dictionary
- gets report file name and creates a folder in the temp directory
- generates the desired CSV report using test data
- prints the path of the report 

#  2. Define a (whitebox) test plan for this project.
TC1- Test the compactness function

Input: A test polygon with known area and length.
Expected Output: The compactness value is within the range of 0-100%.
Test Steps:
    Create a test polygon.
    Call the compactness function with the test polygon.
    Verify that the returned compactness value is within the expected range.

TC2- Test the picks_failures function

Input: A list of the PickResult objects containing both valid and invalid picks.
Expected Output: A list of only the invalid picks.
Test Steps:
    Create a list of PickResult objects with a combination of valid and invalid picks.
    Call the picks_failures function with the list of PickResult objects.
    Verify that the returned list contains only the invalid picks.


TC3- Test the picks_primary_failure_reason function

Input: A list of PickResult objects with different failure reasons.
Expected Output: The most common failure reason among the invalid picks.
Test Steps:
    Create a list of PickResult objects with different failure reasons.
    Call the picks_primary_failure_reason function with the list of PickResult objects.
    Verify that the returned primary failure reason is the most common failure reason among the invalid picks.

TC4- Test picks_first_valid function

Input: A list of the PickResult objects with both valid and invalid picks.
Expected Output: The first valid pick in the list, or the last pick if no valid pick is found.
Test Steps:
    Create a list of PickResult objects with a combination of valid and invalid picks.
    Call the picks_first_valid function with the list of PickResult objects.
    Verify that the returned pick is the first valid pick in the list, or the last pick if no valid pick is found.

# 3. Implement the tests as previously defined.
Check test.py 

# 4. Document your final thoughts on the implementation and potential future improvements.
My thoughts on the implementation:
The code has good modularity and allows user interaction via command-line prompts.
It's also good practice to use the 'gettempdir()' to store the reports.
The code has a 'CSV_REPORTS_DICT' dictionary for adding new report formats easily by simply adding them to the dictionary

Potential future improvements:
The code should have a logging mechanism to record important actions during the execution.
It should also have some other export options like Excel(xlsx) or JSON
Test data should be also an xml file as an alternative to json




