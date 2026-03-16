import argparse
import re
import sys
from pathlib import Path

CITATION_PATTERN = re.compile(
    r"^Frampton, Peter; Robilliard, Mark\. The Joy of Accounting: A Game-Changing\n"
    r"Approach That Makes Accounting Easy \(p\. \d+\)\. \(Function\)\. Kindle Edition\.$"
)


def wrap_quotes(content: str) -> str:
    parts = content.split("\n\n")
    result = []
    for part in parts:
        stripped = part.strip()
        if not stripped or CITATION_PATTERN.match(stripped):
            result.append(part)
        else:
            result.append("`" + stripped + "`")
    output = "\n\n".join(result)
    if content.endswith("\n") and not output.endswith("\n"):
        output += "\n"
    return output


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Wrap non-citation paragraphs in backticks."
    )
    parser.add_argument("file", type=Path, help="Markdown file to process")
    parser.add_argument(
        "--in-place", "-i", action="store_true", help="Edit the file in place"
    )
    args = parser.parse_args()

    content = args.file.read_text()
    output = wrap_quotes(content)

    if args.in_place:
        args.file.write_text(output)
    else:
        sys.stdout.write(output)


if __name__ == "__main__":
    main()
