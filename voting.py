"""
Voting System

Task:
- Implement a simple voting system.
- Store candidates in a dictionary { "candidate_name": vote_count }
- Allow voters (by ID) to vote only once.
- Use *args to register multiple candidates at once.
- Use **kwargs to update candidate details like party, region.


// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Candidate as a class.
- Voter as a class with has_voted flag.
- Election as a manager class.
"""

"""
Voting System

- Store candidates in a dictionary { "candidate_name": vote_count }
- Allow voters (by ID) to vote only once.
- *args → register multiple candidates at once.
- **kwargs → update candidate details (party, region).
"""

# Store candidates as a dictionary
candidates = {}
# Track voters who have voted
voters = set()


def register_candidates(*names):
    """Register multiple candidates at once."""
    for name in names:
        if name not in candidates:
            candidates[name] = {"votes": 0}
    return f"Candidates registered: {', '.join(names)}"


def update_candidate(name, **kwargs):
    """Update candidate details (like party, region)."""
    if name in candidates:
        for key, value in kwargs.items():
            candidates[name][key] = value
        return f"Candidate '{name}' updated with details {kwargs}"
    else:
        return f"Candidate '{name}' not found."


def vote(voter_id, candidate_name):
    """Allow a voter to vote once for a candidate."""
    if voter_id in voters:
        return f"Voter {voter_id} has already voted."
    
    if candidate_name not in candidates:
        return f"Candidate '{candidate_name}' not found."
    
    candidates[candidate_name]["votes"] += 1
    voters.add(voter_id)
    return f"Voter {voter_id} voted for {candidate_name}."


def results():
    """Display the election results."""
    return {name: data["votes"] for name, data in candidates.items()}



print(register_candidates("Alice", "Bob", "Charlie"))
print(update_candidate("Alice", party="Democratic", region="North"))
print(update_candidate("Bob", party="Republican"))

print("\n--- Voting ---")
print(vote(101, "Alice"))
print(vote(102, "Bob"))
print(vote(101, "Charlie"))  # duplicate voter
print(vote(103, "Daisy"))    # invalid candidate

print("\n--- Results ---")
print(results())

