# Call Sequencer

Call Sequencer is a Python package for sequencing function calls as blocks.

## Installation

You can install the package via pip:

```
pip install call-sequencer
```

## Usage

```python
from call_sequencer.block import CallSequencer

# Example usage
text_processor = (
    CallSequencer.start("Great!") >> CallSequencer.with_args(tokenize_text)(delimiter=" ") >> CallSequencer.simple(embed_tokens) >> CallSequencer.simple(classify_embeddings)
)

result = text_processor()
print("Classification Result:", result)
```
Another useage as decorators
```python
# Example Usage
    @CallSequencer.simple
    def sanitize(param) -> str:...

    @CallSequencer.simple
    def retrive_data(param)-> str:...

    @CallSequencer.with_args
    def query_llm(param, *args, **kwargs)-> str:...

    @CallSequencer.simple
    def extract_code(param)-> str:...

    @CallSequencer.simple
    def execute_code(param)-> str:...


    code_evaluator = (
        CallSequencer.start("Hello")  # Initial input block
        >> sanitize
        >> retrive_data
        >> query_llm("extra_param")
        >> extract_code
        >> execute_code
        >> query_llm("another_param")
    )

    # Run the chain
    result = code_evaluator()
    print("Final Result:", result)

```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
