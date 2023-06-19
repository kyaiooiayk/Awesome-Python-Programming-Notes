# Step 01
***

- Add two simple tests:
    - One on the data source: this is done to flag is the result has not changed.
    - One the data sink (the results): this is done to make sure the source of the data has not changed.

- This will implement very simple end-to-end testing which is less effort than unit testing given that the code is not really in a testable state. It caches the value of some variables and the next time you run the code it will compare it to this cache. If they match you didn't change the behaviour of the code with the last change. If your intentions was indeed to change the behaviour, verify from the output of the AssertionError that the changes are working as intended. If they are, delete the chaches and rerun the code to generate new reference values. The tests should be such that if they fail they produce meaningful differences. So instead of aggregate statistics (like an F1 score) test the datasets itself. That way even small changes won't go undetected. Once the code is refactored you can write different type of tests
***

## References
- [Original project](https://github.com/xLaszlo/CQ4DS-notebook-sklearn-refactoring-exercise/tree/master)
***