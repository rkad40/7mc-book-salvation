import sys
sys.path.append("../../../proj/lib")
sys.path.append("C:/Python/xlib")
from util.md import BookUtils
import fs

book = BookUtils()
book.rename('c006-covenant-context-argument.md', 'c007-covenant-context-argument.md')
book.rename('c007-the-two-witness-argument.md', 'c008-the-two-witness-argument.md')
book.rename('c008-god-of-the-jews-only-argument.md', 'c009-god-of-the-jews-only-argument.md')
book.rename('c009-the-abraham-timeline-argument.md', 'c010-the-abraham-timeline-argument.md')
book.apply('c*.md')

