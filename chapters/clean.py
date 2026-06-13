import sys
sys.path.append("../../../proj/lib")
sys.path.append("C:/Python/xlib")
from util.md import CleanMarkdownFiles
import fs

book = fs.join(fs.dirname(__file__), "..", "book.yml")
CleanMarkdownFiles(book)