import time
def random_number_generator(low: int, high:int) -> int:
    now = str(time.perf_counter())
    print("Random number is: \t", low + (float(now[::-1][:3:])/1000)*(high - low))
    
def user_interaction():
    min_val = int(input("Enter the lowest number in the range \t"))
    max_val = int(input("Enter the highest number in the range \t"))
    random_number_generator(min_val, max_val)

user_interaction()