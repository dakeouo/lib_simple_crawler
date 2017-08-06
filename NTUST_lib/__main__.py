from argparse import ArgumentParser
import find_book

parser = ArgumentParser(prog="funcpy")
parser.add_argument("type", type=str, choices=["search","help"])
parser.add_argument("-t", "--search_type", type=str, default="X")
parser.add_argument("-s", "--search_scope", type=int, default=1)
parser.add_argument("-c", "--search_content", type=str)

args = parser.parse_args()

if args.type == "search":
	print(find_book.Search_book(sArg=args.search_content, sType=args.search_type, sScope=args.search_scope))
elif args.type == "help":
	help_msg = """
Python NTUST_lib search [-t type] [-s scope] [-c content]

-t    Search Book Type                      -s    Search Book Scope
----------------------------------------    ------------------------------------
X Keyword           t Book Name             1 All Result    5 Degree Thesis
a author            d topic                 2 Books         6 E-Books
c USA Claim number  l-China Claim number    3 Journals      7 Electronic Journal
i-ISBN              v-Barcode               4 Audiovisual info.
	"""
	print(help_msg)