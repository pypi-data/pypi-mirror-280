from call_sequencer import CallSequencer
import re
from typing import Optional, List, Tuple

# Function decorators are used to manage function calls with CallSequencer
@CallSequencer.simple
def extract_title(md_string: str) -> Optional[str]:
    """
    Extracts the title from a Markdown string (denoted by single #).
    """
    lines = md_string.strip().splitlines()  # type: List[str]
    for line in lines:
        if line.startswith("#"):
            return line.lstrip("#").strip()
    return None  # Return None if no title found

@CallSequencer.simple
def extract_code_blocks(md_string: str) -> List[str]:
    """
    Extracts all code blocks from a Markdown string (denoted by ```).
    """
    code_blocks = re.findall(r"```(.+?)```", md_string, re.DOTALL)  # type: List[str]
    return code_blocks

@CallSequencer.simple
def extract_tables(md_string: str) -> List[str]:
    """
    Extracts tables from a Markdown string.
    """
    tables = re.findall(r'\|(.+)\|', md_string, re.DOTALL)  # type: List[str]
    return tables

@CallSequencer.simple
def extract_lists(md_string: str) -> List[str]:
    """
    Extracts lists (both ordered and unordered) from a Markdown string.
    """
    lists = re.findall(r'(?:(?:^\*|\d+\.) .+$\n?)+', md_string, re.MULTILINE)  # type: List[str]
    return lists

@CallSequencer.simple
def extract_first_code_block(md_string: str) -> Optional[str]:
    """
    Extracts the first code block from a Markdown string.
    """
    code_block = re.search(r'```(.+?)```', md_string, re.DOTALL)  # type: Optional[re.Match]
    return code_block.group(1) if code_block else None

@CallSequencer.simple
def extract_headings(md_string: str) -> List[str]:
    """
    Extracts all headings from a Markdown string.
    Headings are denoted by lines starting with multiple '#' characters.
    """
    headings = re.findall(r'^#+\s*(.+)$', md_string, re.MULTILINE)  # type: List[str]
    return headings

@CallSequencer.simple
def extract_bold_text(md_string: str) -> List[str]:
    """
    Extracts text enclosed in '**' (bold formatting) from a Markdown string.
    """
    bold_text = re.findall(r'\*\*(.*?)\*\*', md_string)  # type: List[str]
    return bold_text

@CallSequencer.simple
def extract_italic_text(md_string: str) -> List[str]:
    """
    Extracts text enclosed in '*' (italic formatting) from a Markdown string.
    """
    italic_text = re.findall(r'\*(.*?)\*', md_string)  # type: List[str]
    return italic_text

@CallSequencer.simple
def extract_links(md_string: str) -> List[Tuple[str, str]]:
    """
    Extracts links from a Markdown string in the format [text](url).
    """
    links = re.findall(r'\[(.*?)\]\((.*?)\)', md_string)  # type: List[Tuple[str, str]]
    return links

@CallSequencer.simple
def extract_all_text(md_string: str) -> str:
    """
    Extracts all plain text (non-markdown formatted) from a Markdown string.
    """
    # Remove all Markdown syntax and extract plain text
    plain_text = re.sub(r'(\*\*|__|\*|_|\[.*?\]\(.*?\))', '', md_string)  # type: str
    return plain_text.strip()
