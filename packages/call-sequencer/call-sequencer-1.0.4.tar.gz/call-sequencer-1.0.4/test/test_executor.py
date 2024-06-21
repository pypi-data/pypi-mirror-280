from call_sequencer.call_sequencer import CallSequencer
from call_sequencer.code_runner import (
    run_python_code,
    run_shell_command,
    evaluate_expression,
    list_installed_packages,
    get_package_info,
    install_package,
    uninstall_package,
    write_file,
    read_file,
    append_to_file,
)
from call_sequencer.markdown_extractors import extract_code_blocks


def test_functions():
    # Test data
    markdown_input = """
# Title of the Markdown
Some introductory text.

```
# This is a code block
a = 5
b = 10
c = a + b
print(c)
```

Another text paragraph.

## Subheading
More text.

### Sub-subheading
- List item 1
- List item 2

```bash
# This is a shell command
echo "Hello, World!"
```
    """

    # Creating a CallSequencer instance
    # seq = CallSequencer.start(markdown_input)

    # # Test extract_code_blocks
    # seq_code_blocks = seq >> extract_code_blocks
    # print("extract_code_blocks:")
    # print(seq_code_blocks())

    # # Test run_python_code
    # python_code = seq_code_blocks()[0]
    # seq_run_python = CallSequencer.start(python_code) >> run_python_code()
    # print("\nrun_python_code:")
    # print(seq_run_python())

    # # Test run_shell_command
    # shell_command = "echo 'Hello, World!'"
    # seq_run_shell = CallSequencer.start(shell_command) >> run_shell_command
    # print("\nrun_shell_command:")
    # print(seq_run_shell())

    # # Test evaluate_expression
    # expression = "5 * 10"
    # seq_eval_expression = CallSequencer.start(expression) >> evaluate_expression
    # print("\nevaluate_expression:")
    # print(seq_eval_expression())

    # Test install_package (example with a harmless package)
    # seq_install_package = CallSequencer.start("requests") >> install_package
    # print("\ninstall_package:")
    # print(seq_install_package())

    # Test uninstall_package (example with a harmless package)
    # seq_uninstall_package = CallSequencer.start("requests") >> uninstall_package
    # print("\nuninstall_package:")
    # print(seq_uninstall_package())

    # # Test list_installed_packages
    # seq_list_packages = CallSequencer.start(None) >> list_installed_packages
    # print("\nlist_installed_packages:")
    # print(seq_list_packages())

    # # Test get_package_info
    # package_name_info = "pip"
    # seq_package_info = CallSequencer.start(package_name_info) >> get_package_info
    # print("\nget_package_info:")
    # print(seq_package_info())

    # Test read_file
    test_file_path = "test_read.txt"
    with open(test_file_path, "w") as file:
        file.write("This is a test file for reading.")
    seq_read_file = CallSequencer.start(test_file_path) >> read_file
    print("\nread_file:")
    print(seq_read_file())

    # # Test write_file
    write_file_path = "test_write.txt"
    # write_file_content = "This is a test file for writing."
    # seq_write_file = CallSequencer.start(write_file_content) >>  write_file(write_file_path)
    
    # print("\nwrite_file:")
    # print(seq_write_file())
    # print("Content written to file:")
    # print(read_file(write_file_path))

    # Test append_to_file
    append_file_content = " This is appended content."
    seq_append_file = CallSequencer.start(append_file_content) >> append_to_file(write_file_path)
    print("\nappend_to_file:")
    print(seq_append_file())


# Run the test function
test_functions()
