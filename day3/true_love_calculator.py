first_name = input("First person name")
second_name = input("Second person name")

full_str = (first_name + second_name).lower()

t_count = full_str.count("t")
r_count = full_str.count("r")
u_count = full_str.count("u")
e_count = full_str.count("e")

true_count = t_count + r_count + u_count + e_count

l_count = full_str.count("l")
o_count = full_str.count("o")
v_count = full_str.count("v")
e_count = full_str.count("e")

love_count = l_count + o_count + v_count + e_count
true_love_score = int(str(true_count) + str(love_count))

if 10 > true_love_score > 90:
    print(f"Your score is: {true_love_score}, you go together like coke and mentos")
elif 40 <= true_love_score <= 50:
    print(f"Your score is {true_love_score}, you are alright together")
else:
    print(f"Your score is {true_love_score}")
