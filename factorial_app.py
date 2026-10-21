import streamlit as st

def factorial_calculate(n):
    if n == 0:
        return 1
    else:
        return n * factorial_calculate(n-1)

def main():
    st.title("Factorial Calculator")
    number = st.number_input("Enter a number:", min_value=0, max_value=200, value=0)

    calculate = st.button("Calculate")
    if calculate:
        factorial = factorial_calculate(number)
        st.write(f"The factorial of {number} is {factorial}.")

if __name__ == "__main__":
    main()
