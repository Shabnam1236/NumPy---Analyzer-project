import numpy as np

def create_array():
    print("Array Creation:-")
    print("Select the type of array to create:")
    print("1. 1D Array\n2. 2D Array\n3. 3D Array")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        elements = list(map(int, input("Enter elements separated by space: ").split()))
        arr = np.array(elements)
    elif choice == 2:
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        elements = list(map(int, input(f"Enter {rows*cols} elements separated by space: ").split()))
        arr = np.array(elements).reshape(rows, cols)
    elif choice == 3:
        dim1 = int(input("Enter first dimension: "))
        dim2 = int(input("Enter second dimension: "))
        dim3 = int(input("Enter third dimension: "))
        elements = list(map(int, input(f"Enter {dim1*dim2*dim3} elements separated by space: ").split()))
        arr = np.array(elements).reshape(dim1, dim2, dim3)
    else:
        print("Invalid choice")
        return None

    print("Array created successfully:\n", arr)
    return arr

def indexing_slicing(arr):
    print("\nChoose an operation:\n1. Indexing\n2. Slicing\n3. Go Back")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        idx = tuple(map(int, input("Enter indices separated by space: ").split()))
        print("Indexed element:", arr[idx])
    elif choice == 2:
        row_range = input("Enter the row range (start:end): ").split(":")
        col_range = input("Enter the column range (start:end): ").split(":")
        sliced = arr[int(row_range[0]):int(row_range[1]), int(col_range[0]):int(col_range[1])]
        print("Sliced Array:\n", sliced)

def math_operations(arr):
    print("\nMathematical operations:")
    print("choose a mathematical operation:")
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
    choice = int(input("Enter your choice: "))
    elements = list(map(int, input(f"Enter same-size array elements separated by space: ").split()))
    second_arr = np.array(elements).reshape(arr.shape)
    print("Original Array:\n", arr)
    print("Second Array:\n", second_arr)
    
    if choice == 1:
        result = arr + second_arr
        print("Result of Addition:\n", result)
    elif choice == 2:
        result = arr - second_arr
        print("Result of Subtraction:\n", result)
    elif choice == 3:
        result = arr * second_arr
        print("Result of Multiplication:\n", result)
    elif choice == 4:
        result = arr / second_arr
        print("Result of Division:\n", result)

def combine_split(arr):
    print("\nChoose an option:\n1. Combine Arrays\n2. Split Arrays")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        elements = list(map(int, input(f"Enter same-size array elements separated by space: ").split()))
        second_arr = np.array(elements).reshape(arr.shape)
        combined = np.vstack((arr, second_arr))
        print("Combine Array (vertical stack):\n", combined)
    elif choice == 2:
        sections = int(input("Enter number of splits: "))
        split_arr = np.array_split(arr, sections)
        print("Split Arrays:")
        for s in split_arr:
            print(s)

def search_sort_filter(arr):
    print("\nChoose an option:\n1. Search a value\n2. Sort the array\n3. Filter values")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        val = int(input("Enter value to search: "))
        indices = np.where(arr == val)
        print("Value found at indices:", indices)
    elif choice == 2:
        sorted_arr = np.sort(arr, axis=1)
        print("Sorted Array (row-wise):\n", sorted_arr)
    elif choice == 3:
        condition = input("Enter condition (e.g., >20): ")
        filtered = arr[eval(f"arr{condition}")]
        print("Filtered Array:", filtered)

def aggregates(arr):
    print("\nChoose an aggregate/statistical operation:")
    print("1. Sum\n2. Mean\n3. Median\n4. Standard Deviation\n5. Variance")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Sum:", np.sum(arr))
    elif choice == 2:
        print("Mean:", np.mean(arr))
    elif choice == 3:
        print("Median:", np.median(arr))
    elif choice == 4:
        print("Standard Deviation:", np.std(arr))
    elif choice == 5:
        print("Variance:", np.var(arr))

def main():
    while True:
        print("\nWelcome to the NumPy Analyzer !")
        print("="*60)
        print("choose an option:")
        print("1. Create a NumPy Array")
        print("2. Perform Mathematical operations")
        print("3. Combine or split Arrays")
        print("4. Search, Sort, or filter arrays")
        print("5. Compute Aggregates and statistics")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            arr = create_array()
            if arr is not None:
                indexing_slicing(arr)
        elif choice == 2:
            math_operations(arr)
        elif choice == 3:
            combine_split(arr)
        elif choice == 4:
            search_sort_filter(arr)
        elif choice == 5:
            aggregates(arr)
        elif choice == 6:
            print("Thank you for using the NumPy Analyzer! Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()