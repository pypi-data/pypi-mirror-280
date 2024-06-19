# code2claude: Code Consolidator

A Python tool that consolidates code from a repository into a unified format for AI-assisted analysis and manipulation.

Code Consolidator is a Python tool that traverses a code repository, extracts code from various files, and consolidates it into a unified format. The consolidated code is optimized for AI-assisted analysis and manipulation, enabling seamless collaboration between humans and AI in understanding and working with the codebase.

## Features

- Traverses a code repository and identifies relevant code files based on specified file extensions.
- Extracts code from each file and applies necessary preprocessing steps.
- Consolidates the extracted code into a single, unified format.
- Includes metadata such as file paths and module names for context.
- Provides options for code organization, dependency management, and documentation.
- Facilitates AI-assisted code analysis, manipulation, and collaboration.

## Installation

From PyPI:

```bash
pip install code2claude
```

From source:

1. Clone the repository:

   ```
   git clone https://github.com/ad3002/code2claude
   ```

2. Navigate to the project directory:
   ```bash
   cd code2claude
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Update the `config.py` file with the necessary configurations, such as the repository path and file extensions to consider.

2. Run the code consolidator:
   
   ```bash
   python code2claude.py /path/to/repo --extensions .py .js .java
   ```

3. The consolidated code will be generated and saved in the specified output format.

4. Provide the consolidated code to an AI system for analysis and manipulation.

## Current format of the consolidated code

The current format of the consolidated code is as follows:

```xml
<file>
   <path>/path/to/file1.py</path>
   <content>
      # Code content of file1.py
      def function1():
         # ...
   </content>
</file>

<file>
   <path>/path/to/file2.py</path>
   <content>
      # Code content of file2.py
      class Class2:
         # ...
   </content>
</file>

...
```

## Possbile prompt for the AI system

```xml
<prompt>
   <consolidated_code>
      <instruction>Claude, please, see the attached file</instruction>
   </consolidated_code>

   <question>
   Your question or request goes here. For example:
   - Can you identify any potential performance issues in the code?
   - How can I refactor the code to improve readability and maintainability?
   - Are there any security vulnerabilities or best practices violations in the code?
   </question>
</prompt>
```

## How to improve the code before running the consolidator

Remember, the specific details and format of the consolidated code may vary based on your project's needs and the programming language being used. The key is to provide a clear, organized, and well-documented representation of your codebase that facilitates effective analysis and collaboration between humans and AI.

To process the consolidated code as a whole and provide effective analysis and manipulation, there are a few additional things that would be helpful:

1. Code Structure and Organization:
   - Clearly indicate the boundaries between different code files or modules within the consolidated code. This can be done using comments, delimiters, or specific markers.
   - Include information about the file paths or module names to provide context about the code's organization.
   - Maintain a consistent indentation level throughout the consolidated code to ensure readability.

2. Dependency and Import Statements:
   - If the code relies on external libraries or modules, include the necessary import statements at the beginning of the consolidated code.
   - If there are inter-dependencies between the code files, ensure that the order of the consolidated code reflects the proper dependency hierarchy.

3. Documentation and Comments:
   - Include relevant comments and documentation within the code to provide explanations and context.
   - Use docstrings to describe the purpose, parameters, and return values of functions and classes.
   - Provide high-level comments to explain the overall structure and flow of the code.

4. Test Cases and Examples:
   - If available, include test cases or example usage of the code within the consolidated format.
   - This helps in understanding how the code is intended to be used and what expected outcomes should be.

5. Configuration and Environment:
   - If the code relies on specific configuration files or environment variables, include them or provide instructions on how to set them up.
   - Specify any required dependencies or libraries that need to be installed for the code to run successfully.

6. Error Handling and Logging:
   - Include error handling and logging statements within the code to aid in debugging and understanding potential issues.
   - Provide information on how to interpret and resolve common errors or exceptions that may occur.

7. Code Analysis Preferences:
   - If you have specific preferences or requirements for code analysis, such as focusing on certain aspects like performance, security, or style, mention them along with the consolidated code.
   - This helps me tailor the analysis and provide targeted insights based on your priorities.

By incorporating these additional elements, you can provide a more comprehensive and context-rich representation of your codebase. It enables me to understand the code's structure, dependencies, and intended usage more effectively, leading to more accurate and valuable analysis and manipulation.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
