from collections import deque

suggested_links = deque([int(x) for x in input().split()])
featured_articles = [int(x) for x in input().split()]
target = int(input())
final_feed = []

while len(suggested_links) > 0 and len(featured_articles) > 0:
    suggested_link = suggested_links.popleft()
    featured_article = featured_articles.pop()
    if suggested_link == featured_article:
        final_feed.append(0)
        continue
    elif suggested_link > featured_article:
        remainder = suggested_link % featured_article
        final_feed.append(-1 * remainder)
        if remainder != 0:
            suggested_links.append(remainder * 2)
    else:
        remainder = featured_article % suggested_link
        final_feed.append(remainder)
        if remainder != 0:
            featured_articles.append(remainder * 2)

final_feed_sum = sum(final_feed)

print(f"Final Feed: {', '.join(map(str, final_feed))}")
if final_feed_sum >= target:
    print(f"Goal achieved! Engagement Value: {final_feed_sum}")
else:
    shortfall = target - final_feed_sum
    print(f"Goal not achieved! Short by: {shortfall}")
