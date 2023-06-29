class CarbonCalculator:
    CONSTANT = 12

    @staticmethod
    #using @staticmethod decorator to create a static method which returns class instances

    def get_valid_float_input(prompt, error_message):
        #To obtain a legitimate input from the client. It will continue to provake the client until a legitmate input is given.
        while True:
            try:
                value = float(input(prompt))
                if value >= 0:
                    return value
                else:
                    print(error_message)
            except ValueError:
                print(error_message)

    @staticmethod
    def calculate_Energy_consumed():
        #obtain values from the client and check its validation 
        Electricity_bill = CarbonCalculator.get_valid_float_input("\nAvg Monthly Electricity bill: ",
                                                                        "Invalid input. Please enter a valid number.")
        Gas_bill = CarbonCalculator.get_valid_float_input("Avg Monthly Gas bill: ",
                                                                    "Invalid input. Please enter a valid number.")
        Fuel_bill = CarbonCalculator.get_valid_float_input("Avg Monthly Fuel bill: ",
                                                                     "Invalid input. Please enter a valid number.")
        
        return round((Electricity_bill * 0.0005 + Gas_bill * 0.0053 + Fuel_bill * 2.32) * CarbonCalculator.CONSTANT, 2)

    @staticmethod
    def calculate_Waste_emissions():
        #obtain values from the client and check its validation 

        Waste_amount = CarbonCalculator.get_valid_float_input("\nAvg Monthly Waste: ",
                                                                       "Invalid input. Please enter a valid number.")
        Waste_recycled_percentage = CarbonCalculator.get_valid_float_input(
            "Avg Monthly Waste Recycled Percentage: ",
            "Invalid input. Please enter a valid number.")
        if Waste_recycled_percentage > 100:
            raise ValueError("Invalid input. Please enter values between 0 to 100.")

        return round(Waste_amount * (0.57 - Waste_recycled_percentage / 100) * CarbonCalculator.CONSTANT, 2)

    @staticmethod
    def calculate_Business_travel():
        #obtain values from the client and check its validation 
        KM_travelled_yearly = CarbonCalculator.get_valid_float_input(
            "\nThe total KM travelled for Business purposes per year: ",
            "Invalid input. Please enter valid KM.")
        Avg_fuel_efficiency = CarbonCalculator.get_valid_float_input("Avg fuel efficiency of car per 100 KM: ",
                                                                              "Invalid input. Please enter a valid number.")
        if Avg_fuel_efficiency == 0:
            raise ValueError("Invalid input. Fuel efficiency must be greater than 0.")
       
        # Calculations

        return round(KM_travelled_yearly * 2.31 / Avg_fuel_efficiency, 2)

def main():
#staring point of the program, a case of CarbonCalculator class and play out the chose computations for energy, waste, 
# and business travel and prints the outcomes.

    carbon_calculator = CarbonCalculator()

    while True:
        print("\nSelect the calculation(s) you want to perform:")
        print("a. Energy Consumed")
        print("b. Waste Emissions")
        print("c. Business Travel")
        print("d. All Calculations")
        print("e. Exit")
        choice = input("Enter your choice (a, b, c, d, or e): ")

        if choice in ["a", "d"]:
            Energy_usage = carbon_calculator.calculate_Energy_consumed()
            print(f"\nEnergy Carbon Emission is: {Energy_usage} KgCO2")

        if choice in ["b", "d"]:
            Waste_emissions = carbon_calculator.calculate_Waste_emissions()
            print(f"\nWaste Carbon Emission is: {Waste_emissions} KgCO2")

        if choice in ["c", "d"]:
            Business_travel = carbon_calculator.calculate_Business_travel()
            if Business_travel == 0:
                print("There is no travel carbon emission.")
            else:
                print(f"\nThe business travel carbon emission is: {Business_travel} KgCO2")

        if choice == "e":
            break
    #if "e" option is selected then the program will exit.

        if choice not in ["a", "b", "c", "d", "e"]:
            print("\nInvalid selection. Please select a valid option.")


if __name__ == "__main__":
    main()
