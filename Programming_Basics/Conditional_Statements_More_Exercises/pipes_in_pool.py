pool_volume = int(input())
first_pipe_debit = int(input())
second_pipe_debit = int(input())
missing_worker_hours = float(input())

first_pipe_volume = first_pipe_debit * missing_worker_hours
second_pipe_volume = second_pipe_debit * missing_worker_hours
total_volume = first_pipe_volume + second_pipe_volume

if total_volume <= pool_volume:
    filled_pool_percentage = (total_volume / pool_volume) * 100
    first_pipe = (first_pipe_volume / total_volume) * 100
    second_pipe = (second_pipe_volume / total_volume) * 100
    print(f"The pool is {filled_pool_percentage:.2f}% full. Pipe 1: {first_pipe:.2f}%. Pipe 2: {second_pipe:.2f}%.")

else:
    overflow = total_volume - pool_volume
    print(f"For {missing_worker_hours:.2f} hours the pool overflows with {overflow:.2f} liters.")
