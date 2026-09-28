A = {"x1": 0.5, "x2": 0.7, "x3": 0}
B = {"x1": 0.8, "x2": 0.2, "x3": 1}

AUB = {}
Aint = {}

# Find union and intersection
for key in A:
    if A[key] > B[key]:
        AUB[key] = A[key]
        Aint[key] = B[key]
    else:
        AUB[key] = B[key]
        Aint[key] = A[key]

# Find complement of A
print("Complement of A:")
for key in A:
    print(key, 1 - A[key])

# Display union and intersection
print("Union:", AUB)
print("Intersection:", Aint)



# Fuzzy set operations are used to perform operations on sets where an element can have a partial membership value between 0 and 1. Unlike classical sets, an element does not have to be completely inside or outside a fuzzy set. Union takes the maximum membership value, Intersection takes the minimum membership value, and Complement is calculated as 1 − membership value. 