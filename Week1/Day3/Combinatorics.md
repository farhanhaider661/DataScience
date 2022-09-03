# Combinatorics: 
*	It is all about the number of ways of choosing some objects out of a collection.
*	E.g., suppose there are five members in a club, let’s say that their names are A, B, C, D,& E & one of them is to be chosen as coordinator. Anyone can be chosen so there are 5 ways. 
*	It is used to develop estimates about how many operations a computer algorithm will require.

# Principles of Combinatorics:
* # SUM Rule (Additive): 
* If there are n(A) ways to do A and, distinct from them, n(B) ways to do B, then the number of ways to do A or B is n(A) + n(B).
*	Example: Suppose there are 5 chicken dishes and 8 beef dishes. How many selections does a customer have? In this case, an event is "selecting a dish of either kind". There are 5 outcomes for the chicken event and 8 outcomes for the beef event. According to the addition principle there are 5 + 8 = 13 possible selections.
* #	PRODUCT Rule (Multiplicative): 
* If there are n(A) ways to do A and n(B) ways to do B, then the number of ways to do A and B is n(A) × n(B).
*	Example:  Suppose that there are three major auto routes from Washington DC to Chicago and five from Chicago to Los Angeles. Then there are 3 * 5 = 15 major routes from Washington DC to Los Angeles.
*	Inclusion-Exclusion: 
*	If the outcome of an experiment can either be drawn from set A or set B and sets A and B may potentially overlap (i.e., it is not guaranteed that A ∩ B = ∅), then the number of outcomes of the experiment is |A ∪ B| = |A| + |B| − |A ∩ B|.
*	Example:  How many integers from 1 to 100 are multiples of 2 or 3? Let A be the set of integers from 1 to 100 that are multiples of 2, then ∣A∣=50. Let B be the set of integers from 1 to 100 that are multiples of 3, then ∣B∣=33. Now, A∩B is the set of integers from 1 to 100 that are multiples of both 2 and 3, and hence are multiples of 6, implying ∣A∩B∣=16. So, A∪B∣=∣A∣+∣B∣−∣A∩B∣=50+33−16=67.
