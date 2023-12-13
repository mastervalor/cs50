import csv
import sys


def main():
    match = {}
    found_match = False
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py FILENAME identifyfile")

    with open(sys.argv[1], "r") as database:
        reader = csv.DictReader(database)

        with open(sys.argv[2], "r") as file:
            find = file.read()

            for subsequence in reader.fieldnames[1:]:
                match[subsequence] = longest_match(find, subsequence)

            # TODO: Check database for matching profiles

            for data_dict in reader:
                if all(
                    str(data_dict[key]) == str(value) for key, value in match.items()
                ):
                    print(data_dict["name"])
                    found_match = True

            if not found_match:
                print("No match")

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
