
from hashlib import md5, sha1

message = "Hello, world!"

md5_hash = md5(message.encode()).hexdigest()
sha1_hash = sha1(message.encode()).hexdigest()

print(f"MD5 hash of '{message}': {md5_hash}")
print(f"SHA-1 hash of '{message}': {sha1_hash}")

message1 = "The quick brown fox jumps over the lazy dog."
message2 = "The quick brown fox jumps over the lazy cog."

md5_hash1 = md5(message1.encode()).hexdigest()
md5_hash2 = md5(message2.encode()).hexdigest()

if md5_hash1 == md5_hash2:
  print("Collision found! Both messages have the same MD5 hash:")
  print(f"Message 1: {message1}")
  print(f"Message 2: {message2}")
  print(f"MD5 hash: {md5_hash1}")
else:
  print("No collisions found for these specific messages.")



target_hash = "00000000000000000000000000000000"

for i in range(1000):
  message = f"Attempt {i+1}"
  if md5(message.encode()).hexdigest() == target_hash:
    print(f"Found a message with the target hash: {message}")
    break
else:
  print(f"Could not find a message with the target hash: {target_hash}")

