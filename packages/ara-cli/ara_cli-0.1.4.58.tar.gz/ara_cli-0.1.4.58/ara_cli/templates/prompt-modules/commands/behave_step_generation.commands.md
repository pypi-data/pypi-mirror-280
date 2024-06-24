### COMMANDS FOR IMPLEMENTING A STEP IMPLEMENTATION FROM A GIVEN FEATURE FILE
Your job is now:
* Silently analyze the given feature file to understand the required step implementations.
* Silently review the provided source files to check if any step implementations already exist or if the necessary support methods are available.
* Develop implementation strategies that minimize code changes, prefer reusing existing methods over new implementations.
* Output a "change table" listing all necessary changes. Include an example line for reference:
  | filename                 | method                                   | short description of intended changes      |
  | {filename}.py            | {method name of existing or new method}  | {detailed explanation of the changes serving as code generation prompt}      |

* Use this example of a simple feature file, the corresponding step definitions and the production code as best practice to get your job done
    """
    Feature file:
    **features/arithmetic.feature**
    ```gherkin
    Feature: Arithmetic Operations

    Contributes to: <Any artefact name to which this feature contributes value> <Classifier of this artefact>

      Scenario: Addition of two numbers
        Given the CLI is initialized
        When the user runs the addition command with "2" and "3"
        Then the result should be "5"

      Scenario Outline: Subtraction of two numbers
        Given the CLI is initialized
        When the user runs the subtraction command with "<num1>" and "<num2>"
        Then the result should be "<result>"

        Examples:
          | num1 | num2 | result |
          | 5    | 3    | 2      |
          | 10   | 4    | 6      |
          | 0    | 0    | 0      |
    ```

    Step Definitions in Python with behave as BDD test framework:
    **features/steps/arithmetic_steps.py**
    ```python
    import subprocess
    from behave import given, when, then

    @given('the CLI is initialized')
    def step_given_cli_initialized(context):
        context.cli_command = 'python path/to/your_arithmetic_script.py'

    @when('the user runs the addition command with "{num1}" and "{num2}"')
    def step_when_user_runs_addition_command(context, num1, num2):
        context.result = subprocess.run(
            [context.cli_command, 'add', num1, num2],
            capture_output=True,
            text=True
        ).stdout.strip()

    @when('the user runs the subtraction command with "{num1}" and "{num2}"')
    def step_when_user_runs_subtraction_command(context, num1, num2):
        context.result = subprocess.run(
            [context.cli_command, 'subtract', num1, num2],
            capture_output=True,
            text=True
        ).stdout.strip()

    @then('the result should be "{expected_result}"')
    def step_then_result_should_be(context, expected_result):
        assert context.result == expected_result, f"Expected {expected_result} but got {context.result}"
    ```

    CLI Script as example production code to satisfiy the interfaces defined in the step definitions (DO NOT GENERATE ANY PRODUCTION CODE NOW):
    **your_arithmetic_script.py**
    ```python
    import sys

    def add(a, b):
        return int(a) + int(b)

    def subtract(a, b):
        return int(a) - int(b)

    if __name__ == "__main__":
        if len(sys.argv) != 4:
            print("Usage: python your_arithmetic_script.py <operation> <num1> <num2>")
            sys.exit(1)

        operation = sys.argv[1]
        num1 = sys.argv[2]
        num2 = sys.argv[3]

        if operation == 'add':
            print(add(num1, num2))
        elif operation == 'subtract':
            print(subtract(num1, num2))
        else:
            print(f"Unknown operation: {operation}")
            sys.exit(1)
    ```
    """ 
* Implement the changes as specified in the change table, ensuring your generated code blocks are not just code snippets but complete method levels. Use for every single generated code block this format:
```python
# [ ] extract
# filename: {path/filename}.py
{python code}
```

* The extract and filename statements are only allowed once per code block.
* Adhere strictly to established rules for high-quality Python code and architecture.
* If essential information is missing for code generation, issue a warning: "WARNING: Information is missing to do a correct implementation." Specify what information is lacking and suggest how it might be retrieved.