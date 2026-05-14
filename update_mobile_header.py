from pathlib import Path
path = Path("src/components/Navbar.tsx")
text = path.read_text()

text = text.replace(
    '                    <div className="flex items-center justify-between px-6 py-4 border-b border-gray-200">',
    '                    <div className="flex items-center justify-between px-6 py-4 border-b border-transparent">'
)

text = text.replace(
    '<button\n                                type="button"\n                                onClick={() => setMobileOpen(true)}\n                                className="inline-flex h-10 w-10 items-center justify-center rounded-full border border-transparent bg-white/80 text-report-right-green shadow-sm backdrop-blur transition hover:bg-white"\n                                aria-label="Open navigation menu"\n                            >\n                                <FaBars className="h-5 w-5" />\n                            </button>',
    '<button\n                                type="button"\n                                onClick={() => setMobileOpen((prev) => !prev)}\n                                className={`inline-flex h-10 w-10 items-center justify-center rounded-full border border-transparent bg-white/80 text-report-right-green shadow-sm backdrop-blur transition hover:bg-white ${mobileOpen ? "rotate-45" : ""}`}\n                                aria-label={mobileOpen ? "Close navigation menu" : "Open navigation menu"}\n                            >\n                                <FaBars className="h-5 w-5 transition-transform duration-200" />\n                            </button>'
)

text = text.replace(
    '<div className="flex items-center justify-between px-6 py-4 border-b border-transparent">\n                        <Link href="/home" className="flex items-center space-x-2" onClick={() => setMobileOpen(false)}>',
    '<div className="flex items-center gap-3">\n                        <button\n                            type="button"\n                            onClick={() => setMobileOpen(false)}\n                            className="inline-flex h-10 w-10 items-center justify-center rounded-full border border-transparent bg-white text-report-right-green shadow-sm transition"\n                            aria-label="Close navigation menu"\n                        >\n                            <FaXmark className="h-5 w-5" />\n                        </button>\n                        <Link href="/home" className="flex items-center space-x-2" onClick={() => setMobileOpen(false)}>'
)

text = text.replace(
    '<button\n                            type="button"\n                            onClick={() => setMobileOpen(false)}\n                            className="rounded-full border border-transparent bg-white/80 p-2 text-report-right-green shadow-sm backdrop-blur transition hover:bg-white"\n                            aria-label="Close navigation menu"\n                        >\n                            <FaTimes className="h-5 w-5" />\n                        </button>',
    ''
)

path.write_text(text)
