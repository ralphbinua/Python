import pyshorteners

long_url = 'https://www.affiliatemarketer.com/product-link?utm_source=email&utm_medium=newsletter&utm_campaign=holiday_sale&ref_id=user12345'

s = pyshorteners.Shortener()

short_url = s.tinyurl.short(long_url)

print(f"Short URL: {short_url}")
# Output: Short URL: https://tinyurl.com/xxxxx