
import re

# Updated regex pattern for matching names (allows for spaces, hyphens, apostrophes)
name_regex = re.compile(r'^[A-Z][a-zA-Z\'\-]*(\s[A-Z][a-zA-Z\'\-]*)*$')

# Regex pattern for matching phone numbers in various formats
phone_regex = re.compile(r'^(\d{10}|\d{3}-\d{3}-\d{4}|\(\d{3}\)\s*\d{3}-\d{4})$')

# Regex pattern for matching email addresses
email_regex = re.compile(r'^[a-zA-Z][a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
