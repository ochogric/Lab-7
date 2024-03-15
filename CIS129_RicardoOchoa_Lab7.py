def calculate_income(tickets_sold_section_a, tickets_sold_section_b, tickets_sold_section_c):
  """
  Calculates the income generated from ticket sales.

  Args:
    tickets_sold_section_a: The number of tickets sold in section A.
    tickets_sold_section_b: The number of tickets sold in section B.
    tickets_sold_section_c: The number of tickets sold in section C.

  Returns:
    The total income generated from ticket sales.
  """

  income_section_a = tickets_sold_section_a * 20
  income_section_b = tickets_sold_section_b * 15
  income_section_c = tickets_sold_section_c * 10

  total_income = income_section_a + income_section_b + income_section_c

  return total_income


def main():
  """Prompts the user for the number of tickets sold in each section and then displays the amount of income generated from ticket sales."""

  # Get the number of tickets sold in each section.
  tickets_sold_section_a = int(input("Enter the number of tickets sold in section A: "))
  tickets_sold_section_b = int(input("Enter the number of tickets sold in section B: "))
  tickets_sold_section_c = int(input("Enter the number of tickets sold in section C: "))

  # Validate the numbers that are entered for each section.
  if tickets_sold_section_a > 300:
    print("The number of tickets sold in section A cannot be greater than 300.")
    return
  elif tickets_sold_section_b > 500:
    print("The number of tickets sold in section B cannot be greater than 500.")
    return
  elif tickets_sold_section_c > 200:
    print("The number of tickets sold in section C cannot be greater than 200.")
    return

  # Calculate the income generated from ticket sales.
  total_income = calculate_income(tickets_sold_section_a, tickets_sold_section_b, tickets_sold_section_c)

  # Display the amount of income generated from ticket sales.
  print("The total income generated from ticket sales is ${}".format(total_income))


if __name__ == "__main__":
  main()
