from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "src" / "components"


def ensure_import(text: str, import_line: str) -> str:
    if import_line in text:
        return text
    parts = text.split("\r\n")
    import_indices = [i for i, line in enumerate(parts) if line.startswith("import ")]
    if import_indices:
        insert_at = import_indices[-1] + 1
    else:
        insert_at = 0
    parts.insert(insert_at, import_line)
    import_indices = [i for i, line in enumerate(parts) if line.startswith("import ")]
    last_import = import_indices[-1]
    if last_import + 1 < len(parts) and parts[last_import + 1] != "":
        parts.insert(last_import + 1, "")
    return "\r\n".join(parts)


def replace_block(text: str, old: str, new: str, path: Path) -> str:
    if old not in text:
        raise RuntimeError(f"Expected block not found in {path}")
    return text.replace(old, new, 1)


def to_crlf(block: str) -> str:
    return block.strip("\n").replace("\n", "\r\n")

updates = [
    {
        "path": BASE / "AboutHomeSection.tsx",
        "old": to_crlf(
            """
                    <div className=\"text-center\">
                        <button className=\"mt-6 inline-flex items-center px-6 py-2 border border-2 border-green-600 font-medium rounded-full hover:bg-green-50\">
                            About Us <ArrowRight className=\"ml-2 w-4 h-4\" />
                        </button>
                    </div>
            """
        ),
        "new": to_crlf(
            """
                    <div className=\"text-center\">
                        <Link
                            href=\"http://172.27.176.1:3000/who-we-are\"
                            className=\"mt-6 inline-flex items-center px-6 py-2 border border-2 border-green-600 font-medium rounded-full hover:bg-green-50\"
                        >
                            About Us <ArrowRight className=\"ml-2 w-4 h-4\" />
                        </Link>
                    </div>
            """
        ),
        "imports": ["import Link from \"next/link\""]
    },
    {
        "path": BASE / "EsgSection.tsx",
        "old": to_crlf(
            """
                    <div className=\"pl-4\">
                        <button className=\"mt-6 inline-flex items-center px-6 py-2 border border-green-600 font-medium rounded-full hover:bg-green-50\">
                            Why ESG Matters <ArrowRight className=\"ml-2 w-4 h-4\" />
                        </button>
                    </div>
            """
        ),
        "new": to_crlf(
            """
                    <div className=\"pl-4\">
                        <Link
                            href=\"http://172.27.176.1:3000/our-services\"
                            className=\"mt-6 inline-flex items-center px-6 py-2 border border-green-600 font-medium rounded-full hover:bg-green-50\"
                        >
                            Why ESG Matters <ArrowRight className=\"ml-2 w-4 h-4\" />
                        </Link>
                    </div>
            """
        ),
        "imports": ["import Link from \"next/link\""]
    },
    {
        "path": BASE / "AuditsSection.tsx",
        "old": to_crlf(
            """
                    <div className=\"pl-4\">
                        <button className=\"mt-6 inline-flex items-center px-6 py-2 border border-3 border-green-600 font-medium rounded-full hover:bg-green-50\">
                            Why Audits <ArrowRight className=\"ml-2 w-4 h-4\" />
                        </button>
                    </div>
            """
        ),
        "new": to_crlf(
            """
                    <div className=\"pl-4\">
                        <Link
                            href=\"http://172.27.176.1:3000/our-services\"
                            className=\"mt-6 inline-flex items-center px-6 py-2 border border-3 border-green-600 font-medium rounded-full hover:bg-green-50\"
                        >
                            Why Audits <ArrowRight className=\"ml-2 w-4 h-4\" />
                        </Link>
                    </div>
            """
        ),
        "imports": ["import Link from \"next/link\""]
    },
    {
        "path": BASE / "QualitySection.tsx",
        "old": to_crlf(
            """
                <div className=\"mt-10\">
                    <button className=\"inline-flex items-center px-6 py-2 border border-2 border-green-600 font-medium rounded-full hover:bg-green-50\">
                        Our Values <ArrowRight className=\"ml-2 w-4 h-4\" />
                    </button>
                </div>
            """
        ),
        "new": to_crlf(
            """
                <div className=\"mt-10\">
                    <Link
                        href=\"http://172.27.176.1:3000/our-values\"
                        className=\"inline-flex items-center px-6 py-2 border border-2 border-green-600 font-medium rounded-full hover:bg-green-50\"
                    >
                        Our Values <ArrowRight className=\"ml-2 w-4 h-4\" />
                    </Link>
                </div>
            """
        ),
        "imports": ["import Link from \"next/link\""]
    },
    {
        "path": BASE / "PragmaticSection.tsx",
        "old": to_crlf(
            """
                    <div className=\"pl-4\">
                        <button className=\"mt-6 inline-flex items-center px-6 py-2 border border-3 border-green-600 font-medium rounded-full hover:bg-green-50\">
                            Why Us <ArrowRight className=\"ml-2 w-4 h-4\" />
                        </button>
                    </div>
            """
        ),
        "new": to_crlf(
            """
                    <div className=\"pl-4\">
                        <Link
                            href=\"http://172.27.176.1:3000/who-we-are\"
                            className=\"mt-6 inline-flex items-center px-6 py-2 border border-3 border-green-600 font-medium rounded-full hover:bg-green-50\"
                        >
                            Why Us <ArrowRight className=\"ml-2 w-4 h-4\" />
                        </Link>
                    </div>
            """
        ),
        "imports": ["import Link from \"next/link\""]
    },
    {
        "path": BASE / "CsrdBook.tsx",
        "old": to_crlf(
            """
        <div>
          <button className=\"inline-flex items-center justify-center rounded-full bg-green-600 px-6 py-3 text-sm font-semibold uppercase tracking-wide text-white transition-colors duration-200 hover:bg-green-700 sm:px-7 sm:py-3.5 sm:text-base\">
            Book a call
          </button>
        </div>
            """
        ),
        "new": to_crlf(
            """
        <div>
          <Link
            href=\"http://172.27.176.1:3000/lets-connect\"
            className=\"inline-flex items-center justify-center rounded-full bg-green-600 px-6 py-3 text-sm font-semibold uppercase tracking-wide text-white transition-colors duration-200 hover:bg-green-700 sm:px-7 sm:py-3.5 sm:text-base\"
          >
            Book a call
          </Link>
        </div>
            """
        ),
        "imports": ["import Link from \"next/link\""]
    },
    {
        "path": BASE / "HeroCTA.tsx",
        "old": to_crlf(
            """
            <button className=\"px-6 py-3 bg-green-600 hover:bg-green-700 text-white font-medium rounded-full shadow-sm transition\">
                Book A Call
            </button>
            """
        ),
        "new": to_crlf(
            """
            <Link
                href=\"http://172.27.176.1:3000/lets-connect\"
                className=\"px-6 py-3 bg-green-600 hover:bg-green-700 text-white font-medium rounded-full shadow-sm transition\"
            >
                Book A Call
            </Link>
            """
        ),
        "imports": ["import Link from \"next/link\""]
    },
    {
        "path": BASE / "BlogSection.tsx",
        "old": to_crlf(
            """
                            <button className=\"mt-6 inline-flex items-center px-4 py-2 bg-white text-black font-medium rounded-full hover:bg-gray-100 transition w-fit\">
                                Read More <span className=\"ml-2\">?+'</span>
                            </button>
            """
        ),
        "new": to_crlf(
            """
                            <Link
                                href=\"http://172.27.176.1:3000/blog\"
                                className=\"mt-6 inline-flex items-center px-4 py-2 bg-white text-black font-medium rounded-full hover:bg-gray-100 transition w-fit\"
                            >
                                Read More <ArrowRight className=\"ml-2 w-4 h-4\" />
                            </Link>
            """
        ),
        "imports": [
            "import { ArrowRight } from \"lucide-react\"",
            "import Link from \"next/link\"",
        ]
    },
]

for entry in updates:
    path = entry["path"]
    text = path.read_text()
    for import_line in entry.get("imports", []):
        text = ensure_import(text, import_line)
    try:
        text = replace_block(text, entry["old"], entry["new"], path)
    except RuntimeError as exc:
        print(exc)
        continue
    if not text.endswith("\r\n"):
        text += "\r\n"
    path.write_text(text)

print("CTA links updated.")
