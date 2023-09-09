import time

data = time.time()
today = time.gmtime()

print("Seconde since January 1 1970: " + f'{data:,.4f}' + " or " + f'{data:,.2e}' + " in scientific notation")
print(time.strftime("%b %d %Y", today))