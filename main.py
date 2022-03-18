import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
symbols = string.punctuation
digits = string.digits

all = lower + upper + symbols + digits

length = 16
password = "".join(random.sample(all, length))
print(password)
