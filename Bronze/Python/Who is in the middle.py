import sys

soup = [int(sys.stdin.readline()) for _ in range(3)]

soup.remove(max(soup))
soup.remove(min(soup))

print(*soup)
