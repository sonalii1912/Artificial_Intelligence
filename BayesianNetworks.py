class Node:
    def __init__(self, name):
        self.name = name
        self.parents = []
        self.probabilities = {}

    def add_parent(self, parent_node):
        self.parents.append(parent_node)

    def add_probability(self, conditions, probability):
        self.probabilities[conditions] = probability

    def get_probability(self, conditions):
        return self.probabilities.get(conditions)


def predict_student_performance(difficulty, intelligence):
    # Create nodes
    grade = Node('grade')
    letter = Node('letter')
    difficulty_node = Node('difficulty')
    intelligence_node = Node('intelligence')

    # Set up parent-child relationships
    grade.add_parent(difficulty_node)
    grade.add_parent(intelligence_node)
    letter.add_parent(grade)

    # Define conditional probabilities
    difficulty_node.add_probability(('Easy',), 0.2)
    difficulty_node.add_probability(('Difficult',), 0.8)

    intelligence_node.add_probability(('Low',), 0.3)
    intelligence_node.add_probability(('High',), 0.7)

    grade.add_probability(('Easy', 'Low'), 0.9)
    grade.add_probability(('Easy', 'High'), 0.6)
    grade.add_probability(('Difficult', 'Low'), 0.4)
    grade.add_probability(('Difficult', 'High'), 0.1)

    letter.add_probability(('A',), 0.3)
    letter.add_probability(('B',), 0.4)
    letter.add_probability(('C',), 0.2)
    letter.add_probability(('D',), 0.1)

    # Perform inference
    grade_probability = grade.get_probability((difficulty, intelligence))
    letter_probability = letter.get_probability((grade_probability,))

    return grade_probability, letter_probability


# Test the prediction
grade_prob, letter_prob = predict_student_performance('Easy', 'High')
print(f"Predicted grade: {grade_prob}")
print(f"Predicted letter grade: {letter_prob}")
