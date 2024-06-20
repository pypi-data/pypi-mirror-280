from call_sequencer import CallSequencer
import re
from typing import Optional, List, Tuple, Union, Iterable

# Function decorators are used to manage function calls with CallSequencer


def flatten_strings(strings: Union[str, Iterable[str]]) -> List[str]:
    """
    Helper function to flatten n-dimensional string arrays into a single list of strings.
    """
    if isinstance(strings, str):
        return [strings]
    else:
        result = []
        for string_or_list in strings:
            result.extend(flatten_strings(string_or_list))
        return result


@CallSequencer.simple
def extract_title(md_string: Union[str, Iterable[str]]) -> Optional[str]:
    """
    Extracts the title from a Markdown string (denoted by single #).
    """
    flattened_strings = flatten_strings(md_string)
    for text in flattened_strings:
        lines = text.strip().splitlines()  # type: List[str]
        for line in lines:
            if line.startswith("#"):
                return line.lstrip("#").strip()
    return None  # Return None if no title found


@CallSequencer.simple
def extract_code_blocks(md_string: Union[str, Iterable[str]]) -> List[str]:
    """
    Extracts all code blocks from a Markdown string (denoted by ```).
    """
    flattened_strings = flatten_strings(md_string)
    code_blocks = []  # type: List[str]
    for text in flattened_strings:
        code_blocks.extend(re.findall(r"```(.+?)```", text, re.DOTALL))
    return code_blocks


@CallSequencer.simple
def extract_tables(md_string: Union[str, Iterable[str]]) -> List[str]:
    """
    Extracts tables from a Markdown string.
    """
    flattened_strings = flatten_strings(md_string)
    tables = []  # type: List[str]
    for text in flattened_strings:
        tables.extend(re.findall(r"\|(.+)\|", text, re.DOTALL))
    return tables


@CallSequencer.simple
def extract_lists(md_string: Union[str, Iterable[str]]) -> List[str]:
    """
    Extracts lists (both ordered and unordered) from a Markdown string.
    """
    flattened_strings = flatten_strings(md_string)
    lists = []  # type: List[str]
    for text in flattened_strings:
        lists.extend(re.findall(r"(?:(?:^\*|\d+\.) .+$\n?)+", text, re.MULTILINE))
    return lists


@CallSequencer.simple
def extract_first_code_block(md_string: Union[str, Iterable[str]]) -> Optional[str]:
    """
    Extracts the first code block from a Markdown string.
    """
    flattened_strings = flatten_strings(md_string)
    for text in flattened_strings:
        code_block = re.search(r"```(.+?)```", text, re.DOTALL)  # type: Optional[re.Match]
        if code_block:
            return code_block.group(1)
    return None


@CallSequencer.simple
def extract_headings(md_string: Union[str, Iterable[str]]) -> List[str]:
    """
    Extracts all headings from a Markdown string.
    Headings are denoted by lines starting with multiple '#' characters.
    """
    flattened_strings = flatten_strings(md_string)
    headings = []  # type: List[str]
    for text in flattened_strings:
        headings.extend(re.findall(r"^#+\s*(.+)$", text, re.MULTILINE))
    return headings


@CallSequencer.simple
def extract_bold_text(md_string: Union[str, Iterable[str]]) -> List[str]:
    """
    Extracts text enclosed in '**' (bold formatting) from a Markdown string.
    """
    flattened_strings = flatten_strings(md_string)
    bold_text = []  # type: List[str]
    for text in flattened_strings:
        bold_text.extend(re.findall(r"\*\*(.*?)\*\*", text))
    return bold_text


@CallSequencer.simple
def extract_italic_text(md_string: Union[str, Iterable[str]]) -> List[str]:
    """
    Extracts text enclosed in '*' (italic formatting) from a Markdown string.
    """
    flattened_strings = flatten_strings(md_string)
    italic_text = []  # type: List[str]
    for text in flattened_strings:
        italic_text.extend(re.findall(r"\*(.*?)\*", text))
    return italic_text


@CallSequencer.simple
def extract_links(md_string: Union[str, Iterable[str]]) -> List[Tuple[str, str]]:
    """
    Extracts links from a Markdown string in the format [text](url).
    """
    flattened_strings = flatten_strings(md_string)
    links = []  # type: List[Tuple[str, str]]
    for text in flattened_strings:
        links.extend(re.findall(r"\[(.*?)\]\((.*?)\)", text))
    return links


@CallSequencer.simple
def extract_all_text(md_string: Union[str, Iterable[str]]) -> str:
    """
    Extracts all plain text (non-markdown formatted) from a Markdown string.
    """
    flattened_strings = flatten_strings(md_string)
    plain_text = ""  # type: str
    for text in flattened_strings:
        plain_text += re.sub(r"(\*\*|__|\*|_|\[.*?\]\(.*?\))", "", text)
    return plain_text.strip()
