def convert_seconds(seconds):
  hours = seconds // 3600
  minutes = (seconds % 3600) // 60
  seconds = seconds % 60
#   if (hours > 0 & minutes > 0 & seconds > 0):
  return hours, minutes, seconds
#   elif (minutes > 0 & seconds > 0):
#     return minutes, seconds
#   elif (seconds > 0):
#     return minutes, seconds

# Example usage:
seconds = 7200
hours, minutes, seconds = convert_seconds(seconds)
print(f"{hours}:{minutes}:{seconds}")