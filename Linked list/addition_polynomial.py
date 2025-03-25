class Polynomial:
    def __init__(self):
        self.terms = {}  # Dictionary to store exponent → coefficient mapping

    def add_term(self, coefficient, exponent):
        if exponent in self.terms:
            self.terms[exponent] += coefficient  # Add coefficient if exponent exists
        else:
            self.terms[exponent] = coefficient  # Insert new term

    def display(self):
        if not self.terms:
            print("0")
            return
        sorted_terms = sorted(self.terms.items(), reverse=True)  # Sort by exponent (descending)
        poly_str = " + ".join(f"{coeff}x^{exp}" for exp, coeff in sorted_terms if coeff != 0)
        print(poly_str)

    @staticmethod
    def add(p1, p2):
        result = Polynomial()
        for exp, coeff in p1.terms.items():
            result.add_term(coeff, exp)
        for exp, coeff in p2.terms.items():
            result.add_term(coeff, exp)
        return result

# Example Usage:
p1 = Polynomial()
p1.add_term(3, 3)
p1.add_term(4, 2)
p1.add_term(5, 1)
p1.add_term(6, 0)

p2 = Polynomial()
p2.add_term(5, 3)
p2.add_term(2, 2)
p2.add_term(7, 1)
p2.add_term(8, 0)

print("P1(x):", end=" ")
p1.display()

print("P2(x):", end=" ")
p2.display()

result = Polynomial.add(p1, p2)
print("P1(x) + P2(x) =", end=" ")
result.display()
