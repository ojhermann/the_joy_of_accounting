import pytest

from tool.wrap_quotes import wrap_quotes

CITATION_21: str = (
    "Frampton, Peter; Robilliard, Mark. The Joy of Accounting: A Game-Changing\n"
    "Approach That Makes Accounting Easy (p. 21). (Function). Kindle Edition."
)
CITATION_42: str = (
    "Frampton, Peter; Robilliard, Mark. The Joy of Accounting: A Game-Changing\n"
    "Approach That Makes Accounting Easy (p. 42). (Function). Kindle Edition."
)


@pytest.mark.unit_test
def test_empty_file() -> None:
    assert wrap_quotes("") == ""


@pytest.mark.unit_test
def test_only_non_citation() -> None:
    text: str = "Some quote from the book."
    assert wrap_quotes(text) == "`Some quote from the book.`"


@pytest.mark.unit_test
def test_only_citation() -> None:
    content: str = CITATION_21 + "\n"
    assert wrap_quotes(content) == content


@pytest.mark.unit_test
def test_mixed() -> None:
    content: str = f"First quote.\n\n{CITATION_21}\n\nSecond quote.\n\n{CITATION_42}\n"
    expected: str = (
        f"`First quote.`\n\n{CITATION_21}\n\n`Second quote.`\n\n{CITATION_42}\n"
    )
    assert wrap_quotes(content) == expected
