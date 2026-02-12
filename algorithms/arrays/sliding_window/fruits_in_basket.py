def fruits_in_basket(fruits):
    """
    You are given an array of strings representing a sequence of fruit trees e.g. ['Apple', 'Banana', 'Orange'].
    You have one basket and you are to pick teo distinct fruits from the tree and put them into the basket.
    Your goal is to return the maximum number of fruit trees you can pick from given the below restrictions

    Restrictions:

    You can only have two types of fruit in each basket
    once you start picking you can't skip a tree and then keep picking

    Time/Space Complexity Analysis
    Time Complexity: O(N), where N is the number of fruits in the input array. The function iterates through the fruits once, performing constant-time operations for each fruit. Therefore, the time complexity is linear with respect to the size of the input.
    Space Complexity: O(1), as the space occupied by our variables remains constant regardless of the size of the input.
    """

    start = 0
    basket = {}
    max_no_fruits = 0

    for idx in range(len(fruits)):
        fruit = fruits[idx]
        basket[fruit] = idx

        if len(basket) > 2:
            min_idx = min(basket.values())
            del basket[fruits[min_idx]]
            start += min_idx

        max_no_fruits = max(max_no_fruits, idx - start + 1)

    return max_no_fruits
