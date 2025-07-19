with open('codepractice1.txt', 'r') as f:
    lines = f.readlines()

# Strip newlines and filter out any empty lines
lines = [x.strip() for x in lines if x.strip()]

if len(lines) != 3:
    raise ValueError("Expected 3 lines of input")

principal, rate, time_period = lines

principal = float(principal)
rate = float(rate)
time_period = float(time_period)

compounded_principal = principal * (1 + rate) ** time_period
print(compounded_principal)

